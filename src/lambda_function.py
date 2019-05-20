import boto3
import logging
import os
import shutil
from urllib.parse import urlparse, unquote
import git
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORK_DIR = '/tmp'
TEMP_DIR = '.repo'

TARGET_REFS = [ 'refs/heads/' + branch for branch in os.getenv('TARGET_BRANCH', '').split(',') ]
BUCKET_NAME = os.getenv('BUCKET_NAME')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
FILE_PATH = os.getenv('FILE_PATH')
SNS_TOPIC = os.getenv('SNS_TOPIC')

s3 = boto3.resource('s3')
sns = boto3.resource('sns')

def lambda_handler(event, context):
    # backlog payload
    logger.info(event)
    payload = json.loads(unquote(event['body'].replace('payload=', '')))
    logger.info(payload)
    if payload['ref'] in TARGET_REFS:
        # generate repository url
        _ = urlparse(payload['repository']['url'])
        url = _.scheme + '://' + USERNAME + ':' + PASSWORD + '@' + _.netloc + _.path + '.git'
        logger.info(url)
        # commit id
        commit = payload['after']

        os.chdir(WORK_DIR)
        logger.info(os.listdir(os.getcwd()))
        
        if not os.path.isdir(TEMP_DIR):
            os.mkdir(TEMP_DIR)
        else:
            shutil.rmtree(TEMP_DIR)
        # git clone
        try:
            git.exec_command('clone', url, TEMP_DIR)
            git.exec_command('checkout', commit, cwd=TEMP_DIR)
            shutil.make_archive('src', 'zip', TEMP_DIR)
            logger.info(os.listdir(os.getcwd()))
            s3.meta.client.upload_file('src.zip', BUCKET_NAME, FILE_PATH)
        except Exception as e:
            logger.error(e)
            sns.Topic(SNS_TOPIC).publish(
                Subject='FAILED TO UPLOAD',
                Message=str(e)
            )
        else:
            sns.Topic(SNS_TOPIC).publish(
                Subject='UPLOAD COMPLETE',
                Message=json.dumps(payload)
            )
    return {
        'statusCode': 200
    }