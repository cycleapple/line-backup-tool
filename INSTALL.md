# LINE 備份工具 - 安裝指南

一步步教你安裝和使用 LINE 備份工具。

## 前置準備

### Windows 用戶

1. **下載 Python**
   - 訪問 https://www.python.org/downloads/
   - 點擊下載 Python 3.8 或更新版本
   - 選擇 **Windows installer** (64-bit 推薦)

2. **安裝 Python**
   - 執行下載的安裝程序
   - ⚠️ **重要**: 勾選 "Add Python to PATH"
   - 點擊 "Install Now"
   - 等待安裝完成

3. **驗證安裝**
   - 按 Win + R，輸入 `cmd`
   - 執行：`python --version`
   - 應該看到版本號 (如 Python 3.10.0)

### macOS 用戶

1. **檢查 Python**
   ```bash
   python3 --version
   ```
   如果已安裝 Python 3.8+，可以跳過下一步。

2. **如需安裝 Python**
   - 方式 1: 使用 Homebrew
     ```bash
     brew install python3
     ```
   - 方式 2: 訪問 https://www.python.org/downloads/ 下載安裝

### Linux 用戶

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

## 安裝步驟

### 方式 1: 快速啟動 (推薦)

**Windows:**
1. 在文件夾中找到 `start.bat`
2. 雙擊執行
3. 等待程序啟動

**macOS/Linux:**
1. 打開終端
2. 進入程序目錄：
   ```bash
   cd /path/to/LineExport
   ```
3. 執行：
   ```bash
   bash start.sh
   ```
   或雙擊 `start.sh` (需要賦予執行權限)

### 方式 2: 命令行運行

```bash
# 進入程序目錄
cd LineExport

# 運行程序
python3 main.py
```

### 方式 3: 設置為快捷方式 (Windows)

1. 在 `start.bat` 上右鍵
2. 選擇"發送到" → "桌面（快捷方式）"
3. 之後可在桌面雙擊快捷方式運行

## 首次使用

1. 啟動程序後會看到菜單
2. 選擇 `1. 開始新備份`
3. 輸入 LINE 聊天室名稱
4. 程序自動備份並保存文件

## 備份文件位置

所有備份保存在 `backups/` 文件夾中:

```
LineExport/
├── backups/
│   ├── chat_name_20261005_100000.json
│   ├── chat_name_20261005_100000.html
│   └── history/
├── logs/
│   └── backup.log
├── main.py
├── config.json
└── README.md
```

## 常見問題

### ❌ "Python is not installed"

**解決方法:**
1. 確認已安裝 Python 3.8+
2. 重新安裝 Python，確保勾選 "Add Python to PATH"
3. 重啟電腦後重試

### ❌ 無法執行 .bat 文件

**解決方法:**
1. 用記事本打開 `start.bat`
2. 複製所有內容
3. 另存為 `start.bat` (注意副檔名)
4. 雙擊執行

### ❌ 無法執行 .sh 文件 (macOS/Linux)

**解決方法:**
```bash
# 賦予執行權限
chmod +x start.sh

# 然後運行
./start.sh
```

### ❌ 報告 "模塊未找到" 錯誤

**解決方法:**
```bash
# 安裝必要的模塊
pip install -r requirements.txt
```

## 升級

只需下載最新版本文件，覆蓋舊文件即可。備份文件不會被刪除。

## 卸載

1. 直接刪除 `LineExport` 文件夾
2. 備份文件位於 `backups/` 文件夾，建議先備份重要文件

## 技術支持

遇到問題？

1. 查看 `logs/backup.log` 文件中的錯誤信息
2. 檢查 Python 版本: `python --version`
3. 嘗試重新安裝程序

## 安全提示

⚠️ **重要:**
- 備份文件包含私密聊天記錄，請妥善保管
- 定期備份，建議每週至少一次
- 不要刪除 `backups/` 文件夾，除非確認不需要

---

**需要幫助?** 檢查 README.md 了解更多信息
