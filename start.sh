#!/bin/bash

# LINE 備份工具 - macOS/Linux 啟動腳本

# 獲取腳本所在目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 進入程序目錄
cd "$SCRIPT_DIR"

# 檢查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python 3"
    echo ""
    echo "請從以下地址下載並安裝 Python 3.8 或更新版本:"
    echo "https://www.python.org/downloads/"
    echo ""
    read -p "按 Enter 退出..."
    exit 1
fi

# 檢查 Python 版本
PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "✅ 找到 Python $PYTHON_VERSION"

# 運行主程序
echo ""
echo "🚀 啟動 LINE 備份工具..."
echo ""

python3 main.py

# 如果運行失敗
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 運行失敗，請檢查錯誤信息"
    read -p "按 Enter 退出..."
    exit 1
fi
