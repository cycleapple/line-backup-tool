# macOS 使用指南

針對 macOS 用戶的完整設置和使用說明。

## 🚀 最快開始 (1 分鐘)

### 方式 1: 雙擊 open_app.command (推薦) ⭐

1. 在 Finder 中找到 `open_app.command`
2. **雙擊**它
3. 輸入聊天室名稱
4. 完成！

### 方式 2: 使用終端

1. 打開**終端**（Applications → Utilities → Terminal）
2. 執行命令：
   ```bash
   bash start.sh
   ```

## 📖 初次安裝

### 第一次使用的完整設置

1. **打開終端**
   ```
   Command + Space → 輸入 Terminal → 按 Enter
   ```

2. **進入程序目錄**
   ```bash
   cd ~/Documents/LineExport
   ```

3. **執行設置腳本**（可選，會自動設置）
   ```bash
   bash mac_setup.sh
   ```

4. **完成！** 現在可以雙擊 `open_app.command` 了

## 🔍 檢查 Python 安裝

### 1. 檢查是否已安裝 Python 3

打開終端，執行：
```bash
python3 --version
```

**如果看到版本號**（如 `Python 3.11.0`）→ ✅ 已安裝，可以開始使用

**如果看到錯誤** → 需要安裝 Python

### 2. 安裝 Python

#### 方式 A: Homebrew (最簡單) ⭐

1. 先安裝 Homebrew（如果還沒有）：
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. 安裝 Python 3：
   ```bash
   brew install python3
   ```

3. 驗證：
   ```bash
   python3 --version
   ```

#### 方式 B: 官方安裝程序

1. 訪問 https://www.python.org/downloads/
2. 下載 **macOS installer** (64-bit)
3. 雙擊安裝程序
4. 按照提示完成安裝

#### 方式 C: 使用 MacPorts

```bash
sudo port install python311
```

## 📱 macOS 特定功能

### 在 Spotlight 中快速搜索

1. 將 `open_app.command` 放在 `~/Documents/LineExport/`
2. 使用 **Command + Space** 搜索 "LINE" 或 "備份"
3. 結果會直接顯示

### 在 Finder 工具欄添加快捷方式

1. 打開 Finder，進入 LineExport 文件夾
2. 將 `open_app.command` **拖曳到** Finder 工具欄
3. 之後可直接點擊工具欄按鈕

### 設置在登錄時自動備份

1. **System Preferences → General → Login Items**
2. 點擊 **+** 按鈕
3. 選擇 LineExport 文件夾中的 `open_app.command`
4. 確認

> 注意：會在每次啟動時自動運行備份

## ⚠️ 常見 macOS 問題

### Q: 雙擊 open_app.command 沒有反應？

**解決方案 1: 授予執行權限**
```bash
chmod +x ~/Documents/LineExport/open_app.command
```

**解決方案 2: 用右鍵打開**
1. 右鍵點擊 `open_app.command`
2. 選擇 "Open With" → "Terminal"

### Q: 提示 "無法驗證開發者"？

這是 macOS 安全提示。

**解決方案:**
1. 右鍵點擊 `open_app.command`
2. 選擇 "Open"（而不是雙擊）
3. 點擊"打開"確認

### Q: 終端顯示 "command not found: python3"？

**解決方案:**

檢查 Python 位置：
```bash
which python3
```

如果沒有結果，執行安裝：
```bash
brew install python3
```

### Q: 備份後終端窗口不關閉？

**解決方案:**

編輯 `open_app.command`，取消註釋最後一行：
```bash
exit
```

### Q: 無法訪問 backups 文件夾？

**解決方案:**

確保有文件夾權限：
```bash
chmod -R 755 ~/Documents/LineExport/backups
```

### Q: 提示 "操作不被允許"？

**解決方案:**

檢查文件權限：
```bash
ls -la ~/Documents/LineExport/
```

重設權限：
```bash
chmod -R u+w ~/Documents/LineExport/
```

## 🎯 推薦用法

### 日常使用

**最簡單的方式：**
1. 雙擊 `open_app.command`
2. 輸入聊天室名稱
3. 等待完成

### 定期備份

**選項 1: 手動備份**
- 每週雙擊 `open_app.command` 一次

**選項 2: 自動備份**
1. 打開終端
2. 編輯 crontab：
   ```bash
   crontab -e
   ```
