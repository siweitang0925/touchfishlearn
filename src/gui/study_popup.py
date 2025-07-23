"""
学习弹窗
"""
import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import List

import sys
import os

# 添加src目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.dirname(current_dir)

if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from data.word_model import Word, WordManager
except ImportError:
    # 备用导入方式
    from src.data.word_model import Word, WordManager


class StudyPopup:
    """学习弹窗类"""
    
    def __init__(self, parent, word: Word, word_manager: WordManager):
        self.parent = parent
        self.word = word
        self.word_manager = word_manager
        self.correct_answer = word.meaning
        
        # 创建完全独立的顶级窗口，不依赖于主窗口
        self.popup = tk.Tk()  # 使用Tk()而不是Toplevel()
        self.popup.title("摸鱼学习 - 单词测试")
        self.popup.geometry("500x450")
        self.popup.resizable(False, False)
        
        # 设置窗口属性
        self.popup.attributes('-topmost', True)  # 始终置顶
        self.popup.attributes('-toolwindow', True)  # 设置为工具窗口，不显示在任务栏
        
        # 设置透明背景（仅支持部分平台）
        try:
            self.popup.attributes('-alpha', 0.95)  # 设置透明度为95%
        except:
            pass  # 如果不支持透明度，就忽略
        
        # 禁用关闭按钮
        self.popup.protocol("WM_DELETE_WINDOW", self.on_close_attempt)
        
        # 选项按钮
        self.option_buttons = []
        self.selected_answer = None
        self.has_answered = False  # 是否已经回答过
        self.is_correct = False    # 是否答对
        
        # 关闭回调
        self.close_callback = None
        
        self.setup_ui()
        self.generate_options()
        
        # 设置弹框位置（屏幕中央）
        self.popup.update_idletasks()
        x = (self.popup.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.popup.winfo_screenheight() // 2) - (450 // 2)
        self.popup.geometry(f"500x450+{x}+{y}")
        
        # 强制显示弹框
        self.popup.deiconify()
        self.popup.lift()
        self.popup.focus_force()
    
    def setup_ui(self):
        """设置用户界面"""
        # 配置样式
        self.setup_styles()
        
        # 主框架 - 使用透明背景
        main_frame = tk.Frame(self.popup, bg='#f0f8ff', relief='flat', bd=0)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 标题区域
        title_frame = tk.Frame(main_frame, bg='#f0f8ff', relief='flat', bd=0)
        title_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(title_frame, text="🎯 单词测试", 
                              font=("Arial", 20, "bold"), 
                              fg='#2c3e50', bg='#f0f8ff')
        title_label.pack()
        
        # 单词显示区域 - 半透明卡片效果
        word_frame = tk.Frame(main_frame, bg='#ffffff', relief='flat', bd=1)
        word_frame.pack(fill=tk.X, pady=(0, 15), padx=5)
        
        # 单词标题
        word_title = tk.Label(word_frame, text="请选择正确的中文含义", 
                             font=("Arial", 12, "bold"), 
                             fg='#34495e', bg='#ffffff')
        word_title.pack(pady=(10, 5))
        
        # 单词
        word_label = tk.Label(word_frame, text=self.word.word, 
                             font=("Arial", 28, "bold"), 
                             fg='#3498db', bg='#ffffff')
        word_label.pack(pady=(0, 8))
        
        # 熟练度显示
        proficiency_text = "★" * self.word.proficiency + "☆" * (5 - self.word.proficiency)
        proficiency_label = tk.Label(word_frame, text=f"熟练度: {proficiency_text}", 
                                    font=("Arial", 11), 
                                    fg='#f39c12', bg='#ffffff')
        proficiency_label.pack(pady=(0, 10))
        
        # 例句区域（初始隐藏）
        self.example_frame = tk.Frame(word_frame, bg='#ffffff')
        self.example_label = tk.Label(self.example_frame, text="", 
                                     font=("Arial", 10), 
                                     fg='#7f8c8d', bg='#ffffff',
                                     wraplength=400, justify='left')
        self.example_label.pack(pady=5)
        
        # 选项区域
        options_frame = tk.Frame(main_frame, bg='#f0f8ff', relief='flat', bd=0)
        options_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建选项按钮
        self.create_option_buttons(options_frame)
    
    def setup_styles(self):
        """设置样式"""
        # 配置按钮样式
        self.style = ttk.Style()
        
        # 成功按钮样式（答对时）
        self.style.configure("Success.TButton",
                           background="#27ae60",
                           foreground="white",
                           font=("Arial", 10, "bold"))
        
        # 错误按钮样式（答错时）
        self.style.configure("Error.TButton",
                           background="#e74c3c",
                           foreground="white",
                           font=("Arial", 10, "bold"))
        
        # 普通按钮样式
        self.style.configure("Normal.TButton",
                           background="#ecf0f1",
                           foreground="#2c3e50",
                           font=("Arial", 10))
        
        # 悬停效果
        self.style.map("Normal.TButton",
                      background=[("active", "#bdc3c7")])
    
    def create_option_buttons(self, parent):
        """创建选项按钮"""
        # 创建按钮网格
        for i in range(2):  # 2行
            parent.rowconfigure(i, weight=1)
        for i in range(3):  # 3列
            parent.columnconfigure(i, weight=1)
        
        # 创建6个选项按钮 - 使用自定义样式
        for i in range(6):
            row = i // 3
            col = i % 3
            
            # 使用tk.Button而不是ttk.Button以获得更好的样式控制
            btn = tk.Button(parent, text="", 
                          font=("Arial", 11),
                          bg='#ecf0f1',
                          fg='#2c3e50',
                          relief='flat',
                          bd=0,
                          padx=15,
                          pady=10,
                          cursor='hand2',
                          command=lambda idx=i: self.on_option_click(idx))
            
            # 添加悬停效果
            btn.bind('<Enter>', lambda e, b=btn: self.on_button_hover(b, True))
            btn.bind('<Leave>', lambda e, b=btn: self.on_button_hover(b, False))
            
            btn.grid(row=row, column=col, padx=8, pady=8, sticky=(tk.W, tk.E, tk.N, tk.S))
            self.option_buttons.append(btn)
    
    def on_button_hover(self, button, entering):
        """按钮悬停效果"""
        if not self.has_answered:  # 只有在未回答时才显示悬停效果
            if entering:
                button.config(bg='#bdc3c7')
            else:
                button.config(bg='#ecf0f1')
    
    def generate_options(self):
        """生成选项"""
        # 获取所有单词的中文含义作为干扰选项
        all_meanings = [word.meaning for word in self.word_manager.words 
                       if word.meaning != self.correct_answer]
        
        # 随机选择5个不同的干扰选项
        if len(all_meanings) >= 5:
            wrong_options = random.sample(all_meanings, 5)
        else:
            wrong_options = all_meanings
        
        # 添加正确答案
        options = wrong_options + [self.correct_answer]
        random.shuffle(options)  # 随机打乱顺序
        
        # 更新按钮文本
        for i, option in enumerate(options):
            if i < len(self.option_buttons):
                self.option_buttons[i].config(text=option)
    
    def on_option_click(self, button_index):
        """选项点击事件"""
        if self.has_answered:
            return  # 已经回答过，忽略点击
        
        self.has_answered = True
        selected_text = self.option_buttons[button_index].cget("text")
        
        if selected_text == self.correct_answer:
            # 答对了
            self.is_correct = True
            
            # 更新按钮样式 - 使用新的颜色方案
            self.option_buttons[button_index].config(
                text=f"{selected_text} ✓",
                bg='#27ae60',  # 绿色
                fg='white',
                font=("Arial", 11, "bold")
            )
            
            # 增加熟练度
            self.word_manager.increase_proficiency(self.word.word)
            
            # 显示例句
            self.show_example()
            
            # 禁用所有按钮
            for btn in self.option_buttons:
                btn.config(state="disabled")
            
            # 1秒后淡出关闭
            self.popup.after(1000, self.fade_out_and_close)
            
        else:
            # 答错了
            self.is_correct = False
            
            # 找到正确答案的按钮
            correct_button_index = None
            for i, btn in enumerate(self.option_buttons):
                if btn.cget("text") == self.correct_answer:
                    correct_button_index = i
                    break
            
            # 更新按钮样式 - 错误选项显示红色
            self.option_buttons[button_index].config(
                text=f"{selected_text} ✗",
                bg='#e74c3c',  # 红色
                fg='white',
                font=("Arial", 11, "bold")
            )
            
            # 显示正确答案 - 绿色
            if correct_button_index is not None:
                self.option_buttons[correct_button_index].config(
                    text=f"{self.correct_answer} ✓",
                    bg='#27ae60',  # 绿色
                    fg='white',
                    font=("Arial", 11, "bold")
                )
            
            # 减少熟练度
            self.word_manager.decrease_proficiency(self.word.word)
            
            # 显示例句
            self.show_example()
            
            # 禁用所有按钮
            for btn in self.option_buttons:
                btn.config(state="disabled")
            
            # 答错不自动关闭，需要用户手动关闭
    
    def reset_button_styles(self):
        """重置按钮样式"""
        for btn in self.option_buttons:
            btn.config(style="TButton")
    
    def set_close_callback(self, callback):
        """设置关闭回调"""
        self.close_callback = callback
    
    def show_example(self):
        """显示例句"""
        if self.word.example:
            self.example_label.config(text=f"例句: {self.word.example}")
            self.example_frame.pack(pady=(10, 0))
    
    def fade_out_and_close(self):
        """淡出并关闭"""
        try:
            # 更平滑的淡出效果
            current_alpha = self.popup.attributes('-alpha')
            if current_alpha > 0.05:
                # 使用指数衰减，让淡出更自然
                new_alpha = current_alpha * 0.85
                self.popup.attributes('-alpha', new_alpha)
                self.popup.after(30, self.fade_out_and_close)  # 更快的更新频率
            else:
                self.destroy_popup()
        except Exception as e:
            print(f"淡出效果出错: {e}")
            self.destroy_popup()
    
    def destroy_popup(self):
        """销毁弹窗"""
        try:
            # 调用关闭回调
            if self.close_callback:
                self.close_callback()
            
            # 销毁窗口
            self.popup.destroy()
        except Exception as e:
            print(f"销毁弹窗时出错: {e}")
    
    def on_close_attempt(self):
        """尝试关闭窗口"""
        if not self.has_answered:
            # 还没回答，不允许关闭
            messagebox.showwarning("提示", "请先选择一个答案！")
        else:
            # 已经回答过，允许关闭
            self.destroy_popup()
    
    def show(self):
        """显示弹窗"""
        # 确保弹框显示
        self.popup.deiconify()
        self.popup.lift()
        self.popup.focus_force()
        
        # 居中显示
        self.popup.update_idletasks()
        x = (self.popup.winfo_screenwidth() // 2) - (self.popup.winfo_width() // 2)
        y = (self.popup.winfo_screenheight() // 2) - (self.popup.winfo_height() // 2)
        self.popup.geometry(f"+{x}+{y}")
        
        # 显示弹窗
        self.popup.mainloop()  # 使用mainloop()而不是wait_window() 