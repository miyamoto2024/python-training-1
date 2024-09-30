## 必須パッケージ

- **Python 3.11**
    - 最新バージョンのPython 3.11をインストールしてください。
- **pip (Python 3.11に対応)**
    - Python 3.11に対応したpipを使用してください。
- **AWS CLI**
    - AWS CLIをインストールし、設定を行ってください。
- **AWS SAM**
    - AWS Serverless Application Model (SAM) CLIをインストールしてください。
- **Docker**
    - Dockerをインストールし、Dockerデーモンが実行されていることを確認してください。

## インストール手順

### Python 3.11 と pip

1. [Python公式サイト](https://www.python.org/downloads/)からPython 3.11をダウンロードしてインストールします。
2. インストール後、以下のコマンドでpipをアップグレードします。
     ```sh
     python3.11 -m ensurepip --upgrade
     ```

### AWS CLI

1. [AWS CLIのインストールガイド](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)に従ってインストールします。
2. インストール後、以下のコマンドでバージョンを確認します。
     ```sh
     aws --version
     ```

### AWS SAM

1. [AWS SAMのインストールガイド](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)に従ってインストールします。
2. インストール後、以下のコマンドでバージョンを確認します。
     ```sh
     sam --version
     ```

### Docker

1. [Dockerの公式サイト](https://www.docker.com/get-started)からDockerをダウンロードしてインストールします。
2. インストール後、以下のコマンドでDockerが正常に動作していることを確認します。
     ```sh
     docker --version
     ```

これらのパッケージをインストールした後、プロジェクトのセットアップを進めてください。

### 利用方法
コマンドはMakefileを通じてください。