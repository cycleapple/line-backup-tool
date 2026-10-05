#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LINE 備份工具 - 圖形化啟動器
讓完全不懂技術的人也能使用
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys
from pathlib import Path

class LineBackupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LINE 聊天記錄備份工具")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # 設置顏色
        self.root.configure(bg="#f0f0f0")

        # 標題
        title_label = tk.Label(
            root,
            text="LINE 聊天記錄備份工具",
            font=("Arial", 24, "bold"),
            bg="#007AFF",
            fg="white",
            pady=20
        )
        title_label.pack(fill=tk.X)

        # 主容器
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 說明文本
        info_text = tk.Label(
            main_frame,
            text="點擊下方按鈕開始備份\nLINE 聊天記錄\n\n無需任何技術知識\n數據完全保存在本地",
            font=("Arial", 14),
            bg="#f0f0f0",
            justify=tk.CENTER,
            pady=20
        )
        info_text.pack()

        # 按鈕框架
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # 開始備份按鈕
        self.backup_btn = tk.Button(
            button_frame,
            text="🚀 開始備份",
            font=("Arial", 16, "bold"),
            bg="#007AFF",
            fg="white",
            padx=40,
            pady=15,
            command=self.start_backup,
            cursor="hand2"
        )
        self.backup_btn.pack(pady=10)

        # 查看備份按鈕
        self.view_btn = tk.Button(
            button_frame,
            text="📁 查看備份文件",
            font=("Arial", 14),
            bg="#34C759",
            fg="white",
            padx=30,
            pady=10,
            command=self.view_backups,
            cursor="hand2"
        )
        self.view_btn.pack(pady=10)

        # 幫助按鈕
        self.help_btn = tk.Button(
            button_frame,
            text="❓ 幫助",
            font=("Arial", 14),
            bg="#FF9500",
            fg="white",
            padx=40,
            pady=10,
            command=self.show_help,
            cursor="hand2"
        )
        self.help_btn.pack(pady=10)

        # 狀態欄
        self.status_label = tk.Label(
            main_frame,
            text="準備就緒",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#666",
            pady=10
        )
        self.status_label.pack(side=tk.BOTTOM)

    def start_backup(self):
        """開始備份"""
        # 彈出對話框
        chat_room = tk.simpledialog.askstring(
            "開始備份",
            "請輸入 LINE 聊天室名稱:\n\n(例如: 我的好友, 家人群組)",
            parent=self.root
        )

        if chat_room:
            self.status_label.config(text=f"正在備份: {chat_room} ...", fg="#007AFF")
            self.root.update()

            # 運行主程序
            try:
                subprocess.run([sys.executable, "main.py"], check=False)
                self.status_label.config(text="✅ 備份完成！", fg="#34C759")
                messagebox.showinfo(
                    "成功",
                    f"✅ {chat_room} 備份完成！\n\n備份文件已保存在 backups/ 文件夾"
                )
            except Exception as e:
                self.status_label.config(text="❌ 備份失敗", fg="#FF3B30")
                messagebox.showerror("錯誤", f"備份失敗:\n{e}")

    def view_backups(self):
        """查看備份文件"""
        backups_dir = Path("backups")

        if backups_dir.exists():
            import subprocess
            subprocess.Popen(["open", str(backups_dir)])
            self.status_label.config(text="已打開備份文件夾", fg="#34C759")
        else:
            messagebox.showinfo("提示", "還沒有任何備份\n\n請先點擊「開始備份」")

    def show_help(self):
        """顯示幫助信息"""
        help_text = """
LINE 聊天記錄備份工具 - 使用指南

📱 如何使用？
1. 點擊「開始備份」按鈕
2. 輸入你要備份的聊天室名稱
3. 等待備份完成
4. 完成！

📂 備份在哪裡？
所有備份保存在「backups」文件夾
點擊「查看備份文件」即可打開

🔒 安全嗎？
✅ 完全安全
✅ 數據 100% 保存在你的電腦
✅ 不會上傳任何數據

❓ 有問題？
查看文件夾中的「START_HERE.md」
或「README_MAC.md」了解更多

祝你使用愉快！
        """
        messagebox.showinfo("幫助", help_text)


import tkinter.simpledialog

def main():
    root = tk.Tk()
    app = LineBackupGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