3. 添加（每天凌晨2點備份）：
   ```bash
   0 2 * * * cd ~/Documents/LineExport && python3 main.py --quiet
   ```

### 快速訪問備份文件

**在程序菜單中:**
- 選擇 `5` (打開備份文件夾)
- 會直接在 Finder 中打開

**或者手動打開:**
```bash
open ~/Documents/LineExport/backups
```

## 🔒 安全建議

### 1. 限制文件夾訪問

```bash
# 只有當前用戶可訪問
chmod 700 ~/Documents/LineExport/backups
```

### 2. 定期備份備份文件

```bash
# 複製到外接硬碟
cp -r ~/Documents/LineExport/backups /Volumes/YourDrive/
```

### 3. 加密備份文件

編輯 `config.json`：
```json
{
  "encryption": true,
  "encryption_password": "your_password"
}
```

## 🧹 清理和維護

### 查看備份文件大小

```bash
du -sh ~/Documents/LineExport/backups
```

### 刪除舊備份（超過 30 天）

```bash
find ~/Documents/LineExport/backups -mtime +30 -delete
```

### 查看最近的備份

```bash
ls -lt ~/Documents/LineExport/backups/*.json | head -5
```

## 📚 文檔位置

所有文檔都在 `~/Documents/LineExport/` 中：

- **START_HERE.md** - 新手入門
- **QUICKSTART.md** - 5分鐘速成
- **README.md** - 完整功能
- **INSTALL.md** - 安裝詳解
- **ADVANCED.md** - 進階用法
- **FAQ.md** - 常見問題

## 🔄 更新程序

### 檢查更新

訪問 GitHub 查看最新版本（待補充）

### 安全更新

1. 備份現有文件：
   ```bash
   cp -r ~/Documents/LineExport ~/Documents/LineExport_backup
   ```

2. 下載新版本

3. 覆蓋舊文件（保留 `backups/` 和 `logs/` 文件夾）

## 🆘 故障排除

### 查看詳細日誌

```bash
# 查看最後 50 行日誌
tail -50 ~/Documents/LineExport/logs/backup.log

# 實時查看日誌
tail -f ~/Documents/LineExport/logs/backup.log
```

### 運行除錯模式

```bash
cd ~/Documents/LineExport
python3 main.py --debug
```

### 重置配置

```bash
# 備份現有配置
cp config.json config.json.bak

# 重置為默認配置
rm config.json
python3 main.py
```

## 💡 macOS 專業提示

### 1. 使用 Automator 創建應用

1. 打開 Automator (Applications → Automator)
2. 新建 → 選擇 "Application"
3. 搜索並添加 "Run Shell Script"
4. 輸入：
   ```bash
   cd ~/Documents/LineExport
   python3 main.py
   ```
5. 儲存為 "LINE Backup.app"

### 2. 設置快捷鍵

使用 Alfred 或 Raycast 設置快捷鍵快速啟動

### 3. 與 iCloud 同步備份

```bash
# 將備份軟連結到 iCloud Drive
ln -s ~/Documents/LineExport/backups ~/Library/Mobile\ Documents/com\~apple\~CloudDocs/LineExport_Backups
```

### 4. 使用 Time Machine 備份備份文件

1. System Preferences → Time Machine
2. 選擇備份磁碟
3. 確保 `~/Documents/LineExport/` 被包含

## 🎓 進階主題

### 使用 zsh 別名快速啟動

編輯 `~/.zshrc`：
```bash
alias linebackup='cd ~/Documents/LineExport && python3 main.py'
```

重啟終端，然後直接執行 `linebackup`

### 集成到工作流程

使用 Shortcuts App（macOS 12+）創建快捷方式

### 批量備份多個聊天室

編輯 `config.json`：
```json
{
  "backup_rooms": [
    "聊天室1",
    "聊天室2",
    "聊天室3"
  ],
  "auto_backup": true
}
```

---

## 📞 需要幫助？

1. 查看本文檔（你現在所在）
2. 查看 **FAQ.md** 常見問題
3. 檢查 `logs/backup.log` 日誌文件
4. 在終端執行：`python3 main.py --debug`

---

**版本:** 1.0.0
**最後更新:** 2026-10-05
**針對:** macOS 10.14+
