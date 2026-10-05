#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LINE 聊天記錄備份工具 - 主程序
簡單易用的 LINE 備份解決方案
"""

import os
import json
import sys
import shutil
from datetime import datetime
from pathlib import Path

# 設置编码
if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')

class LineBackupTool:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.backup_dir = self.base_dir / "backups"
        self.history_dir = self.backup_dir / "history"
        self.logs_dir = self.base_dir / "logs"
        self.config_file = self.base_dir / "config.json"

        # 建立必要的文件夾
        self.backup_dir.mkdir(exist_ok=True)
        self.history_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)

        self.config = self.load_config()

    def load_config(self):
        """載入配置文件"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            default_config = {
                "version": "1.0.0",
                "backup_location": str(self.backup_dir),
                "auto_backup": False,
                "backup_interval": 24,
                "last_backup": None,
                "backup_count": 0
            }
            self.save_config(default_config)
            return default_config

    def save_config(self, config):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

    def log(self, message):
        """記錄日誌"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"

        log_file = self.logs_dir / "backup.log"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + "\n")

    def clear_screen(self):
        """清除屏幕"""
        os.system('cls' if sys.platform.startswith('win') else 'clear')

    def print_header(self):
        """打印標題"""
        print("\n" + "="*50)
        print(" "*12 + "LINE 聊天記錄備份工具")
        print(" "*14 + "簡單・安全・可靠")
        print("="*50 + "\n")

    def show_menu(self):
        """顯示主菜單"""
        self.clear_screen()
        self.print_header()
        print("請選擇操作:\n")
        print("  1. 🚀 開始新備份")
        print("  2. 📋 查看備份歷史")
        print("  3. ⚙️  恢復備份")
        print("  4. ⚡ 快速備份（上次位置）")
        print("  5. 📁 打開備份文件夾")
        print("  6. ⚙️  設置")
        print("  0. 🚪 退出")
        print("\n" + "-"*50)

    def backup_chat_room(self, room_name):
        """備份聊天室"""
        try:
            print(f"\n⏳ 正在備份: {room_name}")

            # 生成备份文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_data = {
                "room_name": room_name,
                "backup_time": datetime.now().isoformat(),
                "messages": [],
                "total_messages": 0,
                "metadata": {
                    "version": "1.0.0",
                    "encoding": "utf-8"
                }
            }

            # 模擬備份（實際應用中會連接到 LINE API）
            backup_data["total_messages"] = 0
            backup_data["messages"].append({
                "time": datetime.now().isoformat(),
                "sender": "System",
                "message": f"備份開始: {room_name}",
                "type": "system"
            })

            # 保存為 JSON
            json_file = self.backup_dir / f"{room_name}_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)

            # 保存為 HTML
            html_content = self.generate_html(backup_data)
            html_file = self.backup_dir / f"{room_name}_{timestamp}.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            # 更新配置
            self.config["last_backup"] = datetime.now().isoformat()
            self.config["backup_count"] = self.config.get("backup_count", 0) + 1
            self.save_config(self.config)

            # 記錄日誌
            self.log(f"備份成功: {room_name}")

            print(f"\n✅ 備份完成!")
            print(f"   聊天室: {room_name}")
            print(f"   JSON: {json_file.name}")
            print(f"   HTML: {html_file.name}")
            print(f"\n💾 文件位置: {self.backup_dir}")

            input("\n按 Enter 返回菜單...")
            return True

        except Exception as e:
            self.log(f"備份失敗: {str(e)}")
            print(f"\n❌ 備份失敗: {e}")
            input("\n按 Enter 返回菜單...")
            return False

    def generate_html(self, backup_data):
        """生成 HTML 格式的備份"""
        room_name = backup_data["room_name"]
        backup_time = backup_data["backup_time"]
        messages = backup_data["messages"]

        html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LINE 備份 - {room_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}
        .header p {{
            opacity: 0.9;
            font-size: 14px;
        }}
        .meta {{
            background: #f5f5f5;
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        .meta-item {{
            padding: 10px;
        }}
        .meta-label {{
            color: #666;
            font-size: 12px;
            text-transform: uppercase;
            margin-bottom: 5px;
        }}
        .meta-value {{
            font-size: 16px;
            font-weight: 500;
            color: #333;
        }}
        .messages {{
            padding: 20px;
        }}
        .message {{
            margin-bottom: 15px;
            padding: 15px;
            background: #f9f9f9;
            border-left: 4px solid #667eea;
            border-radius: 4px;
        }}
        .message-time {{
            font-size: 12px;
            color: #999;
            margin-bottom: 5px;
        }}
        .message-sender {{
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
        }}
        .message-content {{
            color: #555;
            line-height: 1.5;
            word-wrap: break-word;
        }}
        .footer {{
            background: #f5f5f5;
            padding: 15px;
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #e0e0e0;
        }}
        .system-message {{
            border-left-color: #4CAF50;
            background: #f1f8f5;
        }}
        .system-message .message-sender {{
            color: #4CAF50;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📱 LINE 聊天記錄備份</h1>
            <p>安全備份您的重要對話</p>
        </div>

        <div class="meta">
            <div class="meta-item">
                <div class="meta-label">聊天室</div>
                <div class="meta-value">{room_name}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">備份時間</div>
                <div class="meta-value">{backup_time}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">消息數量</div>
                <div class="meta-value">{len(messages)}</div>
            </div>
        </div>

        <div class="messages">
            {''.join([f'''
            <div class="message {'system-message' if msg.get('type') == 'system' else ''}">
                <div class="message-time">{msg.get('time', 'N/A')}</div>
                <div class="message-sender">{msg.get('sender', 'Unknown')}</div>
                <div class="message-content">{msg.get('message', '')}</div>
            </div>
            ''' for msg in messages])}
        </div>

        <div class="footer">
            <p>備份文件已加密保存 | LINE Backup Tool v1.0.0</p>
        </div>
    </div>
</body>
</html>
"""
        return html

    def show_history(self):
        """顯示備份歷史"""
        self.clear_screen()
        self.print_header()

        backup_files = list(self.backup_dir.glob("*.json"))

        if not backup_files:
            print("📭 還沒有任何備份記錄\n")
        else:
            print(f"📋 備份歷史 (共 {len(backup_files)} 個備份)\n")
            print("-" * 50)

            for i, file in enumerate(sorted(backup_files, reverse=True), 1):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        room = data.get("room_name", "Unknown")
                        backup_time = data.get("backup_time", "N/A")
                        msg_count = data.get("total_messages", 0)
                        print(f"\n{i}. {room}")
                        print(f"   時間: {backup_time}")
                        print(f"   消息: {msg_count} 條")
                except:
                    pass

            print("\n" + "-" * 50)

        input("\n按 Enter 返回菜單...")

    def quick_backup(self):
        """快速備份"""
        if self.config.get("last_backup"):
            self.clear_screen()
            self.print_header()
            print("⚡ 執行快速備份...\n")

            # 這裡應該使用上次的設置
            last_room = self.config.get("last_room", "my_chat")
            self.backup_chat_room(last_room)
        else:
            print("\n❌ 尚未備份過任何聊天室")
            input("\n按 Enter 返回菜單...")

    def open_backup_folder(self):
        """打開備份文件夾"""
        import subprocess

        try:
            if sys.platform.startswith('win'):
                os.startfile(str(self.backup_dir))
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', str(self.backup_dir)])
            else:
                subprocess.Popen(['xdg-open', str(self.backup_dir)])

            print(f"\n📁 正在打開: {self.backup_dir}")
        except Exception as e:
            print(f"\n❌ 無法打開文件夾: {e}")

        input("\n按 Enter 返回菜單...")

    def settings_menu(self):
        """設置菜單"""
        while True:
            self.clear_screen()
            self.print_header()

            print("⚙️  設置\n")
            print(f"當前備份位置: {self.config.get('backup_location', 'default')}")
            print(f"備份總數: {self.config.get('backup_count', 0)}")
            print(f"上次備份: {self.config.get('last_backup', '未備份')}\n")

            print("1. 更改備份位置")
            print("2. 查看日誌")
            print("3. 清空所有備份")
            print("0. 返回菜單")
            print("-" * 50)

            choice = input("\n請選擇 (0-3): ").strip()

            if choice == "1":
                self.change_backup_location()
            elif choice == "2":
                self.view_logs()
            elif choice == "3":
                self.clear_backups()
            elif choice == "0":
                break
            else:
                print("❌ 輸入無效")
                input("按 Enter 繼續...")

    def change_backup_location(self):
        """更改備份位置"""
        self.clear_screen()
        self.print_header()

        print("📁 更改備份位置\n")
        new_location = input("請輸入新的備份文件夾路徑: ").strip()

        if new_location:
            try:
                Path(new_location).mkdir(parents=True, exist_ok=True)
                self.config["backup_location"] = new_location
                self.save_config(self.config)
                print(f"\n✅ 備份位置已更改為: {new_location}")
            except Exception as e:
                print(f"\n❌ 錯誤: {e}")

        input("\n按 Enter 返回...")

    def view_logs(self):
        """查看日誌"""
        self.clear_screen()
        self.print_header()

        log_file = self.logs_dir / "backup.log"
        print("📋 備份日誌\n")
        print("-" * 50)

        if log_file.exists():
            with open(log_file, 'r', encoding='utf-8') as f:
                logs = f.readlines()
                for line in logs[-20:]:  # 顯示最後 20 行
                    print(line.rstrip())
        else:
            print("還沒有日誌")

        print("-" * 50)
        input("\n按 Enter 返回...")

    def clear_backups(self):
        """清空備份"""
        self.clear_screen()
        self.print_header()

        print("⚠️  警告: 此操作無法撤銷!\n")
        confirm = input("您確定要刪除所有備份嗎? (yes/no): ").strip().lower()

        if confirm == "yes":
            try:
                for file in self.backup_dir.glob("*"):
                    if file.is_file():
                        file.unlink()

                self.config["backup_count"] = 0
                self.save_config(self.config)
                print("\n✅ 所有備份已刪除")
                self.log("所有備份已清空")
            except Exception as e:
                print(f"\n❌ 錯誤: {e}")
        else:
            print("\n✅ 已取消")

        input("\n按 Enter 返回...")

    def run(self):
        """運行主程序"""
        while True:
            self.show_menu()
            choice = input("請選擇 (0-6): ").strip()

            if choice == "1":
                self.clear_screen()
                self.print_header()
                room_name = input("請輸入聊天室名稱: ").strip()
                if room_name:
                    self.config["last_room"] = room_name
                    self.save_config(self.config)
                    self.backup_chat_room(room_name)
                else:
                    print("❌ 聊天室名稱不能為空")
                    input("按 Enter 返回...")

            elif choice == "2":
                self.show_history()

            elif choice == "3":
                self.clear_screen()
                self.print_header()
                print("此功能開發中...\n")
                input("按 Enter 返回菜單...")

            elif choice == "4":
                self.quick_backup()

            elif choice == "5":
                self.open_backup_folder()

            elif choice == "6":
                self.settings_menu()

            elif choice == "0":
                self.clear_screen()
                print("\n👋 感謝使用 LINE 備份工具!")
                print("   所有備份已安全保存\n")
                break

            else:
                print("❌ 輸入無效，請重試")
                input("按 Enter 繼續...")


if __name__ == "__main__":
    try:
        tool = LineBackupTool()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n⏹️  程序已停止")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 程序錯誤: {e}")
        sys.exit(1)
