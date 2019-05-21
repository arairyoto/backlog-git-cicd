# Backlog Git CI/CD
## 説明
BacklogのGitと連携するCI/CDパイプラインを構築するSAM Templateです。

## 構成
![OverView](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Backlog%20Git%20CI%2FCD#R7VxZe6rK0v41uTz7YR4uQUYVUHHCm%2FMwySCTjMKv%2FxqjK3HIWu7sJCtrny%2FmSeiiaZp636qurm58QgfxQczNzFdSx42eEMg5PKHcE4LAOAaDf72kfZZQKPEs8PLAOVV6EehB556E0ElaBY5bXFQs0zQqg%2BxSaKdJ4trlhczM87S5rLZNo8u7Zqbn3gh024xupavAKf2TFIaglxOSG3j%2B6dYUfjphmfbOy9MqOd3vCUG3x5%2Fn07F5butUv%2FBNJ21eiVD%2BCR3kaVo%2BH8WHgRv1uj2r7fk64Y2zP%2Fqdu0n5yAWEA5M4STsQTdIYjFD%2FwZ5bqM2ocs%2BPcOxo2Z6Vc3w8t28AfkJZM7dP%2BGGg5JiFfzwFgUJR5unOHaRRmh%2BvRKHjDzizDaLoLE%2FSBFzNernpBKDXV%2BLnNs4gIL3krLK%2BITuNA%2Ft0vE2TUjDjIOpJt3Rzx0zMk%2FjUQxg5le%2F1yS%2Fj6PRMt1o8KbZ289I9vBKdtCq6aeyWeQuqnM6i2AnhkwXA53LzwicSPmnbf0UlnDxVNE8c9n60%2FYIjODhB%2BSCs%2BK9hvYDulTKAvrO%2BSnzwemP%2Fy2wK9C87SivnCkigTAGncGDqb6J5cY9LHr0J6w2LeKL%2F3HCD%2BOcU%2BAjcCfISd%2BQWdxy5hf3sID8UdRj%2BYNgL9BZzHsIRDH0b838lzPhZtSeYUYr6C781cOIsfA01jX4C1OcR9xWyrgPGtFMxzUs%2F9dLEjPgX6StorsCPTMuN2B9j2U99Mvw4IO4hKNf93YBankvGqYH%2BmDucOnIstK8KEzcPgIrc%2FCxLgLpeNdQXjWMR%2BlF%2Bae1Yal%2BXrtt7kxBFWuX2SZ1hecA1iy10acGsBHqC6Vz7nxOUpZl7bvmTeien0EPyU3rlbmSWQX0ZhtwjyvFSJs%2FN9lWFLA2SsnjV8qQXvLCWoLAL1uLYVXRwVZ%2BCqZ%2FVBwfPPXjjahS9vJrGz%2BZw7vCzfk%2FX%2FaQjJHLpVTHyqqFnAG4aOprRD%2FW%2Bz7LQB0Kiv%2BVEY2AcnhsDrv0XxK9FejTFK6fKIRzK%2Fa85VZimL1Am0duxk0BvHSrxAQ71rtU%2BMHymVRkFCVDxeSICXYc5%2FfMHYGox7n3qJC2CMkgTcM5KyzKNX1VgosDrT5Rp1sfVp5IN9Nk7ql%2FSysyC%2F3pm6Ta9Qd7wiWZIDH6bT58Q%2BSDQnYj30wbEu%2FghfxJ%2BkRlbjvlGTI19KXRfHc38bGj9M8CzU8fNgsztu3MLIYnTg%2F7JPxFCAr%2Bcb6L0LYAEeQ9A6idRxj8C8IFx83sBaFVBdGdS%2BwXokdQVehT9u83vgYzB90IPGGCU3hn6vgA%2BGr4MXFAau%2BM%2Fv9j8iD8KwD6ftE3z2Hy%2BwW8B8Qdo3yeCIf84EBuztP3f40TJyyiGgJAb%2BCjkS%2BGj%2FiT4iqT4LROH61waAUMPR58v0g%2FHjv41dm7iMP1qU6%2FlyCyKft79Ws2fnu%2F62mTXeSXuV8muk6J%2Bmex6nRKHbrE9y%2F5eTuw26QVfxlbAL1w28WgSiiCuGoKvGvq4JNR99T%2BQjniUkfArPr6w8z2MvMy%2FfnH6Fbll5JuLIN%2BEjhhJXoUZOP5OQuLITVPQF1PygQzLv5eSb1Ltlx4S%2FV6UxC%2BXBTDsnWl6HEZ%2F3tBn0%2FGBnNG%2Fl47%2FaIEK%2B16MJK4Yib%2BXkQj684Y%2Bm5EPJMG%2BipHvJxH2IInw70Ui8opExHtJdLWQedPQZ5OIuuXM%2F6%2Ftf7rrxB9k%2FfdY26fxq9X2T13bJ%2Bgr26Ku9i89alsUcjmpIr46gv1G0%2Fx%2F7KC%2Fi%2BO9mnET9DsnONccJb54xn3m5seQ48MiSvi3RpTkg26R%2BlacxK9W2KhrP%2FNwFgi9bIi8nr1%2FNif%2FqI1%2BF5THqD%2BV89Qt59%2FcJ%2Fab4wDsauM5gZE%2F5fN1fZJAfk8ccO3qya81qwcyWW%2B9%2BABfLNnATx%2Fz5kPf4MQsAX37VRygHQgEeBB8%2FH%2FvvYg32f03NpFcTXTQc8b7lY9GSfjWScPXTvDjtnB9RErnjSkF%2FB4ncj%2FYg%2F62Z3u%2FM3p0XkJ8qwEYgy9T1Sh0tej6qKe4aei8a%2FSrPMUDKZ3z%2BmoQH180%2B%2FUS7hvj8MvrY2%2Bu8hbZ87LxNjj07oc93pI5S6GzBBw7ZgnGaua5iAhZ4j0hg2DJarMGGoleyoAfVV%2F4%2FMIDRxoP%2FnD%2BgFF6%2BdDSh3J%2FYMCssuSXgy7rFXv%2BpYoWD8GgxG5nM2hvEN2mobsNOqcqo%2BuG2RgaqXxHcGPg09nRAadHW4zKAT%2BFGgVEEiZJDE5MxA1WOC0ynoWwSUxRamwAr8fGOU5LElnSNELGPDru9v19NAejEpd2EYqg9zFu980gZObAo5IKqnAPuipJi4ifLmdYoiEOgZuBwrQMAg3HzHrJL0SRqmt6bnlVmNLDdu%2B25qZOQNNd4mkoFA0L3WQhRizgKq4QbeYnLCMPJdGwsMypIkyt1qEOqh%2FAjS2bIja40EypVQxrQJiZ2tBV8L6jZYVtZnt37sVjKIg0I7LDLdX58hD0mCXEHZ8g5GqGjdnEIzgo0AbVJG0QblfHPtyyhmg03ZrP%2B7pG4Q422zFvbDI5pOlmSspDFt6vpACeStQsZ%2F2dKPddGjvs1lUDcCTClbjX7SEsd16%2BWRNmHjaOvHZ5rVtYlr9LSJIvEWk8LibKFhKjWN2p%2FGI2pQ6dMKMUgduJUcUx1izy%2BGg13CleS6GB6fLzphGVDcYOlwHKGQB5QUJ0xRbHS0pZdBBq2GNqaWHGMAtXe96OO8PY5OEqw%2BjYM3qsfbpgqM2E9V1KXk7ZrdSaZAg6YJjIJKtWIq%2Bk0yxw5opiy5spO5cwZd553IgfYZUk8Soz4Usl0EXNMMpmL8YzU2zHqnLYOyY%2B9VF%2FsJfFnBuvci6fD20sQnZmtquilaipG3U%2F48nhINe8RdTMMgX0Z6fSgUlyfCJmyz0d65LmiOlyrIQtT3jrihdGGyGJszHQGCHW0EFrdvS2KWnBH8zB5TS3pjYWR%2FLTUYhIbLw5fVjvMIh3HIQumqKERWtsyqaQx8mwGG8glo6nz%2BaDc02rdlOiSxegpPg1FnYGohWEIHWyBdqXKdiBLc2f0Z4yQWEHQvhDzadx7RaZGiuHjNNloVgudSXgBpjhkzP0EFc0HSWF27E41%2BkpsQbOAFjTIfNWI3CXzYLaUdFqznHcmgy3%2BmEuxnxq5Du51uuUzDLL97VSFF18gxz8TK9GwHiFQFPx6Xhp1nikYeIgl0Lw%2BIKQEIe821HSwvXH62QBZ5N50W5J2eJUcE%2FwGyWkskAjbqHQvLudRx2QMWXTZWiq7XqDwfyJPazHaD3fSQQ76XXqrcFfarPIU7b3D4KrYnqlybxfG8NVogwbdpu5JRtowEsImO6xi9L3kklATxofSOQSG6Fbw%2FdGk5W2sCSDCxtmZQ%2FBKS43LCKE9vN2lfaqGKQVKs9NcxlymR4S4GoWVGO9OYSToVvMiFgEYwWr9a5qPRi4QaEpzky2gW5ygbOc1DaJINEqiORkmvG40FpEpn8A9i%2FARrNrkKiiVtHeXUR0LHZox3GajE3bMRcWNhMLyFZu0OUiX07ElGasugy5KdIt2d770b1B19tBEHJLWlxyOMDCzyWmGSq0u2N8VMVXw3QCmWLFtw7HL1PFmGJDmwPGGnDIjAvGTIFO6Vqqa95Qo0mI7NlNtto7cU5na6BogR0CixR4xBlQJLxtpPJgczoKjEkNdaUBw98gEWOHM7adzWS8rxKmyZNd2dQyg8d7eSRbA8BFNtzT7Xq%2FXIPhkbWZuTeE0ABWLJLq8XfDsta0nsrEAjEnG85YYBAvbvneW250K8RXa0WyxsO21%2FFmN9mldMqN1pEHrhY8p%2FKxIOcPA2ioqDwh0p0NlWAwmmaOImN6GXr5jhEJSeTzfH6wPRYdTCb0Yr0EHtGlltiU1sagHZFkxopnbNrAwI22ZKvNNIbFje%2FV1vhgmJ4KIglWtdVwxIVjLS2WhmxNzTokttBIn6LuAWnweCBvhR1frpw9POHsA68nWbgf1f2zTdZTqsFLzmFH3Kj0x6Plbi4QedM7GGzPynOLjxfdeoBq%2FDrnF6t4OihVVcOd6YJipLijrNAZMNSsns%2FtWLFbD48kVZDNBliCsCA8XbJVIe%2FqQGiara0aOj2jaryyDaMi1DDbavZgnXDpmmk6xm21DDM1uxRcOiIhLSrjdYN7S1vYppu9yyQNOaRCZy337iXAJ1u6yoXBHvXHCWZx6B4j4XBUdrmBdyTubFHFqGZ576yqbpJQU3w1oLHxzDekeqFlrIPTQT8QKkeHxs7rVne37rAT9%2FQE6agERDm4mqQi280PLq8bWUDNunAcUIsJDqmz5WrhDnfdZF7Pt6RheXPCS4Rwtle6Vx8C2xG9O1mLfcQhkei8P4DxKhYUZLjTFqzIkd1m3ngeW%2FBZodeBMu0jnSKZadiwHfAWREmrjbygIKKREU3wdy3b6gGLmBAmrVswXribhUxuR7uRjGRqOt0wtaZqwUxgZqlILyCClY3NNDjgqGESWe%2FXSl0yrVHamivFMCSk2LtFL1utVU2p9zt1NycstVrppS7SBtMEFrGHxEJhMOClvcbh4oofYzFsNhjl1yF6WO%2BHsAK1h%2BGsWNUzfyAxYcfldHg0HXEhlXN0xhysWSG6fEaAcIFtNqzoirhAR%2ByqD4IYuUbKaMRTXOBTKjEbSTLoUdxKqjLoY4JOAmGxoBbT6cG15dLrlrXro7MYnUzXFJyNknWMWV6%2BFerxQjHdiaq3c0tX2FFsuf6hDoHS2QU13OmjiXHouBGier0Nd7OF5qxIL0mrCDGWQcuroz3tVvZhs3FLrvSj3pNFKA6VRhD17pWe0U6110bGcMuRcqOvdcdazmg82sveiJnH%2BijZB4SYTMi5sJAUCt%2BgS27AHuapVRBDbYJX1nFwESrwQOyUSIjIGQpLd%2BYlCWzmuis3OTkUKp9sszAn2CZU56o%2F57HiGOoyfCTMd3o1jQeDj5k%2BwzR0s4OYuLOVkbozy6I%2BbQL9wEb%2B9y1wfNKc983E2q%2F3HX6vZZCr7YLEe%2FcdwtfLKV%2B9CvLAmwSfsYfhTbZ8E3yRU6b0h7Fj5PsARnHqqiHiLwJDMJyCIQjHqfP2rK%2FC%2B4GXDh73GDT1GnP4Lwj9yoXRb%2BYSYPpqFer6y14epsyVc8E%2BzydYY7RYWnLXjqt9jPAtvYLgO29GT6rCv6EJGDjLS2LkbhF0pnWs0ENrVmVanNLoT3deWrjOesWB4xyXtE7rIOA2OPuEc%2FdT65d5%2BJt351%2B4dTPI36Hb2%2BM%2Befn6F0YQN2M%2BdodUyAeM%2BXfRuV3LWLmWn6a7%2F1GAXr0mcnaxd76Wh%2FxKiG6TyHbUP%2F3%2FKkDXkTOK3wL0QTYEii9fsPbsEF%2B%2BxQ7l%2Fw8%3D)
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
    --template-file package.yml \
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
### buildspec.ymlファイル記載方法
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
```例2) ServerlessFrameworkでのデプロイ
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