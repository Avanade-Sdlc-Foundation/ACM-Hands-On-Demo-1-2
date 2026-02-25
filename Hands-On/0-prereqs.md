# 演習 0: 環境のセットアップ

| | [次の手順: 脆弱性アプリケーションのセットアップ →](./1-vulnerable-app-setup.md) |
|:--|--:|

このセクションでは、ハンズオンに必要な環境を整備し、プロジェクトリポジトリをローカルに設定します。

## シナリオ

セキュリティ脆弱性の修正を始める前に、まず開発環境を準備し、脆弱性を含むサンプルアプリケーションのソースコードを入手する必要があります。

## 必須 1. 開発環境とリポジトリのセットアップ

PowerShellで一連のセットアップ作業を実行します。

### 1.1 PowerShellでのセットアップ
 - Pythonのインストール確認
 - デモ環境のクローン

1. **PowerShellを起動します**

2. **Python環境の確認**:
   ```powershell
   # Pythonのバージョンを確認
   python --version
   ```
   バージョンが表示されない場合は、Microsoft StoreからPythonをインストールしてください。

3. **作業ディレクトリへ移動**:
   ```powershell
   # お好みの作業用ディレクトリに移動（例：C:\workフォルダー）
   cd C:\work
   # フォルダーが存在しない場合は作成
   New-Item -ItemType Directory -Force -Path C:\work
   ```

4. **リポジトリのクローン**:
   ```powershell
   # GitHubリポジトリをクローン（講師から提供されたURLを使用）
   git clone <リポジトリのURL>
   ```
   
   > **注意**: `<リポジトリのURL>`の部分は、講師から提供される実際のGitHubリポジトリURLに置き換えてください。

5. **クローン結果の確認**:
   ```powershell
   # クローンしたディレクトリに移動（フォルダー名はリポジトリによって異なります）
   cd <クローンしたフォルダー名>
   # ディレクトリ内容を確認
   Get-ChildItem
   ```

## 必須 2. VS Codeでプロジェクトを開く

VS Codeでクローンしたプロジェクトフォルダーを開きます。

### 2.1 プロジェクト構造の確認

VS Codeのエクスプローラーで以下のファイル・フォルダーが存在することを確認してください：
- `demos/` フォルダー
- `demos/sqlinject_python.py` （Python版アプリケーション）

## 必須 3. VS Code内でのブランチ管理

VS Codeの統合ターミナルでブランチ管理を実行します。

1. **VS Code統合ターミナルで以下のコマンドを実行します**:

2. **リモートブランチの確認**:
   ```powershell
   # 全ブランチ（リモート含む）を表示
   git branch -a
   ```

3. **ベースブランチへの切り替え**:
   ```powershell
   # 講師指定のベースブランチにチェックアウト（例：JP-translation）
   git checkout <ベースブランチ名>
   ```

4. **ブランチの最新化**:
   ```powershell
   # リモートから最新の変更を取得
   git pull origin <ベースブランチ名>
   ```

5. **新しい作業ブランチの作成**:
   ```powershell
   # ベースブランチから新しいブランチを作成・チェックアウト
   git checkout -b <作業用ブランチ名>
   ```
   
   > **ブランチ名の例**: `feature/security-fix-handson` など、ハンズオンの内容に合った名前を推奨します。

6. **ブランチ作成の確認**:
   ```powershell
   # 現在のブランチ状態を確認
   git branch
   ```

## 参考 4. GitHub Copilotの確認

GitHub Copilot拡張機能が利用可能であることを確認します。

### 4.1 拡張機能の確認

1. VS Codeの拡張機能タブで「GitHub Copilot」と「GitHub Copilot Chat」がインストール済みであることを確認します
2. インストールされていない場合は、インストールしてください

### 4.2 Copilotのサインイン

1. VS Code下部のステータスバーでCopilotアイコンを確認し、必要に応じてGitHubアカウントでサインインしてください

## トラブルシューティング

### 問題が発生した場合

1. **権限の確認**: リポジトリクローンでエラーが発生する場合、GitHubリポジトリへのアクセス権限を確認してください
2. **パスの確認**: ファイルパスに日本語が含まれる場合、問題が発生することがあります。英語のパスを使用してください
3. **ネットワークの確認**: インストールやクローンでエラーが発生する場合、インターネット接続を確認してください

## まとめと次のステップ

環境の準備が完了しました。次は脆弱性を含むWebアプリケーションを実際に起動し、SQL Injection攻撃を体験してみましょう。

## リソース

- [Python公式サイト](https://www.python.org/)
- [GitHub Copilot拡張機能](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GitHub Copilot Chat拡張機能](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

---

| | [次の手順: 脆弱性アプリケーションのセットアップ →](./1-vulnerable-app-setup.md) |
|:--|--:|