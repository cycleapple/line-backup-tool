#!/bin/bash

# LINE 備份工具 - macOS 初始化設置腳本

echo ""
echo "=============================================="
echo "  LINE 聊天記錄備份工具 - macOS 設置"
echo "=============================================="
echo ""

# 獲取腳本目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 1. 檢查 Python
echo "📝 檢查 Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python 3"
    echo ""
    echo "請選擇以下方式安裝："
    echo ""
    echo "方法 1: Homebrew (推薦)"
    echo "  brew install python3"
    echo ""
    echo "方法 2: 官方安裝程序"
    echo "  訪問: https://www.python.org/downloads/"
    echo ""
    read -p "按 Enter 退出..."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "✅ 找到 Python $PYTHON_VERSION"
echo ""

# 2. 賦予執行權限
echo "🔧 設置執行權限..."
chmod +x open_app.command
chmod +x start.sh
chmod +x mac_setup.sh
echo "✅ 完成"
echo ""

# 3. 創建備份文件夾
echo "📁 創建文件夾..."
mkdir -p backups/history
mkdir -p logs
echo "✅ 完成"
echo ""

# 4. 在 Finder 中設置快捷方式（可選）
echo "🎯 設置 Finder 快捷方式?"
echo ""
echo "選擇:"
echo "  1. 是 (推薦)"
echo "  2. 否"
echo ""
read -p "請選擇 (1 或 2): " choice

if [ "$choice" = "1" ]; then
    # 創建桌面快捷方式
    DESKTOP="$HOME/Desktop"
    SHORTCUT="$DESKTOP/LINE 備份工具.command"

    cat > "$SHORTCUT" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/../Documents/LineExport"
python3 main.py
EOF

    chmod +x "$SHORTCUT"
    echo "✅ 已在桌面創建快捷方式"
    echo ""
fi

# 5. 驗證安裝
echo "🧪 驗證安裝..."
if [ -f "main.py" ] && [ -d "backups" ]; then
    echo "✅ 所有文件設置完成！"
    echo ""
    echo "🚀 現在可以:"
    echo ""
    echo "方法 1: 雙擊 open_app.command (最簡單)"
    echo "方法 2: 執行命令 bash start.sh"
    echo "方法 3: 執行命令 python3 main.py"
    echo ""
else
    echo "❌ 設置驗證失敗"
    exit 1
fi

echo "=========================================="
echo "✨ macOS 設置完成！"
echo "=========================================="
echo ""
read -p "按 Enter 繼續..."
