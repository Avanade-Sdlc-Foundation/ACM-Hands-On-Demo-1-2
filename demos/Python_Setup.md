# Python版SQL Injectionデモのセットアップ

## 前提条件
- Python 3.x がインストールされていること

## 依存関係のインストール

### 方法 1: pipを使用（推奨）
```powershell
pip install flask flask-cors
```

### 方法 2: condaを使用（Anacondaユーザー）
```powershell
conda install flask
pip install flask-cors
```

## 実行方法

1. demosフォルダに移動：
```powershell
cd "【クローンした場所】\ACM-Hands-On-Demo-1-2\demos"
```

2. Python版スクリプトを実行：
```powershell
python sqlinject_python.py
```

## テスト方法

ブラウザで以下のURLにアクセス：

### 正常な検索
```
http://127.0.0.1:8080/search?name=Apple
```

### SQL Injection攻撃テスト
```
http://127.0.0.1:8080/search?name=' OR 1=1 --
```

この攻撃により、すべての製品データが表示されます。

## 注意事項
- これはセキュリティ学習目的のデモです
- 実際のアプリケーションでは決してこのようなコードを使用しないでください
- プリペアードステートメントを使用して SQL Injection を防止してください