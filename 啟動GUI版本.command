#!/bin/bash
# LINE 備份工具 - GUI 圖形化版本
# 雙擊即可使用，完全不需要任何技術知識！

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

python3 gui_launcher.py
