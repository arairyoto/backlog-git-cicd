# Backlog Git CI/CD
## 説明
BacklogのGitと連携するCI/CDパイプラインを構築するSAM Templateです。

## 構成
BacklogのGitのWebhookによってソースをS3にコピーし、CodePipelineのS3トリガー機能を利用して、CodePipelineを駆動します。
template.ymlとtemplate.cfn.ymlではCodePipelineの構成が異なります。
- template.yml
1. Source：S3からソースをコピー
2. Approval：手動承認プロセス
3. Build：ソースにあるbuildspec.ymlファイルに従ったビルドプロセス
- template.cfn.yml
1. Source：S3からソースをコピー
2. Test：ソースにあるbuildspec.ymlファイルに従いビルドをし、CloudFormationテンプレートを作成
3. Build：2で作成したCloudFormationテンプレートでChangeSetを作成
4. Approval：手動承認プロセス
5. Deploy：ChangeSetのデプロイ
## 使い方
```
aws cloudformation package \
    --template-file template.yml \
    --output-template-file packaged.yml \
    --s3-bucket YOUR_BUCKET
```
でpackage化されたyamlファイルを作成します。
その後、
```
aws cloudformation deploy \
    --template-file package.yml \
    --stack-name YOUR_STACK \
    -- capability CAPABILITY_NAMED_IAM \
    --parameter-overrides ParameterKey1=ParameterValue1 ParameterKey2=ParameterValue2 ...
```
でデプロイします。
※ソースのビルドには、buildspec.ymlが必要です。
※ソースコードにbuildspec.ymlを含め、ビルドの内容を記載するようにしてください。

```例1) buildspec.yml
version: 0.1

phases:
  install:
    runtime-versions:
        python: 3.7
    commands:
      - |
        pip install -U pip
        pip install -r requirements.txt
  pre_build:
    commands:
      - |
        [ -d .cfn ] || mkdir .cfn
        aws configure set default.region $AWS_REGION
        for template in src/* cfn.yml; do
          echo "$template" | xargs -I% -t aws cloudformation validate-template --template-body file://%
        done
  build:
    commands:
      - |
        aws cloudformation package \
          --template-file cfn.yml \
          --s3-bucket $S3_BUCKET \
          --output-template-file .cfn/packaged.yml

artifacts:
  files:
    - .cfn/*
    - params/*
  discard-paths: yes

```
```例2) buildspec.yml
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.7
  build:
    commands:
      - |
        aws s3 sync assets/ s3://${ENV}-serverless-deployments-arh/

```
## 備考
- Lambdaの環境変数にBacklogのログイン情報をベタで記載しています。
- API Gatewayに認証をかけていません。（本番環境で利用する場合には、認証をかける必要があります。）

## License
MIT License (MIT)
This software is released under the MIT License, see LICENSE.txt.