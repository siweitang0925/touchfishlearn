"""
完整功能演示 v2.0 - 包含当天已答对功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.word_model import Word, WordManager
from src.gui.study_popup import StudyPopup
import tkinter as tk
from datetime import datetime

def demo_all_features():
    """演示所有功能"""
    print("=" * 60)
    print("🎓 英语学习助手 - 完整功能演示 v2.0")
    print("=" * 60)
    
    # 创建单词管理器
    word_manager = WordManager()
    
    # 清空现有数据
    word_manager.words = []
    
    # 添加演示单词
    demo_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("book", "书", "I read a book."),
        ("cat", "猫", "The cat is sleeping."),
        ("dog", "狗", "The dog is running."),
        ("elephant", "大象", "The elephant is big."),
        ("fish", "鱼", "The fish is swimming."),
        ("garden", "花园", "The garden is beautiful."),
        ("house", "房子", "I live in a big house."),
        ("internet", "互联网", "I use the internet every day."),
        ("journey", "旅程", "Life is a journey.")
    ]
    
    print("📝 1. 添加演示单词...")
    for word, meaning, example in demo_words:
        word_manager.add_word(word, meaning, example)
    print(f"   ✅ 成功添加 {len(demo_words)} 个单词")
    
    print("\n📊 2. 显示初始统计信息...")
    total_count = word_manager.get_word_count()
    studyable_count = len(word_manager.get_studyable_words())
    today_correct_count = word_manager.get_today_correct_count()
    print(f"   📈 总单词数: {total_count}")
    print(f"   📚 可学习数: {studyable_count}")
    print(f"   ✅ 今日已答对: {today_correct_count}")
    
    print("\n🎯 3. 演示学习功能...")
    print("   模拟答对几个单词...")
    
    # 模拟答对几个单词
    correct_words = ["apple", "book", "cat"]
    for word in correct_words:
        word_manager.increase_proficiency(word)
        print(f"   ✅ 答对单词: {word}")
    
    print("\n📊 4. 显示答对后的统计信息...")
    studyable_count = len(word_manager.get_studyable_words())
    today_correct_count = word_manager.get_today_correct_count()
    print(f"   📚 可学习数: {studyable_count} (减少了{len(correct_words)}个)")
    print(f"   ✅ 今日已答对: {today_correct_count}")
    
    print("\n🔍 5. 演示搜索功能...")
    search_results = word_manager.search_words("cat")
    print(f"   搜索 'cat': 找到 {len(search_results)} 个结果")
    
    print("\n📋 6. 显示单词详细信息...")
    print("   单词列表预览:")
    for i, word in enumerate(word_manager.words[:5]):
        today = datetime.now().strftime('%Y-%m-%d')
        status = "✅ 已答对" if word.last_correct_date == today else "⏳ 未答对"
        print(f"   {i+1}. {word.word} - {word.meaning} (熟练度: {'★' * word.proficiency + '☆' * (5 - word.proficiency)}) [{status}]")
    
    print("\n🎮 7. 演示独立弹框功能...")
    print("   创建独立弹框（不依赖主窗口）...")
    
    # 获取一个未答对的单词
    random_word = word_manager.get_random_word()
    if random_word:
        print(f"   随机单词: {random_word.word} - {random_word.meaning}")
        print("   弹框特性:")
        print("   - 使用独立窗口 (tk.Tk())")
        print("   - 不依赖主窗口状态")
        print("   - 始终置顶显示")
        print("   - 答对后自动关闭")
        print("   - 答错后保持显示")
        
        # 创建弹框
        popup = StudyPopup(None, random_word, word_manager)
        
        def on_popup_closed():
            print("   ✅ 弹框已关闭")
        
        popup.set_close_callback(on_popup_closed)
        
        print("   显示弹框进行测试...")
        popup.show()
    else:
        print("   ⚠️ 没有可用的单词进行测试")
    
    print("\n🎉 8. 功能总结:")
    print("   ✅ 生词本管理 - 添加、编辑、删除、搜索")
    print("   ✅ 熟练度系统 - 智能学习调度")
    print("   ✅ 每日学习限制 - 当天已答对不再弹出")
    print("   ✅ 独立弹框 - 主窗口最小化时仍能显示")
    print("   ✅ 系统托盘 - 后台运行不干扰工作")
    print("   ✅ 数据持久化 - 自动保存学习进度")
    print("   ✅ 可执行文件 - 无需Python环境")
    
    print("\n🚀 现在可以运行主程序体验完整功能！")
    print("   运行命令: python main.py")
    print("   或直接运行: dist/英语学习助手.exe")

if __name__ == "__main__":
    demo_all_features() 