#!/bin/bash

# LINE 備份工具 - 朋友版本一鍵安裝

clear

echo "=================================================="
echo ""
echo "   LINE 聊天記錄備份工具"
echo "   朋友版本 - 超簡單安裝"
echo ""
echo "=================================================="
echo ""

# 獲取腳本目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "📝 正在檢查系統..."
echo ""

# 1. 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安裝"
    echo ""
    echo "需要安裝 Python 3。選擇以下方式之一："
    echo ""
    echo "1️⃣  使用 Homebrew（推薦）"
    echo "   brew install python3"
    echo ""
    echo "2️⃣  從官方網站下載"
    echo "   https://www.python.org/downloads/"
    echo ""
    read -p "按 Enter 退出..."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "✅ 找到 Python $PYTHON_VERSION"
echo ""

# 2. 檢查可執行文件
echo "📦 檢查應用程序..."

if [ -d "$SCRIPT_DIR/dist/LineBackup.app" ]; then
    echo "✅ 應用程序已準備好"
    APP_PATH="$SCRIPT_DIR/dist/LineBackup.app"
else
    echo "⚠️  應用程序未找到"
    echo "   嘗試運行主程序..."
    APP_PATH="python3"
fi

echo ""

# 3. 固化啟動腳本
echo "⚙️  設置啟動快捷方式..."

# 修復簡單啟動腳本
if [ -f "$SCRIPT_DIR/簡單啟動.command" ]; then
    chmod +x "$SCRIPT_DIR/簡單啟動.command"
    echo "✅ 簡單啟動已設置"
fi

# 修復 GUI 啟動腳本
if [ -f "$SCRIPT_DIR/啟動GUI版本.command" ]; then
    chmod +x "$SCRIPT_DIR/啟動GUI版本.command"
    echo "✅ GUI 版本已設置"
fi

echo ""

# 4. 移除隔離標記（如果有的話）
echo "🔐 清除安全標記..."
xattr -rd com.apple.quarantine "$SCRIPT_DIR/dist/LineBackup.app" 2>/dev/null
echo "✅ 完成"

echo ""

# 5. 創建桌面快捷方式（詢問）
echo "🎯 是否在桌面創建快捷方式?"
echo ""
echo "選擇:"
echo "  1) 是 - 推薦（最方便）"
echo "  2) 否"
echo ""
read -p "請選擇 (1 或 2): " choice

if [ "$choice" = "1" ]; then
    DESKTOP="$HOME/Desktop"
    SHORTCUT_NAME="LINE備份 - 快速啟動.command"
    SHORTCUT_PATH="$DESKTOP/$SHORTCUT_NAME"

    cat > "$SHORTCUT_PATH" << 'SHORTCUT_EOF'
#!/bin/bash
SCRIPT_DIR="$(dirname "$(cd "$(dirname "$0")" && pwd)")/Documents/LineExport"
open "$SCRIPT_DIR/dist/LineBackup.app"
SHORTCUT_EOF

    chmod +x "$SHORTCUT_PATH"
    echo ""
    echo "✅ 已在桌面創建快捷方式"
    echo "   名稱: $SHORTCUT_NAME"
    echo ""
fi

echo ""
echo "=================================================="
echo ""
echo "  🎉 安裝完成！"
echo ""
echo "=================================================="
echo ""

# 6. 展示使用說明
echo "📖 現在可以使用以下方式啟動:"
echo ""
echo "方式 1: 最簡單 ⭐⭐⭐"
echo "  • Finder 進入 Documents/LineExport"
echo "  • 雙擊「簡單啟動.command」"
echo ""
echo "方式 2: 圖形界面"
echo "  • 雙擊「啟動GUI版本.command」"
echo "  • 點擊按鈕完成備份"
echo ""
echo "方式 3: 應用包"
echo "  • 進入 dist 文件夾"
echo "  • 雙擊「LineBackup.app」"
echo ""
echo "方式 4: 桌面快捷方式"
echo "  • 如果選擇了，直接雙擊桌面的快捷方式"
echo ""

# 7. 顯示幫助文件
echo "📚 查看使用說明:"
echo "  • 給朋友的使用說明.md - 超簡單說明"
echo "  • START_HERE.md - 快速開始"
echo "  • README_MAC.md - Mac 詳細指南"
echo ""

echo "🚀 立即開始:"
echo ""
read -p "按 Enter 打開應用程序..."

# 打開應用
if [ -d "$SCRIPT_DIR/dist/LineBackup.app" ]; then
    open "$SCRIPT_DIR/dist/LineBackup.app"
else
    cd "$SCRIPT_DIR"
    python3 main.py
fi

echo ""
echo "✨ 祝你使用愉快！"
echo ""
