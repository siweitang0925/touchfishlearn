"""
主窗口界面
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading
import time
import json
import os
from typing import Optional

# 尝试导入系统托盘功能
try:
    import pystray
    from PIL import Image, ImageDraw
    TRAY_AVAILABLE = True
except ImportError:
    TRAY_AVAILABLE = False

import sys
import os

# 添加src目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.dirname(current_dir)

if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from data.word_model import WordManager
    from gui.study_popup import StudyPopup
except ImportError:
    # 备用导入方式
    from src.data.word_model import WordManager
    from src.gui.study_popup import StudyPopup


class MainWindow:
    """主窗口类"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("英语学习助手 - 生词本")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # 初始化数据管理器
        self.word_manager = WordManager()
        
        # 学习线程
        self.study_thread: Optional[threading.Thread] = None
        self.study_running = False
        
        # 设置文件
        self.settings_file = "settings.json"
        
        # 系统托盘相关
        self.tray_icon = None
        self.is_minimized = False
        
        # 弹框状态管理
        self.current_popup = None
        self.popup_lock = threading.Lock()
        
        self.setup_ui()
        self.load_word_list()
        
        # 绑定窗口事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Unmap>", self.on_minimize)
        self.root.bind("<Map>", self.on_restore)
    
    def setup_ui(self):
        """设置用户界面"""
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # 标题
        title_label = ttk.Label(main_frame, text="英语学习助手", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 添加单词区域
        add_frame = ttk.LabelFrame(main_frame, text="添加新单词", padding="10")
        add_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        add_frame.columnconfigure(1, weight=1)
        add_frame.columnconfigure(3, weight=1)
        
        # 单词输入
        ttk.Label(add_frame, text="单词:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.word_entry = ttk.Entry(add_frame, width=20)
        self.word_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # 中文含义输入
        ttk.Label(add_frame, text="中文含义:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.meaning_entry = ttk.Entry(add_frame, width=20)
        self.meaning_entry.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # 例句输入
        ttk.Label(add_frame, text="例句:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=(10, 0))
        self.example_entry = ttk.Entry(add_frame, width=50)
        self.example_entry.grid(row=1, column=1, columnspan=3, sticky=(tk.W, tk.E), 
                               padx=(0, 10), pady=(10, 0))
        
        # 添加按钮
        add_btn = ttk.Button(add_frame, text="添加单词", command=self.add_word)
        add_btn.grid(row=1, column=4, padx=(10, 0), pady=(10, 0))
        
        # 搜索区域
        search_frame = ttk.LabelFrame(main_frame, text="搜索和设置", padding="10")
        search_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        search_frame.columnconfigure(1, weight=1)
        search_frame.columnconfigure(3, weight=1)
        
        # 搜索功能
        ttk.Label(search_frame, text="搜索单词:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.search_entry = ttk.Entry(search_frame, width=25)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        clear_search_btn = ttk.Button(search_frame, text="清除搜索", command=self.clear_search)
        clear_search_btn.grid(row=0, column=2, padx=(0, 20))
        
        # 学习间隔设置
        ttk.Label(search_frame, text="学习间隔(分钟):").grid(row=0, column=3, sticky=tk.W, padx=(0, 5))
        self.interval_var = tk.StringVar(value="10")
        self.interval_spinbox = ttk.Spinbox(search_frame, from_=1, to=60, width=8, 
                                           textvariable=self.interval_var)
        self.interval_spinbox.grid(row=0, column=4, padx=(0, 10))
        
        # 单词列表区域
        list_frame = ttk.LabelFrame(main_frame, text="生词本", padding="10")
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # 创建Treeview
        columns = ("单词", "中文含义", "熟练度", "今日状态", "例句", "创建时间")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        # 设置列标题
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "熟练度":
                self.tree.column(col, width=100)
            elif col == "今日状态":
                self.tree.column(col, width=80)
            elif col == "例句":
                self.tree.column(col, width=200)
            else:
                self.tree.column(col, width=120)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 绑定双击事件
        self.tree.bind("<Double-1>", self.on_word_double_click)
        
        # 操作按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=(0, 10))
        
        # 删除按钮
        delete_btn = ttk.Button(button_frame, text="删除选中", command=self.delete_word)
        delete_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # 清空按钮
        clear_btn = ttk.Button(button_frame, text="清空生词本", command=self.clear_words)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # 摸鱼学习按钮
        self.study_btn = ttk.Button(button_frame, text="启动摸鱼学习", 
                                   command=self.toggle_study_mode)
        self.study_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # 状态标签
        self.status_label = ttk.Label(button_frame, text="就绪")
        self.status_label.pack(side=tk.RIGHT)
        
        # 统计信息
        self.update_stats()
        
        # 加载设置
        self.load_settings()
    
    def add_word(self):
        """添加单词"""
        word = self.word_entry.get().strip()
        meaning = self.meaning_entry.get().strip()
        example = self.example_entry.get().strip()
        
        if not word or not meaning:
            messagebox.showwarning("警告", "请输入单词和中文含义！")
            return
        
        if self.word_manager.add_word(word, meaning, example):
            self.load_word_list()
            self.update_stats()
            self.clear_entries()
            messagebox.showinfo("成功", f"已添加单词: {word}")
        else:
            messagebox.showwarning("警告", f"单词 '{word}' 已存在！")
    
    def delete_word(self):
        """删除选中的单词"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择要删除的单词！")
            return
        
        item = selection[0]
        word = self.tree.item(item, "values")[0]
        
        if messagebox.askyesno("确认", f"确定要删除单词 '{word}' 吗？"):
            if self.word_manager.remove_word(word):
                self.load_word_list()
                self.update_stats()
                messagebox.showinfo("成功", f"已删除单词: {word}")
    
    def clear_words(self):
        """清空生词本"""
        if not self.word_manager.words:
            messagebox.showinfo("提示", "生词本已经是空的！")
            return
        
        if messagebox.askyesno("确认", "确定要清空所有单词吗？此操作不可恢复！"):
            self.word_manager.words.clear()
            self.word_manager.save_words()
            self.load_word_list()
            self.update_stats()
            messagebox.showinfo("成功", "已清空生词本")
    
    def on_word_double_click(self, event):
        """双击单词编辑"""
        selection = self.tree.selection()
        if not selection:
            return
        
        item = selection[0]
        values = self.tree.item(item, "values")
        word, meaning, proficiency, today_status, example = values[0], values[1], values[2], values[3], values[4]
        
        # 弹出编辑对话框
        self.edit_word(word, meaning, example)
    
    def edit_word(self, old_word: str, old_meaning: str, old_example: str):
        """编辑单词"""
        # 这里简化处理，直接弹出输入对话框
        new_word = simpledialog.askstring("编辑单词", "单词:", initialvalue=old_word)
        if not new_word:
            return
        
        new_meaning = simpledialog.askstring("编辑单词", "中文含义:", initialvalue=old_meaning)
        if not new_meaning:
            return
        
        new_example = simpledialog.askstring("编辑单词", "例句:", initialvalue=old_example)
        if new_example is None:
            return
        
        # 删除旧单词，添加新单词
        self.word_manager.remove_word(old_word)
        self.word_manager.add_word(new_word, new_meaning, new_example)
        self.load_word_list()
        self.update_stats()
        messagebox.showinfo("成功", f"已更新单词: {new_word}")
    
    def load_word_list(self, search_text=""):
        """加载单词列表"""
        # 清空现有项目
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 获取单词（支持搜索）
        if search_text:
            words_to_show = self.word_manager.search_words(search_text)
        else:
            words_to_show = self.word_manager.get_all_words()
        
        # 添加单词到列表
        for word in words_to_show:
            # 显示熟练度星级
            proficiency_stars = "★" * word.proficiency + "☆" * (5 - word.proficiency)
            
            # 显示今日状态（三种状态）
            from datetime import datetime
            today = datetime.now().strftime('%Y-%m-%d')
            if word.last_practice_date == today:
                if word.last_correct_date == today:
                    today_status = "✅ 已答对"
                else:
                    today_status = "❌ 未答对"
            else:
                today_status = "⏳ 未练习"
            
            self.tree.insert("", "end", values=(
                word.word,
                word.meaning,
                proficiency_stars,
                today_status,
                word.example,
                word.created_time[:10] if word.created_time else ""
            ))
        
        # 更新统计信息
        self.update_stats()
    
    def update_stats(self):
        """更新统计信息"""
        total_count = self.word_manager.get_word_count()
        studyable_count = len(self.word_manager.get_studyable_words())
        today_correct_count = self.word_manager.get_today_correct_count()
        today_wrong_count = self.word_manager.get_today_wrong_count()
        search_text = self.search_entry.get().strip()
        
        if search_text:
            # 显示搜索结果统计
            filtered_count = len(self.word_manager.search_words(search_text))
            self.status_label.config(text=f"共 {total_count} 个单词，可学习 {studyable_count} 个，今日已答对 {today_correct_count} 个，今日答错 {today_wrong_count} 个，搜索到 {filtered_count} 个")
        else:
            # 显示总统计
            self.status_label.config(text=f"共 {total_count} 个单词，可学习 {studyable_count} 个，今日已答对 {today_correct_count} 个，今日答错 {today_wrong_count} 个")
    
    def clear_entries(self):
        """清空输入框"""
        self.word_entry.delete(0, tk.END)
        self.meaning_entry.delete(0, tk.END)
        self.example_entry.delete(0, tk.END)
    
    def on_search(self, event=None):
        """搜索单词"""
        search_text = self.search_entry.get().strip().lower()
        self.load_word_list(search_text)
    
    def clear_search(self):
        """清除搜索"""
        self.search_entry.delete(0, tk.END)
        self.load_word_list()
    
    def get_study_interval(self) -> int:
        """获取学习间隔（分钟）"""
        try:
            interval = int(self.interval_var.get())
            return max(1, min(60, interval))  # 限制在1-60分钟之间
        except ValueError:
            return 10  # 默认10分钟
    
    def load_settings(self):
        """加载设置"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    interval = settings.get('study_interval', 10)
                    self.interval_var.set(str(interval))
        except Exception as e:
            print(f"加载设置失败: {e}")
    
    def save_settings(self):
        """保存设置"""
        try:
            settings = {
                'study_interval': self.get_study_interval()
            }
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存设置失败: {e}")
    
    def create_tray_icon(self):
        """创建系统托盘图标"""
        if not TRAY_AVAILABLE:
            return None
        
        try:
            # 创建一个简单的图标
            image = Image.new('RGB', (64, 64), color='blue')
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), "EN", fill='white')
            
            # 创建托盘菜单
            menu = pystray.Menu(
                pystray.MenuItem("显示主窗口", self.show_main_window_from_menu),
                pystray.MenuItem("停止学习", self.stop_study_from_tray),
                pystray.MenuItem("退出", self.quit_app)
            )
            
            # 创建托盘图标
            icon = pystray.Icon("英语学习助手", image, "英语学习助手", menu)
            
            # 设置双击事件处理函数（比单击更可靠）
            try:
                def on_double_click(icon, event):
                    print("托盘图标被双击")
                    self.root.after(0, self.show_main_window)
                
                icon.on_double_click = on_double_click
                print("双击事件已设置")
            except Exception as e:
                print(f"设置双击事件失败: {e}")
            
            # 尝试设置单击事件（可能在某些系统上不工作）
            try:
                def on_click(icon, event):
                    print("托盘图标被单击")
                    self.root.after(0, self.show_main_window)
                
                icon.on_click = on_click
                print("单击事件已设置（可能不工作）")
            except Exception as e:
                print(f"设置单击事件失败: {e}")
            return icon
        except Exception as e:
            print(f"创建系统托盘失败: {e}")
            return None
    
    def minimize_to_tray(self):
        """最小化到系统托盘"""
        if not TRAY_AVAILABLE:
            # 如果不支持系统托盘，就只是隐藏窗口
            self.root.withdraw()
            self.is_minimized = True
            return
        
        # 如果已经最小化到托盘，直接返回
        if self.is_minimized:
            return
        
        try:
            # 创建系统托盘图标（如果还没有创建）
            if not self.tray_icon:
                self.tray_icon = self.create_tray_icon()
                # 启动托盘图标
                if self.tray_icon:
                    threading.Thread(target=self.tray_icon.run, daemon=True).start()
                    print("托盘图标已创建并启动")
                else:
                    print("托盘图标创建失败")
                    return
            
            # 隐藏主窗口
            self.root.withdraw()
            self.is_minimized = True
            
            print("程序已最小化到系统托盘")
        except Exception as e:
            print(f"最小化到托盘失败: {e}")
            # 回退到普通隐藏
            self.root.withdraw()
            self.is_minimized = True
    
    def show_main_window(self, icon=None, item=None):
        """显示主窗口"""
        print("正在显示主窗口...")
        try:
            self.root.deiconify()
            self.root.lift()
            self.root.focus_force()
            self.root.state('normal')  # 确保窗口状态正常
            self.is_minimized = False
            print("主窗口已显示")
        except Exception as e:
            print(f"显示主窗口失败: {e}")
        
        # 不停止托盘图标，让它继续运行
        # 这样用户可以继续通过托盘图标操作
    
    def stop_study_from_tray(self, icon=None, item=None):
        """从托盘停止学习"""
        self.stop_study_mode()
        self.show_main_window()
    
    def show_main_window_from_menu(self, icon=None, item=None):
        """从菜单显示主窗口"""
        print("从菜单显示主窗口")
        self.show_main_window()
    
    def quit_app(self, icon=None, item=None):
        """退出应用"""
        self.stop_study_mode()
        if self.tray_icon:
            try:
                self.tray_icon.stop()
                self.tray_icon = None
            except:
                pass
        self.root.quit()
    
    def toggle_study_mode(self):
        """切换学习模式"""
        if self.study_running:
            self.stop_study_mode()
        else:
            self.start_study_mode()
    
    def start_study_mode(self):
        """启动摸鱼学习模式"""
        studyable_count = len(self.word_manager.get_studyable_words())
        if studyable_count == 0:
            messagebox.showwarning("警告", "没有可学习的单词！\n所有单词熟练度都已达到5星，或一个月内已学习过。")
            return
        
        # 保存当前设置
        self.save_settings()
        
        self.study_running = True
        self.study_btn.config(text="停止摸鱼学习")
        
        # 获取间隔时间
        interval = self.get_study_interval()
        self.status_label.config(text=f"摸鱼学习中... (间隔{interval}分钟)")
        
        # 启动学习线程
        self.study_thread = threading.Thread(target=self.study_loop, daemon=True)
        self.study_thread.start()
        
        # 显示提示信息
        messagebox.showinfo("提示", f"摸鱼学习已启动！\n每{interval}分钟会弹出单词测试。\n程序将最小化到系统托盘。")
        
        # 最小化到系统托盘
        self.minimize_to_tray()
    
    def stop_study_mode(self):
        """停止摸鱼学习模式"""
        self.study_running = False
        self.study_btn.config(text="启动摸鱼学习")
        self.status_label.config(text="已停止学习")
        
        # 如果窗口被最小化，重新显示
        if self.is_minimized:
            self.show_main_window()
    
    def study_loop(self):
        """学习循环"""
        while self.study_running:
            # 获取当前设置的间隔时间
            interval_minutes = self.get_study_interval()
            interval_seconds = interval_minutes * 60
            
            time.sleep(interval_seconds)  # 等待指定时间
            
            if not self.study_running:
                break
            
            # 在主线程中显示弹窗
            self.root.after(0, self.show_study_popup)
    
    def show_study_popup(self):
        """显示学习弹窗"""
        if not self.study_running:
            return
        
        # 检查是否已有弹框在显示
        with self.popup_lock:
            if self.current_popup is not None:
                try:
                    # 检查弹框是否还存在
                    self.current_popup.popup.winfo_exists()
                    print("已有弹框在显示，跳过本次弹出")
                    return
                except:
                    # 弹框已关闭，清除引用
                    self.current_popup = None
        
        word = self.word_manager.get_random_word()
        if not word:
            return
        
        try:
            # 创建学习弹窗（独立窗口，不依赖于主窗口）
            popup = StudyPopup(None, word, self.word_manager)
            
            # 设置弹框关闭回调
            popup.set_close_callback(self.on_popup_closed)
            
            # 记录当前弹框
            with self.popup_lock:
                self.current_popup = popup
            
            popup.show()
        except Exception as e:
            print(f"显示学习弹窗失败: {e}")
            with self.popup_lock:
                self.current_popup = None
    
    def on_popup_closed(self):
        """弹框关闭回调"""
        with self.popup_lock:
            self.current_popup = None
            print("弹框已关闭，可以弹出新的弹框")
        
        # 更新单词列表显示（因为可能有单词被标记为已答对）
        self.load_word_list()
    
    def on_closing(self):
        """窗口关闭事件"""
        self.stop_study_mode()
        if self.tray_icon:
            try:
                self.tray_icon.stop()
                self.tray_icon = None
            except:
                pass
        self.root.destroy()
    
    def on_minimize(self, event):
        """窗口最小化事件"""
        if self.study_running and not self.is_minimized:
            # 如果学习模式正在运行且窗口还没有最小化到托盘，则最小化到托盘
            self.minimize_to_tray()
    
    def on_restore(self, event):
        """窗口恢复事件"""
        if self.is_minimized:
            self.is_minimized = False
    
    def run(self):
        """运行主窗口"""
        self.root.mainloop() 