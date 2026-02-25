# 演習 1: 脆弱性アプリケーションのセットアップ

| [← 前の手順](./0-prereqs.md) | [次の手順: SQL Injection攻撃の実演 →](./2-vulnerability-demo.md) |
|:--|--:|

このセクションでは、SQL Injection脆弱性を含むPython製のWebアプリケーションを起動し、動作確認を行います。

## シナリオ

セキュリティ監査の一環として、既存のWebアプリケーションにセキュリティ脆弱性が報告されました。まずはこのアプリケーションを起動し、正常な動作を確認してから脆弱性の調査を進めます。

## ? 必須 1. Python版アプリケーションの起動

### 1.1 demosフォルダーへの移動

VS Code統合ターミナルで以下のコマンドでdemosフォルダーに移動します：
```powershell
cd demos
```

### 1.2 必要なライブラリのインストール

Flaskライブラリをインストールします：
```powershell
pip install flask
```

### 1.3 Python版アプリケーションの起動

sqlinject_python.pyファイルを実行します：
```powershell
python sqlinject_python.py
```
以下のメッセージが表示されることを確認します：
```
* Running on http://127.0.0.1:8080
```

## ? 必須 2. アプリケーションの動作確認

### 2.1 正常な商品検索機能の確認

以下のURLにアクセスして正常な検索機能を確認します：
```
http://localhost:8080/search?name=Apple
```
Appleを含む製品情報が表示されることを確認します。

### 2.2 空の検索結果の確認

存在しない商品名で検索してみます：
```
http://localhost:8080/search?name=NonExistentProduct
```
検索結果が空であることを確認します。

## ? 参考 3. アプリケーションの構造理解

### 3.1 ソースコードの確認

1. VS Codeで脆弱性ファイルを開きます：`demos/sqlinject_python.py`

2. SQLクエリの構築部分を確認します：
     ```python
     query = f"SELECT * FROM products WHERE name LIKE '%{product_name}%'"
     ```

### 3.2 データベース構造の理解

このアプリケーションはSQLiteデータベースを使用し、製品情報を格納するproductsテーブルから検索を行います。

## ? トラブルシューティング

### 問題が発生した場合

1. **ポート衝突エラー**: 別のアプリケーションが既にポート8080を使用している可能性があります
   - 他のアプリケーションを終了するか、ポート番号を変更してください
   
2. **パッケージインストールエラー**: 
   - `pip install --upgrade pip` でpipをアップグレードしてから再度インストール

3. **ファイルが見つからないエラー**: 
   - 現在のディレクトリを確認し、`Get-Location`でdemosフォルダーにいることを確認

## まとめと次のステップ

Webアプリケーションが正常に起動し、基本的な検索機能が動作することを確認できました。次は実際にSQL Injection攻撃を実行し、脆弱性の危険性を体験してみましょう。

## リソース

- [Flask公式ドキュメント](https://flask.palletsprojects.com/)
- [SQLite公式サイト](https://www.sqlite.org/)

---

| [← 前の手順](./0-prereqs.md) | [次の手順: SQL Injection攻撃の実演 →](./2-vulnerability-demo.md) |
|:--|--:|