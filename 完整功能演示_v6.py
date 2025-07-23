"""
完整功能演示 v6.0 - 包含系统栏图标功能
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
    print("🎓 英语学习助手 - 完整功能演示 v6.0")
    print("=" * 60)
    
    # 创建单词管理器
    word_manager = WordManager()
    
    print("📊 1. 显示当前单词统计...")
    total_count = word_manager.get_word_count()
    studyable_count = len(word_manager.get_studyable_words())
    today_correct_count = word_manager.get_today_correct_count()
    today_wrong_count = word_manager.get_today_wrong_count()
    print(f"   📈 总单词数: {total_count}")
    print(f"   📚 可学习数: {studyable_count}")
    print(f"   ✅ 今日已答对: {today_correct_count} 个")
    print(f"   ❌ 今日答错: {today_wrong_count} 个")
    
    if total_count > 0:
        print("\n📋 2. 雅思高频词汇预览:")
        print("   前10个雅思高频词汇:")
        for i, word in enumerate(word_manager.words[:10]):
            print(f"   {i+1}. {word.word} - {word.meaning}")
            print(f"      例句: {word.example}")
        
        print("\n🎯 3. 演示学习功能...")
        print("   模拟答对几个单词...")
        
        # 模拟答对几个单词
        correct_words = ["academic", "accomplish"]
        for word in correct_words:
            word_manager.increase_proficiency(word)
            print(f"   ✅ 答对单词: {word}")
        
        print("   模拟答错几个单词...")
        # 模拟答错几个单词
        wrong_words = ["accurate", "achieve"]
        for word in wrong_words:
            word_manager.decrease_proficiency(word)
            print(f"   ❌ 答错单词: {word}")
        
        print("\n📊 4. 显示学习后的统计信息...")
        studyable_count = len(word_manager.get_studyable_words())
        today_correct_count = word_manager.get_today_correct_count()
        today_wrong_count = word_manager.get_today_wrong_count()
        today_practice_count = word_manager.get_today_practice_count()
        print(f"   📚 可学习数: {studyable_count} (减少了{len(correct_words) + len(wrong_words)}个)")
        print(f"   ✅ 今日已答对: {today_correct_count} 个")
        print(f"   ❌ 今日答错: {today_wrong_count} 个")
        print(f"   📝 今日已练习: {today_practice_count} 个")
        
        print("\n🔍 5. 演示搜索功能...")
        search_results = word_manager.search_words("academic")
        print(f"   搜索 'academic': 找到 {len(search_results)} 个结果")
        if search_results:
            print(f"   结果: {search_results[0].word} - {search_results[0].meaning}")
        
        print("\n📋 6. 显示单词详细信息（三种状态）...")
        print("   单词列表预览:")
        for i, word in enumerate(word_manager.words[:8]):
            today = datetime.now().strftime('%Y-%m-%d')
            if word.last_practice_date == today:
                if word.last_correct_date == today:
                    status = "✅ 已答对"
                else:
                    status = "❌ 未答对"
            else:
                status = "⏳ 未练习"
            print(f"   {i+1}. {word.word} - {word.meaning} (熟练度: {'★' * word.proficiency + '☆' * (5 - word.proficiency)}) [{status}]")
        
        print("\n🎮 7. 演示独立弹框功能...")
        print("   创建独立弹框（不依赖主窗口）...")
        
        # 获取一个未练习的单词
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
        
        print("\n🖱️ 8. 演示系统托盘和系统栏图标功能...")
        print("   托盘功能特性:")
        print("   - 程序最小化到系统托盘")
        print("   - 单击系统托盘图标显示主窗口")
        print("   - 支持窗口最小化事件处理")
        print("   - 支持窗口恢复事件处理")
        print("   - 右键托盘图标显示菜单")
        print("   - 菜单包含：显示主窗口、停止学习、退出")
        print("   - 后台运行不干扰工作")
        print("   - 托盘图标保持运行，可以重复使用")
        
        print("\n🎉 9. 功能总结:")
        print("   ✅ 生词本管理 - 添加、编辑、删除、搜索")
        print("   ✅ 雅思高频词汇 - 内置50个雅思高频词汇，首次启动自动加载")
        print("   ✅ 熟练度系统 - 智能学习调度")
        print("   ✅ 三种今日状态 - 未练习、未答对、已答对")
        print("   ✅ 每日学习限制 - 当天已练习过的单词不再弹出")
        print("   ✅ 独立弹框 - 主窗口最小化时仍能显示")
        print("   ✅ 系统托盘 - 单击系统栏图标显示主窗口，后台运行")
        print("   ✅ 窗口事件处理 - 支持最小化和恢复事件")
        print("   ✅ 数据持久化 - 自动保存学习进度")
        print("   ✅ 可执行文件 - 无需Python环境")
        
        print("\n🚀 现在可以运行主程序体验完整功能！")
        print("   运行命令: python main.py")
        print("   或直接运行: dist/英语学习助手.exe")
        print("\n💡 使用提示:")
        print("   1. 程序首次启动会自动加载50个雅思高频词汇")
        print("   2. 启动摸鱼学习后程序会最小化到托盘")
        print("   3. 单击系统托盘图标可以快速显示主窗口")
        print("   4. 支持窗口最小化事件处理")
        print("   5. 右键托盘图标可以访问更多功能")
        print("   6. 雅思词汇包含学术、商务、生活等高频词汇")
        print("   7. 托盘图标保持运行，可以多次最小化和显示")
    else:
        print("❌ 雅思词汇加载失败")
        print("请检查 assets/data/ielts_1000_words.json 文件是否存在")

if __name__ == "__main__":
    demo_all_features() 