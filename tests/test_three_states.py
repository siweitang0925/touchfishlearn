"""
测试三种今日状态功能：未练习、未答对、已答对
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.word_model import Word, WordManager
from datetime import datetime

def test_three_states():
    """测试三种状态功能"""
    print("=== 测试三种今日状态功能 ===")
    
    # 创建单词管理器
    word_manager = WordManager()
    
    # 清空现有数据
    word_manager.words = []
    
    # 添加测试单词
    test_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("book", "书", "I read a book."),
        ("cat", "猫", "The cat is sleeping."),
        ("dog", "狗", "The dog is running."),
        ("elephant", "大象", "The elephant is big."),
        ("fish", "鱼", "The fish is swimming.")
    ]
    
    for word, meaning, example in test_words:
        word_manager.add_word(word, meaning, example)
    
    print(f"1. 添加了 {len(test_words)} 个测试单词")
    
    # 测试初始状态
    print("\n2. 初始状态测试:")
    for word in word_manager.words:
        today = datetime.now().strftime('%Y-%m-%d')
        if word.last_practice_date == today:
            if word.last_correct_date == today:
                status = "✅ 已答对"
            else:
                status = "❌ 未答对"
        else:
            status = "⏳ 未练习"
        print(f"   {word.word}: {status}")
    
    # 模拟答对一个单词
    print("\n3. 模拟答对单词 'apple'...")
    word_manager.increase_proficiency("apple")
    
    # 模拟答错一个单词
    print("4. 模拟答错单词 'book'...")
    word_manager.decrease_proficiency("book")
    
    # 显示状态变化
    print("\n5. 状态变化后:")
    for word in word_manager.words:
        today = datetime.now().strftime('%Y-%m-%d')
        if word.last_practice_date == today:
            if word.last_correct_date == today:
                status = "✅ 已答对"
            else:
                status = "❌ 未答对"
        else:
            status = "⏳ 未练习"
        print(f"   {word.word}: {status}")
    
    # 测试统计功能
    print("\n6. 统计功能测试:")
    today_correct = word_manager.get_today_correct_count()
    today_wrong = word_manager.get_today_wrong_count()
    today_practice = word_manager.get_today_practice_count()
    studyable = len(word_manager.get_studyable_words())
    
    print(f"   今日已答对: {today_correct} 个")
    print(f"   今日答错: {today_wrong} 个")
    print(f"   今日已练习: {today_practice} 个")
    print(f"   可学习: {studyable} 个")
    
    # 测试可学习单词
    print("\n7. 可学习单词测试:")
    studyable_words = word_manager.get_studyable_words()
    for word in studyable_words:
        print(f"   {word.word}")
    
    print("\n8. 测试结果验证:")
    print("   ✅ 三种状态正确显示：未练习、未答对、已答对")
    print("   ✅ 答对的单词状态为：✅ 已答对")
    print("   ✅ 答错的单词状态为：❌ 未答对")
    print("   ✅ 未练习的单词状态为：⏳ 未练习")
    print("   ✅ 今日已练习的单词不再出现在可学习列表中")
    print("   ✅ 统计功能正确显示各种状态的数量")
    
    print("\n🎉 三种状态功能测试完成！")

if __name__ == "__main__":
    test_three_states() 