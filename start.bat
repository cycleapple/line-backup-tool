@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

REM LINE 備份工具 - Windows 啟動腳本

cls
echo.
echo ============================================================
echo.
echo              LINE 聊天記錄備份工具
echo.
echo ============================================================
echo.

REM 檢查 Python
python --version > nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Python
    echo.
    echo 請從以下地址下載並安裝 Python 3.8 或更新版本:
    echo https://www.python.org/downloads/
    echo.
    echo 安裝時請勾選: "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ 找到 Python %PYTHON_VERSION%
echo.
echo 🚀 啟動 LINE 備份工具...
echo.

REM 運行主程序
python main.py

if errorlevel 1 (
    echo.
    echo ❌ 運行失敗，請檢查錯誤信息
    pause
    exit /b 1
)

exit /b 0
