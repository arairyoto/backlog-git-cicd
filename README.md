# Backlog Git CI/CD
## 説明
BacklogのGitと連携するCI/CDパイプラインを構築するSAM Templateです。

## 構成
![OverView](https://github.com/arairyoto/images/blob/master/backlog-git-cicd/Backlog%20Git%20CI_CD.png)
BacklogのGitのWebhookによってソースをS3にコピーし、CodePipelineのS3トリガー機能を利用して、CodePipelineを駆動します。
template.ymlとtemplate.cfn.ymlではCodePipelineの構成が異なります。
- template.yml
1. Source：S3からソースコードをコピー
2. Approval：手動承認プロセス
3. Build：ソースコードにあるbuildspec.ymlファイルに従ったビルドプロセス
- template.cfn.yml
1. Source：S3からソースコードをコピー
2. Test：ソースコードにあるbuildspec.ymlファイルに従いビルドをし、CloudFormationテンプレートを作成
3. Build：2で作成したCloudFormationテンプレートでChangeSetを作成
4. Approval：手動承認プロセス
5. Deploy：ChangeSetのデプロイ
## 使い方
1. SAM Templateのパッケージング
```
aws cloudformation package \
    --template-file {template.yml or template.cfn.yml} \
    --output-template-file YOUR_PACKAGE_FILE \
    --s3-bucket YOUR_BUCKET
```
でyamlファイル(YOUR_PACKAGE_FILE)を作成します。

2. デプロイ
```
aws cloudformation deploy \
    --template-file YOUR_PACKAGE_FILE \
    --stack-name YOUR_STACK \
    -- capability CAPABILITY_NAMED_IAM \
    --parameter-overrides ParameterKey1=ParameterValue1 ParameterKey2=ParameterValue2 ...
```
で1で作成したyamlファイルをデプロイします。
parameter-overridesで指定するパラメータは下記の通りです。
- Environment:環境名
- AppName:アプリケーション名
- TargetBranchName:ターゲットのブランチ（カンマ区切りで複数指定可能です）
- Username:Backlog Gitのユーザ名
- Password:Backlog Gitのパスワード
- InputSourceCodeFilePath:ソースコードをS3に置く際のファイル名
- Email:メールアドレス（承認プロセスのメール通知先）
3. Webhook設定

BacklogでターゲットとなるリポジトリのWebhookに、2でデプロイした時に作成されたAPI Gatewayのエンドポイントを指定します。
（WebhookApiEndpointという論理名でCloudFormationに出力しています）
4. Backlog Gitの操作

Backlog Gitで2で指定したブランチにpush操作が発生すると、CI/CDが駆動されます。
CI/CDのビルドには、ソースコードに含まれるbuildspec.ymlを利用します。
そのため、必ずソースコードにbuildspec.ymlファイルを含めるようにしてください。
### buildspec.ymlファイル記述方法
※　phases>install>runtime-versionに必ずランタイムを記載してください。（https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/build-spec-ref.html#runtime-versions-buildspec-file）
※　template.cfn.ymlを利用する場合は、必ずパッケージングしたCloudFormationのテンプレートを"packaged.yml"として出力してください。

例1) CloudFormationテンプレートの出力
```
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

例2) ServerlessFrameworkでのデプロイ
```
version: 0.2

phases:
  install:
    runtime-versions:
      nodejs: 8
    commands:
      - |
        npm install serverless
        npm install
  build:
    commands:
      - |
        sls deploy

```
## 備考
- Lambdaの環境変数にBacklogのログイン情報をベタで記載しています。
- API Gatewayに認証をかけていません。（本番環境で利用する場合には、認証をかける必要があります。）

## License
MIT License (MIT)
This software is released under the MIT License, see LICENSE.txt.