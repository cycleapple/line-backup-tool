# Build 構建指南

本文檔說明如何將 LINE 備份工具構建成可執行文件（不需要用戶安裝 Python）。

## 📦 構建產物

構建完成後生成以下文件：

### macOS
- **LineBackup.app** - 完整的 macOS 應用程序包
  - 可直接雙擊打開
  - 可拖到應用程式文件夾安裝
  - 大小: ~3.4 MB

### Windows
- **LineBackup.exe** - Windows 可執行文件
  - 可直接運行
  - 無需安裝 Python
  - 大小: ~4 MB

### Linux
- **LineBackup** - Linux 可執行文件
  - 可直接運行
  - 無需安裝 Python
  - 大小: ~3.5 MB

## 🚀 快速構建 (macOS)

### 第一步: 安裝構建工具

```bash
# 進入項目目錄
cd ~/Documents/LineExport

# 安裝 PyInstaller
python3 -m pip install PyInstaller
```

### 第二步: 執行構建

```bash
# 方式 1: 運行 Python 構建腳本
python3 build.py

# 方式 2: 手動執行 PyInstaller
python3 -m PyInstaller \
  --name=LineBackup \
  --onefile \
  --add-data=config.json:. \
  main.py

# 方式 3: 創建 macOS 應用包
bash create_macos_app.sh
```

### 第三步: 驗證構建結果

```bash
# 查看生成的文件
ls -lh dist/

# 測試應用程序
open dist/LineBackup.app
```

## 📋 完整構建步驟

### 1. 環境準備

```bash
# 確保 Python 3.8+ 已安裝
python3 --version

# 升級 pip
python3 -m pip install --upgrade pip

# 安裝 PyInstaller
python3 -m pip install PyInstaller
```

### 2. 清理舊構建

```bash
# 刪除舊的構建文件
rm -rf build/ dist/ *.spec

# 或使用 Python 腳本
python3 build.py  # 會自動清理
```

### 3. 執行構建

```bash
# macOS
python3 build.py
bash create_macos_app.sh

# 或直接使用 PyInstaller
python3 -m PyInstaller --name=LineBackup --onefile --add-data=config.json:. main.py
```

### 4. 構建結果

構建完成後，文件位置：

```
dist/
├── LineBackup          # macOS/Linux 可執行文件
├── LineBackup.app/     # macOS 應用包 ⭐
│   └── Contents/
│       ├── MacOS/
│       │   └── LineBackup
│       ├── Resources/
│       └── Info.plist
└── LineBackup.exe      # Windows 可執行文件（如果在 Windows 上構建）
```

### 5. 分發和安裝

#### macOS
```bash
# 方式 1: 直接打開
open dist/LineBackup.app

# 方式 2: 複製到應用程式文件夾
cp -r dist/LineBackup.app /Applications/

# 方式 3: 創建 DMG 安裝程序
hdiutil create -volname "LINE Backup" \
  -srcfolder dist/LineBackup.app \
  -ov -format UDZO \
  line-backup-1.0.0.dmg
```

#### Windows
```bash
# 直接運行
dist\LineBackup.exe
```

#### Linux
```bash
# 添加執行權限
chmod +x dist/LineBackup

# 執行
./dist/LineBackup
```

## 🔧 PyInstaller 選項說明

```bash
python3 -m PyInstaller [OPTIONS] script.py
```

### 常用選項

| 選項 | 說明 |
|-----|------|
| `--onefile` | 打包成單個可執行文件 |
| `--onedir` | 打包成目錄（包含依賴） |
| `--windowed` | 隱藏控制台窗口（GUI 應用） |
| `--icon=file.ico` | 設置應用圖標 |
| `--name=NAME` | 設置輸出名稱 |
| `--add-data=SRC:DEST` | 添加數據文件 |
| `--hidden-import=MOD` | 包含隱藏的模塊 |
| `--clean` | 清理 PyInstaller 緩存 |

### 我們的完整命令

```bash
python3 -m PyInstaller \
  --name=LineBackup \          # 應用名稱
  --onefile \                   # 單個文件
  --add-data=config.json:. \    # 包含配置文件
  --hidden-import=json \        # 包含必要模塊
  --hidden-import=datetime \
  --hidden-import=pathlib \
  --clean \                     # 清理緩存
  main.py                       # 源文件
```

## 📊 構建結果示例

