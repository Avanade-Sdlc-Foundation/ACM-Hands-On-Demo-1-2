# SQL Injection デモ - 実行方法の選択肢

## 各種Demo環境起動方法
主な選択肢：
1. **Node.jsインストール** - [nodejs.org](https://nodejs.org/) からLTS版をダウンロード
2. **Python版使用** - [Python_Setup.md](Python_Setup.md) を参照  

### 1?? 最も簡単：Node.jsをインストール
```powershell
# 1. https://nodejs.org/ からLTSバージョンをダウンロード・インストール
# 2. 新しいPowerShellウィンドウで元の手順を実行
cd "【クローンした場所】\ACM-Hands-On-Demo-1-2\demos"
npm install express sqlite3
node sqlinject.js
```

### 2?? 代替案：Python版を使用
詳細は  [Python_Setup.md](Python_Setup.md) を参照 


## トラブルシューティング

### Pythonが見つからない場合
- Microsoft Store から Python をインストール
- または [python.org](https://www.python.org/) からダウンロード

### SQLiteが見つからない場合  
- [SQLite公式サイト](https://www.sqlite.org/download.html) からダウンロード
