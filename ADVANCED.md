# 進階使用指南

適合有一定技術基礎的使用者。

## 命令行參數

```bash
python main.py [OPTIONS]
```

### 可用選項

```
--quiet, -q          靜默模式，無提示信息
--backup <room>      直接備份指定聊天室
--export <format>    導出格式 (json, html, csv, excel)
--compress, -c       壓縮備份文件
--encrypt, -e        加密備份文件
--output <path>, -o  指定輸出路徑
--config <file>      使用自訂配置文件
--debug              顯示除錯信息
```

### 使用範例

```bash
# 直接備份指定聊天室
python main.py --backup "我的群組"

# 備份並壓縮為 CSV
python main.py --backup "chat" --export csv --compress

# 使用自訂配置
python main.py --config custom_config.json
```

## 配置文件 (config.json)

### 進階設置

```json
{
  "version": "1.0.0",
  "backup_location": "./backups",
  "auto_backup": true,
  "backup_interval": 24,
  "compression": true,
  "encryption": true,
  "encryption_password": "your_password",
  "retention_days": 365,
  "max_backup_size_mb": 1000,
  "language": "zh_TW",
  "theme": "dark",
  "notifications": true,
  "export_formats": ["json", "html"],
  "backup_metadata": true,
  "include_media": false,
  "max_message_length": 10000
}
```

## 自動備份

### 設置定時備份

1. 打開 `config.json`
2. 設置:
```json
{
  "auto_backup": true,
  "backup_interval": 24
}
```
3. 保存並重啟程序

### Windows 排程工作

使用 Windows 工作排程器:

1. 按 Win + R，輸入 `taskschd.msc`
2. 建立基本工作
3. 名稱: "LINE 自動備份"
4. 觸發條件: 每天特定時間
5. 操作: 啟動程式 `start.bat`

### macOS / Linux Cron 工作

編輯 crontab:
```bash
crontab -e
```

添加:
```bash
# 每天凌晨 2 點備份
0 2 * * * cd /path/to/LineExport && python3 main.py --backup "聊天室名稱" --quiet
```

## 備份加密

### 啟用加密

編輯 `config.json`:
```json
{
  "encryption": true,
  "encryption_password": "your_secure_password"
}
```

### 手動加密備份

```bash
python main.py --backup "chat" --encrypt
```

## 導出格式

### JSON 導出

最詳細的格式，包含所有元數據:

```bash
python main.py --backup "chat" --export json
```

### HTML 導出

美化的網頁格式，可在瀏覽器查看:

```bash
python main.py --backup "chat" --export html
```

### CSV 導出 (開發中)

適合 Excel/Google Sheets:

```bash
python main.py --backup "chat" --export csv
```

### Excel 導出 (開發中)

帶格式的 Excel 文件:

```bash
python main.py --backup "chat" --export excel
```

## 批量備份

### 批量備份多個聊天室

創建 `batch_backup.py`:

```python
import subprocess
import json

# 讀取聊天室列表
rooms = [
    "聊天室1",
    "聊天室2",
    "聊天室3"
]

# 逐個備份
for room in rooms:
    print(f"正在備份: {room}")
    subprocess.run([
        "python", "main.py",
        "--backup", room,
        "--quiet"
    ])
    print(f"✅ {room} 備份完成")
```

運行:
```bash
python batch_backup.py
```

## 備份恢復

### 從 HTML 備份查看聊天記錄

直接在瀏覽器打開 HTML 文件:
```bash
open backups/chat_20261005_120000.html
```

### 從 JSON 備份提取數據

```python
import json

with open('backups/chat_20261005_120000.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 列出所有消息
for msg in data['messages']:
    print(f"{msg['time']} | {msg['sender']}: {msg['message']}")
```

## 備份管理

### 查看備份大小

```bash
# Linux/macOS
du -sh backups/

# Windows PowerShell
Get-ChildItem -Path .\backups -Recurse | Measure-Object -Property Length -Sum
```

### 自動清理舊備份

編輯 `config.json`:
```json
{
  "retention_days": 365
}
```

30 天後，舊備份會自動刪除

### 手動刪除備份

```bash
# 刪除指定備份
rm backups/chat_20261005_120000.json

# 刪除所有超過 30 天的備份
find backups -mtime +30 -delete
```

## 效能優化

### 只備份最近的消息

編輯 `config.json`:
```json
{
  "message_limit": 10000
}
```

### 不包含媒體文件

```json
{
  "include_media": false
}
```

### 啟用壓縮

```bash
python main.py --backup "chat" --compress
```

## 故障排除

### 檢查日誌

```bash
# 顯示最後 50 行日誌
tail -n 50 logs/backup.log

# Windows
type logs\backup.log | more
```

### 啟用除錯模式

```bash
python main.py --debug
```

### 驗證備份完整性

```python
import json
import hashlib

# 檢查 JSON 格式
with open('backups/chat.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"消息數: {len(data['messages'])}")
    print(f"最後備份: {data['backup_time']}")

# 驗證文件完整性
with open('backups/chat.json', 'rb') as f:
    md5 = hashlib.md5(f.read()).hexdigest()
    print(f"MD5: {md5}")
```

## 自訂指令碼

### 備份後發送通知

創建 `post_backup.py`:

```python
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "your_email@gmail.com"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

send_email("備份完成", "LINE 聊天記錄備份已完成")
```

### 備份後上傳雲端

使用 AWS S3、Google Drive 或其他雲端服務:

```python
import boto3

def upload_to_s3(file_path, bucket, key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, key)
    print(f"✅ 已上傳到 S3: {key}")

# 使用
upload_to_s3('backups/chat.json', 'my-bucket', 'line-backups/chat.json')
```

---

**提示:** 進階功能需要一定的技術知識。如有問題，參考主 README 或檢查日誌文件。