### macOS

```
✅ 構建完成！
📁 輸出目錄: /Users/mingtu/Documents/LineExport/dist
平臺: Darwin

生成的文件:
  - LineBackup (3.39 MB) - 可執行文件
  - LineBackup.app (3.4 MB) - 應用包

🚀 使用方式:
  1. 直接打開: open dist/LineBackup.app
  2. 在 Finder 中雙擊 LineBackup.app
  3. 或將其拖到應用程式文件夾
```

## 🐛 常見問題

### Q: 構建失敗，提示找不到模塊？

**解決方案:**
```bash
# 添加 --hidden-import 參數
python3 -m PyInstaller \
  --name=LineBackup \
  --onefile \
  --hidden-import=MODULE_NAME \
  main.py
```

### Q: 構建的文件太大？

**解決方案:**
- 使用 `--onedir` 代替 `--onefile`（更快）
- 移除不必要的依賴
- 使用 UPX 壓縮（Windows）

### Q: macOS 說"無法驗證開發者"？

**解決方案:**
```bash
# 移除代碼簽名限制
xattr -d com.apple.quarantine dist/LineBackup.app

# 或在 System Preferences 中允許
```

### Q: 能否在 macOS 上構建 Windows 版本？

**不能**。需要在相應的平臺上構建：
- Windows 版本 → 在 Windows 上構建
- macOS 版本 → 在 macOS 上構建
- Linux 版本 → 在 Linux 上構建

## 🚀 CI/CD 自動構建

### GitHub Actions 工作流程

創建 `.github/workflows/build.yml`:

```yaml
name: Build

on:
  push:
    tags:
      - 'v*'

jobs:
  build-macos:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyInstaller
      - name: Build
        run: python build.py
      - name: Create macOS app
        run: bash create_macos_app.sh
      - name: Upload artifact
        uses: actions/upload-artifact@v2
        with:
          name: LineBackup-macOS
          path: dist/LineBackup.app

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyInstaller
      - name: Build
        run: python build.py
      - name: Upload artifact
        uses: actions/upload-artifact@v2
        with:
          name: LineBackup-Windows
          path: dist/LineBackup.exe

  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyInstaller
      - name: Build
        run: python build.py
      - name: Upload artifact
        uses: actions/upload-artifact@v2
        with:
          name: LineBackup-Linux
          path: dist/LineBackup
```

## 📦 分發方式

### 方式 1: 直接分享可執行文件

```bash
# macOS
dist/LineBackup.app

# Windows
dist/LineBackup.exe

# Linux
dist/LineBackup
```

### 方式 2: 創建 Release

```bash
gh release upload v1.0.0 \
  dist/LineBackup.app \
  dist/LineBackup.exe \
  dist/LineBackup
```

### 方式 3: 創建安裝程序

#### macOS DMG
```bash
hdiutil create -volname "LINE Backup" \
  -srcfolder dist/LineBackup.app \
  -ov -format UDZO \
  line-backup-1.0.0.dmg
```

#### Windows MSI/NSIS
使用工具如 NSIS 或 Inno Setup

#### Linux AppImage
使用 appimagetool

## ⚙️ 優化構建

### 減少文件大小

```bash
# 使用 UPX 壓縮（Windows）
pyinstaller ... --upx-dir=/path/to/upx

# 移除不需要的文件
strip dist/LineBackup  # Linux/macOS
```

### 加快構建速度

```bash
# 使用 --onedir 而非 --onefile
python3 -m PyInstaller --onedir --name=LineBackup main.py

# 使用快速構建模式
python3 -m PyInstaller --distpath=./dist --buildpath=./build main.py
```

## 📝 版本管理

### 更新版本號

1. 編輯 `main.py` 中的版本
2. 編輯 `config.json` 中的版本
3. 更新 `CHANGELOG.md`
4. 重新構建

```bash
# 例如: v1.0.0 → v1.1.0
sed -i 's/"version": "1.0.0"/"version": "1.1.0"/' config.json
python3 build.py
```

## 🔗 資源

- [PyInstaller 官方文檔](https://pyinstaller.org/)
- [PyInstaller 選項](https://pyinstaller.readthedocs.io/en/stable/usage.html)
- [GitHub Actions 文檔](https://docs.github.com/en/actions)

---

**版本**: 1.0.0
**最後更新**: 2026-10-05
