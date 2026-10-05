# 🚀 從這裡開始

歡迎使用 **LINE 聊天記錄備份工具**！

> 本文檔會在 30 秒內讓你上手

## ⚡ 最快開始 (30 秒)

### Windows 用戶
1. **雙擊** `start.bat`
2. 輸入聊天室名稱
3. ✅ 完成！

### macOS / Linux 用戶
1. **打開終端**，進入程序文件夾
2. 執行: `bash start.sh`
3. 輸入聊天室名稱
4. ✅ 完成！

---

## 📚 文檔導航

根據你的需求，選擇對應的文檔：

| 你想... | 閱讀... | 花費時間 |
|--------|--------|--------|
| 馬上開始用 | **QUICKSTART.md** | 5 分鐘 |
| 安裝和設置 | **INSTALL.md** | 10 分鐘 |
| 了解所有功能 | **README.md** | 15 分鐘 |
| 自動化和進階 | **ADVANCED.md** | 20 分鐘 |
| 查找答案 | **FAQ.md** | 按需 |
| 版本更新 | **CHANGELOG.md** | 按需 |

---

## ❓ 常見問題速解

### "Python 未安裝"？
👉 去 https://www.python.org/downloads/ 下載安裝

安裝時**必須勾選** ✅ "Add Python to PATH"

### "無法執行 .sh 文件"？
👉 在終端執行:
```bash
chmod +x start.sh
bash start.sh
```

### "備份文件在哪裡"？
👉 在程序菜單選 `5` (打開備份文件夾)

或直接進入 `backups/` 文件夾

### "需要更多幫助"？
👉 查看 **FAQ.md**

---

## 🎯 三步完成備份

```
┌─ 啟動程序 ─┐
│  執行 start │
└──────┬─────┘
       │
┌─ 輸入名稱 ─┐
│  聊天室名  │
└──────┬─────┘
       │
┌─ 等待完成 ┐
│  幾秒鐘... │
└──────┬─────┘
       │
       └──→ ✅ 備份完成！
```

---

## 📁 項目結構一覽

```
📦 LineExport/
 ├── 📄 START_HERE.md          ← 你在這裡
 ├── 📄 README.md              ← 完整說明
 ├── 📄 QUICKSTART.md          ← 快速開始
 ├── 📄 INSTALL.md             ← 安裝指南
 ├── 📄 ADVANCED.md            ← 進階功能
 ├── 📄 FAQ.md                 ← 常見問題
 ├── 📄 LICENSE                ← 開源許可
 ├── 🐍 main.py                ← 主程序
 ├── ⚙️  config.json            ← 配置文件
 ├── 🪟 start.bat              ← Windows 啟動
 ├── 🐧 start.sh               ← Linux/Mac 啟動
 ├── 📦 requirements.txt        ← 依賴列表
 ├── 📁 backups/               ← 備份文件夾
 │   └── 📁 history/           ← 備份歷史
 └── 📁 logs/                  ← 日誌文件夾
```

---

## 🎓 學習路徑

### 初學者 👶
1. 讀 **START_HERE.md** (你現在所在)
2. 讀 **QUICKSTART.md** (5 分鐘)
3. 試著備份一個聊天室
4. 查看 **README.md** 了解更多功能

### 進階用戶 🚀
1. 讀 **ADVANCED.md**
2. 設置自動備份
3. 探索命令行參數
4. 自訂備份腳本

### 尋求幫助 🆘
1. 查看 **FAQ.md**
2. 檢查 `logs/backup.log` 文件
3. 讀相關文檔

---

## 💡 使用建議

✅ **推薦**
- 定期備份（每週）
- 多地備份重要記錄（本機、外接硬碟、雲端）
- 檢查 `logs/backup.log` 確保備份成功
- 設置自動備份（詳見 ADVANCED.md）

❌ **不推薦**
- 備份後刪除 `backups/` 文件夾
- 在公共電腦上不加密備份
- 依賴單一備份副本
- 忽略錯誤日誌

---

## 🔐 安全提示

⚠️ **重要事項**

1. **隱私**: 所有備份 100% 保存在本地，不上傳任何數據
2. **加密**: 可編輯 `config.json` 啟用加密保護
3. **訪問控制**: 限制他人訪問 `backups/` 文件夾
4. **備份策略**: 3-2-1 備份法則
   - 3 份副本
   - 2 種儲存媒介
   - 1 份異地備份

---

## 🚀 下一步

### 立即開始
👉 執行 `start.bat` (Windows) 或 `bash start.sh` (Mac/Linux)

### 詳細了解
👉 打開 `QUICKSTART.md` 或 `README.md`

### 遇到問題
👉 查看 `FAQ.md` 或 `logs/backup.log`

---

## ℹ️ 版本信息

- **版本**: 1.0.0
- **日期**: 2026-10-05
- **狀態**: ✅ 穩定版
- **Python**: 3.8+
- **平臺**: Windows, macOS, Linux

---

## 📞 支持

- 📖 文檔: 本文件夾中的 .md 文件
- 🐛 報告 Bug: GitHub Issues (待補充)
- 💬 功能建議: GitHub Discussions (待補充)
- 📝 日誌: `logs/backup.log`

---

## 👋 开始吧！

```
現在就準備好了！
雙擊 start.bat (Windows) 或執行 bash start.sh (Mac/Linux)
享受安心的備份體驗！
```

---

**祝你使用愉快！** 💚

*如有任何問題，所有答案都在文檔裡。*
