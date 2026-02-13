# SQL Injection脆弱性デモアプリ

これはSQLiteを使用したシンプルなExpressアプリで、製品検索APIにおけるSQL Injection脆弱性を実演します。

## 機能
- SQL Injectionに対して脆弱な製品検索エンドポイント
- 41個のサンプル製品を含むSQLiteデータベース

## インストール

1. ターミナルを開き、`demos`フォルダに移動します：
   ```powershell
   cd "【クローンした場所】\ACM-Hands-On-Demo-1-2\demos"
   ```
2. 依存関係をインストールします：
   ```powershell
   npm install express sqlite3
   ```

## アプリの実行

サーバーを起動します：
```powershell
node sqlinject.js
```

以下のように表示されます：
```
API server listening on port 8080
```

## 脆弱なエンドポイントへのアクセス

ブラウザを開くか、curl/Postmanを使用してアクセスします：
```
http://localhost:8080/search?name=Apple
```

### SQL Injectionの実演
悪意のある入力で検索を試みます：
```
http://localhost:8080/search?name=' OR 1=1 --
```
これによりすべての製品が返され、SQL Injection脆弱性が示されます。

## 注意事項
- デモンストレーション目的のみです。本番環境ではこのコードを使用しないでください。
- データベースをリセットするには、アプリを再起動してください。