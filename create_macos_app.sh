#!/bin/bash

# 創建 macOS .app 應用包

echo "🍎 創建 macOS .app 應用包..."

# 定義目錄
DIST_DIR="dist"
APP_NAME="LineBackup.app"
APP_DIR="$DIST_DIR/$APP_NAME"
EXECUTABLE="$DIST_DIR/LineBackup"

# 檢查可執行文件是否存在
if [ ! -f "$EXECUTABLE" ]; then
    echo "❌ 錯誤: 找不到 $EXECUTABLE"
    echo "請先運行: python3 build.py"
    exit 1
fi

# 創建應用包結構
echo "📁 創建應用包結構..."

# 刪除舊的應用包
if [ -d "$APP_DIR" ]; then
    rm -rf "$APP_DIR"
fi

# 創建目錄結構
mkdir -p "$APP_DIR/Contents/MacOS"
mkdir -p "$APP_DIR/Contents/Resources"

# 複製可執行文件
cp "$EXECUTABLE" "$APP_DIR/Contents/MacOS/LineBackup"
chmod +x "$APP_DIR/Contents/MacOS/LineBackup"

# 創建 Info.plist
cat > "$APP_DIR/Contents/Info.plist" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>LineBackup</string>
    <key>CFBundleName</key>
    <string>LINE Backup</string>
    <key>CFBundleIdentifier</key>
    <string>com.linebackup.app</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleGetInfoString</key>
    <string>LINE Chat Backup Tool v1.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0.0</string>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSMinimumSystemVersion</key>
    <string>10.14</string>
</dict>
</plist>
EOF

echo "✅ Info.plist 已創建"

# 創建簡單的圖標（可選）
echo "✅ 應用包結構已創建"

# 驗證
echo ""
echo "📊 驗證應用包..."
if [ -d "$APP_DIR" ] && [ -x "$APP_DIR/Contents/MacOS/LineBackup" ]; then
    SIZE=$(du -sh "$APP_DIR" | cut -f1)
    echo "✅ $APP_NAME 已成功創建"
    echo "   位置: $APP_DIR"
    echo "   大小: $SIZE"
    echo ""
    echo "🚀 使用方式:"
    echo "   1. 直接打開: open $APP_DIR"
    echo "   2. 在 Finder 中雙擊 $APP_NAME"
    echo "   3. 或將其拖到應用程式文件夾"
else
    echo "❌ 應用包創建失敗"
    exit 1
fi
