# ?? SQL Injection脆弱性修正ガイド

このガイドでは、SQL Injection脆弱性を発見した後に、GitHub Copilotを使用してコードを安全に修正する手順を説明します。

## 前提条件
- SQL Injection脆弱性デモを実行済み
- 攻撃が成功することを確認済み（`' OR 1=1 --`で全データが表示される）

## 1.脆弱なコードの特定

### JavaScript版（sqlinject.js）
```javascript
let query = `SELECT * FROM products WHERE name LIKE '%${productName}%'`;
```

### Python版（sqlinject_python.py）
```python
query = f"SELECT * FROM products WHERE name LIKE '%{product_name}%'"
```

**問題点**: ユーザー入力が直接SQLクエリに埋め込まれている

## 2.GitHub Copilot Chatで修正依頼

### 2-1. 脆弱なコード行を選択
- 上記の脆弱なクエリ行をマウスで選択

### 2-2. Copilot Chatを起動
- **Ctrl + I** を押してCopilot Chatを開く

### 2-3. 修正プロンプトを入力
```
このSQL Injectionの脆弱性を修正してください。
プリペアードステートメントを使用し、安全なクエリに書き換えてください。
```

## 3.修正内容の確認

### JavaScript版（修正後）
```javascript
// プリペアードステートメント使用
const query = `SELECT * FROM products WHERE name LIKE ?`;
db.all(query, [`%${productName}%`], (err, rows) => {
  if (err) {
    res.status(500).json({ error: err.message });
    return;
  }
  res.json({ products: rows });
});
```

### Python版（修正後）
```python
# パラメータ化クエリ使用
query = "SELECT * FROM products WHERE name LIKE ?"
cursor.execute(query, (f'%{product_name}%',))
```
## extra 追加の指示
```
入力値検証とサニタイズ機能も追加してください。
特殊文字をエスケープする処理を含めてください。
```

### 追加のセキュリティ強化例
```python
import re

# 入力値検証
def validate_input(input_str):
    # 基本的な文字のみ許可
    if re.match("^[a-zA-Z0-9\s]+$", input_str):
        return input_str
    else:
        raise ValueError("無効な文字が含まれています")

# 使用例
try:
    validated_name = validate_input(product_name)
    query = "SELECT * FROM products WHERE name LIKE ?"
    cursor.execute(query, (f'%{validated_name}%',))
except ValueError as e:
    return jsonify({'error': str(e)}), 400
```

## 4.修正版の動作確認

### 4-1. 修正されたコードを保存・実行
**?? [SetUp_Exercise.md](SetUp_Exercise.md) - アプリの立ち上げを参照**

### 4-2. 攻撃テストを再実行
```
http://localhost:8080/search?name=' OR 1=1 --
```

### 4-3. 期待される結果
- **修正前**: すべての製品（41件）が表示されること
- **修正後**: 検索結果なし、またはエラーメッセージこと

### 4-4. 正常な検索の確認
```
http://localhost:8080/search?name=Apple
```
- Appleを含む製品のみが表示されること

## ポイント

### プリペアードステートメントの重要性
- SQLクエリとデータを分離
- データベースエンジンがクエリ構造を事前に解析
- 悪意のあるSQL文の挿入を防止

### 多層防御アプローチ
1. **プリペアードステートメント** - 基本的な防御
2. **入力値検証** - 不正なデータの事前チェック  
3. **エスケープ処理** - 特殊文字の無害化
4. **最小権限の原則** - データベースアクセス権限の制限

## 追加演習

### レベル1: 基本修正
- プリペアードステートメントの実装

### レベル2: 強化版
- 入力値検証の追加
- エラーハンドリングの改善

### レベル3: 上級者向け
- ログ機能の実装
- レート制限の追加
- CSRFプロテクションの実装

## ? 重要な注意事項

- **本番環境では**: 必ずプリペアードステートメントを使用
- **開発段階で**: 静的解析ツール（SonarQube等）を活用  
- **継続的に**: セキュリティテストを実行
- **定期的に**: 依存関係のセキュリティ更新を確認
