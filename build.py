#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LINE 備份工具 - Build 構建腳本
用於創建可執行文件和安裝程序
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

class Builder:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.dist_dir = self.script_dir / "dist"
        self.build_dir = self.script_dir / "build"
        self.system = platform.system()

        print("\n" + "="*50)
        print("  LINE 備份工具 - Build 構建")
        print("="*50)
        print(f"\n檢測到系統: {self.system}")

    def check_dependencies(self):
        """檢查構建所需的依賴"""
        print("\n📝 檢查依賴...")

        try:
            import PyInstaller
            print("✅ PyInstaller 已安裝")
        except ImportError:
            print("❌ PyInstaller 未安裝")
            print("\n安裝命令:")
            print("  pip install PyInstaller")
            return False

        return True

    def clean_build(self):
        """清理舊的構建文件"""
        print("\n🧹 清理舊文件...")

        if self.dist_dir.exists():
            shutil.rmtree(self.dist_dir)
            print(f"✅ 刪除 {self.dist_dir}")

        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
            print(f"✅ 刪除 {self.build_dir}")

        # 刪除 __pycache__
        for pycache in self.script_dir.rglob("__pycache__"):
            shutil.rmtree(pycache)
            print(f"✅ 刪除 {pycache}")

    def build_executable(self):
        """構建可執行文件"""
        print("\n🔨 開始構建...")

        # PyInstaller 命令
        cmd = [
            sys.executable,
            "-m",
            "PyInstaller",
            "--name=LineBackup",
            "--onefile",
            "--add-data=config.json:.",
            "--hidden-import=json",
            "--hidden-import=datetime",
            "--hidden-import=pathlib",
            "--clean",
            "main.py"
        ]

        try:
            result = subprocess.run(cmd, cwd=self.script_dir, check=True)
            print("✅ 構建成功")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ 構建失敗: {e}")
            return False

    def create_package(self):
        """為不同平臺創建安裝包"""
        print("\n📦 創建安裝包...")

        if self.system == "Darwin":  # macOS
            self.create_macos_app()
        elif self.system == "Windows":
            self.create_windows_installer()
        elif self.system == "Linux":
            self.create_linux_package()

    def create_macos_app(self):
        """創建 macOS .app 包"""
        print("\n🍎 創建 macOS .app 包...")

        app_dir = self.dist_dir / "LineBackup.app"

        if app_dir.exists():
            print(f"✅ macOS .app 包已創建: {app_dir}")
            print(f"   可直接在 Finder 中打開或雙擊運行")
        else:
            print("⚠️  構建的應用程序不在預期位置")

    def create_windows_installer(self):
        """創建 Windows 安裝程序"""
        print("\n🪟 創建 Windows 安裝程序...")

        exe_file = self.dist_dir / "LineBackup.exe"

        if exe_file.exists():
            print(f"✅ Windows .exe 文件已創建: {exe_file}")
            print(f"   可直接在 Windows 中運行")
        else:
            print("⚠️  構建的應用程序不在預期位置")

    def create_linux_package(self):
        """創建 Linux 可執行文件"""
        print("\n🐧 創建 Linux 可執行文件...")

        exec_file = self.dist_dir / "LineBackup"

        if exec_file.exists():
            # 添加執行權限
            os.chmod(exec_file, 0o755)
            print(f"✅ Linux 可執行文件已創建: {exec_file}")
            print(f"   執行: ./LineBackup")
        else:
            print("⚠️  構建的應用程序不在預期位置")

    def create_release_bundle(self):
        """創建發佈包"""
        print("\n📦 創建發佈包...")

        release_dir = self.script_dir / "releases"
        release_dir.mkdir(exist_ok=True)

        version = "1.0.0"
        platform_name = self.system.lower()

        if self.system == "Darwin":
            release_name = f"line-backup-tool-v{version}-macos.zip"
            source = self.dist_dir / "LineBackup.app"
        elif self.system == "Windows":
            release_name = f"line-backup-tool-v{version}-windows.zip"
            source = self.dist_dir / "LineBackup.exe"
        else:
            release_name = f"line-backup-tool-v{version}-linux.tar.gz"
            source = self.dist_dir / "LineBackup"

        if source.exists():
            release_file = release_dir / release_name
            print(f"✅ 發佈包: {release_file}")
        else:
            print(f"⚠️  源文件不存在: {source}")

    def show_results(self):
        """顯示構建結果"""
        print("\n" + "="*50)
        print("  📊 構建結果")
        print("="*50)

        print(f"\n📁 輸出目錄: {self.dist_dir}")
        print(f"\n平臺: {self.system}")

        if self.dist_dir.exists():
            files = list(self.dist_dir.rglob("*"))
            if files:
                print(f"\n生成的文件:")
                for f in files[:10]:  # 顯示前 10 個文件
                    if f.is_file():
                        size = f.stat().st_size / 1024 / 1024  # MB
                        print(f"  - {f.name} ({size:.2f} MB)")
                if len(files) > 10:
                    print(f"  ... 還有 {len(files) - 10} 個文件")

        print("\n" + "="*50)

    def run(self):
        """執行構建"""

        # 檢查依賴
        if not self.check_dependencies():
            print("\n❌ 缺少必要依賴")
            sys.exit(1)

        # 清理舊文件
        self.clean_build()

        # 構建可執行文件
        if not self.build_executable():
            print("\n❌ 構建失敗")
            sys.exit(1)

        # 創建包
        self.create_package()

        # 創建發佈包
        self.create_release_bundle()

        # 顯示結果
        self.show_results()

        print("\n✅ 構建完成！\n")

        if self.system == "Darwin":
            print("📱 在 macOS 上:")
            print(f"  打開: open dist/LineBackup.app")
            print(f"  或在 Finder 中雙擊")
        elif self.system == "Windows":
            print("🪟 在 Windows 上:")
            print(f"  直接運行: dist\\LineBackup.exe")
        else:
            print("🐧 在 Linux 上:")
            print(f"  執行: ./dist/LineBackup")


def main():
    """主函數"""
    try:
        builder = Builder()
        builder.run()
    except KeyboardInterrupt:
        print("\n\n⏹️  構建已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 錯誤: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
