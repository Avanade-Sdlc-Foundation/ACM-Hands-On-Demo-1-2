# SQL Injection脆弱性デモアプリ

これはSQLiteを使用したシンプルなExpressアプリで、製品検索APIにおけるSQL Injection脆弱性を実演します。

## 機能
- SQL Injectionに対して脆弱な製品検索エンドポイント
- 41個のサンプル製品を含むSQLiteデータベース

## SQL Injection脆弱性デモアプリ起動方法

| 方法 | 難易度 | 必要な準備 | 利点 | 欠点 |
|------|--------|------------|------|------|
| Node.js インストール | ⭐⭐ | Node.jsのダウンロード・インストール | 元のデモと同じ動作 | インストールが必要 |
| Python版 | ⭐⭐⭐ | Python + Flask | 多くの環境でPythonは利用可能 | 異なる言語 |

**📋 [Setup_Guide.md](Setup_Guide.md) - セットアップ方法**


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

## 次のステップ
脆弱性を確認できたら、以下のガイドでセキュリティ修正を学習してください：

**🛡️ [Security_Fix_Exercise.md](Security_Fix_Exercise.md) - GitHub Copilotを使った修正手順**