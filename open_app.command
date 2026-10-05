#!/bin/bash
# LINE 備份工具 - macOS 一鍵啟動腳本
# 雙擊此文件即可運行

# 獲取腳本所在目錄
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 移動到腳本目錄
cd "$DIR"

# 執行 Python 程序
python3 main.py

# 關閉終端窗口（可選，註釋掉此行則保持窗口開啟）
# exit
