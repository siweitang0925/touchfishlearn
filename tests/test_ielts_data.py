"""
测试雅思词汇数据加载功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.word_model import WordManager

def test_ielts_data_loading():
    """测试雅思词汇数据加载"""
    print("=== 测试雅思词汇数据加载 ===")
    
    # 创建单词管理器
    word_manager = WordManager()
    
    print(f"📊 当前单词总数: {word_manager.get_word_count()}")
    
    if word_manager.get_word_count() > 0:
        print("✅ 雅思词汇加载成功！")
        print("\n📋 前10个雅思词汇预览:")
        for i, word in enumerate(word_manager.words[:10]):
            print(f"   {i+1}. {word.word} - {word.meaning}")
            print(f"      例句: {word.example}")
        
        print(f"\n📈 统计信息:")
        print(f"   总单词数: {word_manager.get_word_count()}")
        print(f"   可学习数: {len(word_manager.get_studyable_words())}")
        print(f"   今日已答对: {word_manager.get_today_correct_count()}")
        print(f"   今日答错: {word_manager.get_today_wrong_count()}")
        
        # 测试搜索功能
        print(f"\n🔍 搜索测试:")
        search_results = word_manager.search_words("academic")
        print(f"   搜索 'academic': 找到 {len(search_results)} 个结果")
        if search_results:
            print(f"   结果: {search_results[0].word} - {search_results[0].meaning}")
        
        # 测试随机单词
        random_word = word_manager.get_random_word()
        if random_word:
            print(f"\n🎲 随机单词测试:")
            print(f"   随机单词: {random_word.word} - {random_word.meaning}")
            
            # 测试选项生成
            meanings = word_manager.get_random_meanings(random_word.meaning, 5)
            print(f"   选项: {meanings}")
    else:
        print("❌ 雅思词汇加载失败")
        print("请检查 assets/data/ielts_1000_words.json 文件是否存在")

if __name__ == "__main__":
    test_ielts_data_loading() 