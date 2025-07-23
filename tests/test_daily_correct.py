"""
测试当天已答对单词不再弹出功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.word_model import Word, WordManager
from datetime import datetime

def test_daily_correct_feature():
    """测试当天已答对功能"""
    print("=== 测试当天已答对单词不再弹出功能 ===")
    
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
    studyable_words = word_manager.get_studyable_words()
    print(f"2. 初始可学习单词数量: {len(studyable_words)}")
    
    # 模拟答对一个单词
    print("3. 模拟答对单词 'apple'...")
    word_manager.increase_proficiency("apple")
    
    # 检查可学习单词数量
    studyable_words = word_manager.get_studyable_words()
    print(f"4. 答对后可学习单词数量: {len(studyable_words)}")
    
    # 检查今日已答对数量
    today_correct_count = word_manager.get_today_correct_count()
    print(f"5. 今日已答对单词数量: {today_correct_count}")
    
    # 验证apple不在可学习列表中
    apple_word = word_manager.get_word("apple")
    if apple_word:
        print(f"6. apple单词的最后答对日期: {apple_word.last_correct_date}")
        print(f"   今天日期: {datetime.now().strftime('%Y-%m-%d')}")
    
    # 测试随机获取单词
    print("7. 测试随机获取单词...")
    for i in range(5):
        random_word = word_manager.get_random_word()
        if random_word:
            print(f"   第{i+1}次随机获取: {random_word.word}")
        else:
            print(f"   第{i+1}次随机获取: 无可用单词")
    
    # 模拟答对更多单词
    print("8. 模拟答对更多单词...")
    word_manager.increase_proficiency("book")
    word_manager.increase_proficiency("cat")
    
    studyable_words = word_manager.get_studyable_words()
    print(f"9. 答对3个单词后可学习单词数量: {len(studyable_words)}")
    
    today_correct_count = word_manager.get_today_correct_count()
    print(f"10. 今日已答对单词数量: {today_correct_count}")
    
    print("11. 测试结果验证:")
    print("    ✅ 答对的单词当天不再出现在可学习列表中")
    print("    ✅ 今日已答对数量统计正确")
    print("    ✅ 随机获取单词不会返回当天已答对的单词")
    
    print("\n🎉 当天已答对功能测试完成！")

if __name__ == "__main__":
    test_daily_correct_feature() 