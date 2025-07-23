"""
单词数据模型
"""
import json
import os
from typing import List, Dict, Optional
from datetime import datetime


class Word:
    """单词类"""
    
    def __init__(self, word: str, meaning: str, example: str = "", 
                 created_time: str = None, last_review: str = None, 
                 proficiency: int = 0, last_correct_date: str = None, 
                 last_practice_date: str = None):
        self.word = word.strip()
        self.meaning = meaning.strip()
        self.example = example.strip()
        self.created_time = created_time or datetime.now().isoformat()
        self.last_review = last_review
        self.proficiency = max(0, min(5, proficiency))  # 熟练度范围0-5
        self.last_correct_date = last_correct_date  # 最后答对日期
        self.last_practice_date = last_practice_date  # 最后练习日期
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'word': self.word,
            'meaning': self.meaning,
            'example': self.example,
            'created_time': self.created_time,
            'last_review': self.last_review,
            'proficiency': self.proficiency,
            'last_correct_date': self.last_correct_date,
            'last_practice_date': self.last_practice_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Word':
        """从字典创建单词对象"""
        return cls(
            word=data.get('word', ''),
            meaning=data.get('meaning', ''),
            example=data.get('example', ''),
            created_time=data.get('created_time'),
            last_review=data.get('last_review'),
            proficiency=data.get('proficiency', 0),
            last_correct_date=data.get('last_correct_date'),
            last_practice_date=data.get('last_practice_date')
        )
    
    def __str__(self) -> str:
        return f"{self.word} - {self.meaning}"
    
    def __repr__(self) -> str:
        return f"Word('{self.word}', '{self.meaning}')"


class WordManager:
    """单词管理器"""
    
    def __init__(self, data_file: str = "words.json"):
        self.data_file = data_file
        self.words: List[Word] = []
        self.load_words()
        # 如果单词列表为空，加载内置雅思词汇
        if len(self.words) == 0:
            self.load_builtin_ielts_words()
    
    def add_word(self, word: str, meaning: str, example: str = "") -> bool:
        """添加单词"""
        # 检查是否已存在
        if self.get_word(word):
            return False
        
        new_word = Word(word, meaning, example)
        self.words.append(new_word)
        self.save_words()
        return True
    
    def remove_word(self, word: str) -> bool:
        """删除单词"""
        for i, w in enumerate(self.words):
            if w.word.lower() == word.lower():
                del self.words[i]
                self.save_words()
                return True
        return False
    
    def get_word(self, word: str) -> Optional[Word]:
        """获取单词"""
        for w in self.words:
            if w.word.lower() == word.lower():
                return w
        return None
    
    def get_all_words(self) -> List[Word]:
        """获取所有单词"""
        return self.words.copy()
    
    def search_words(self, search_text: str) -> List[Word]:
        """搜索单词"""
        if not search_text:
            return self.words.copy()
        
        search_text = search_text.lower()
        results = []
        
        for word in self.words:
            if (search_text in word.word.lower() or 
                search_text in word.meaning.lower() or 
                search_text in word.example.lower()):
                results.append(word)
        
        return results
    
    def get_random_word(self) -> Optional[Word]:
        """获取随机单词"""
        import random
        studyable_words = self.get_studyable_words()
        if not studyable_words:
            return None
        return random.choice(studyable_words)
    
    def get_random_meanings(self, correct_meaning: str, count: int = 5) -> List[str]:
        """获取随机错误选项"""
        import random
        
        # 获取所有不同的中文含义
        all_meanings = list(set([w.meaning for w in self.words if w.meaning != correct_meaning]))
        
        # 如果错误选项不够，添加一些通用选项
        if len(all_meanings) < count:
            common_meanings = [
                "学习", "工作", "生活", "时间", "朋友", "家庭", "学校", "公司",
                "城市", "国家", "世界", "自然", "科技", "文化", "历史", "未来"
            ]
            all_meanings.extend(common_meanings)
        
        # 随机选择错误选项
        wrong_options = random.sample(all_meanings, min(count, len(all_meanings)))
        return wrong_options
    
    def update_review_time(self, word: str):
        """更新复习时间"""
        w = self.get_word(word)
        if w:
            w.last_review = datetime.now().isoformat()
            self.save_words()
    
    def increase_proficiency(self, word: str):
        """增加熟练度"""
        w = self.get_word(word)
        if w and w.proficiency < 5:
            w.proficiency += 1
            w.last_review = datetime.now().isoformat()
            # 更新最后答对日期为今天
            w.last_correct_date = datetime.now().strftime('%Y-%m-%d')
            # 更新最后练习日期为今天
            w.last_practice_date = datetime.now().strftime('%Y-%m-%d')
            self.save_words()
    
    def decrease_proficiency(self, word: str):
        """减少熟练度"""
        w = self.get_word(word)
        if w:
            if w.proficiency > 0:
                w.proficiency -= 1
            w.last_review = datetime.now().isoformat()
            # 更新最后练习日期为今天
            w.last_practice_date = datetime.now().strftime('%Y-%m-%d')
            self.save_words()
    
    def get_studyable_words(self) -> List[Word]:
        """获取可学习的单词（熟练度<5且一个月内未学习，且当天未练习）"""
        from datetime import datetime, timedelta
        
        current_time = datetime.now()
        one_month_ago = current_time - timedelta(days=30)
        today = current_time.strftime('%Y-%m-%d')
        
        studyable_words = []
        for word in self.words:
            # 检查是否当天已经练习过
            if word.last_practice_date == today:
                continue  # 当天已练习，跳过
            
            # 熟练度小于5的单词
            if word.proficiency < 5:
                studyable_words.append(word)
            # 熟练度为5但一个月内未学习的单词
            elif word.proficiency == 5 and word.last_review:
                try:
                    last_review_time = datetime.fromisoformat(word.last_review)
                    if last_review_time < one_month_ago:
                        studyable_words.append(word)
                except:
                    studyable_words.append(word)
        
        return studyable_words
    
    def load_words(self):
        """从文件加载单词"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.words = [Word.from_dict(item) for item in data]
            except Exception as e:
                print(f"加载单词数据失败: {e}")
                self.words = []
        else:
            self.words = []
    
    def save_words(self):
        """保存单词到文件"""
        try:
            data = [word.to_dict() for word in self.words]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存单词数据失败: {e}")
    
    def get_word_count(self) -> int:
        """获取单词总数"""
        return len(self.words)
    
    def get_today_correct_count(self) -> int:
        """获取今天已答对的单词数量"""
        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d')
        count = 0
        for word in self.words:
            if word.last_correct_date == today:
                count += 1
        return count
    
    def get_today_practice_count(self) -> int:
        """获取今天已练习的单词数量"""
        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d')
        count = 0
        for word in self.words:
            if word.last_practice_date == today:
                count += 1
        return count
    
    def get_today_wrong_count(self) -> int:
        """获取今天答错的单词数量"""
        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d')
        count = 0
        for word in self.words:
            if (word.last_practice_date == today and 
                word.last_correct_date != today):
                count += 1
        return count
    
    def load_builtin_ielts_words(self):
        """加载内置雅思高频词汇"""
        try:
            # 获取内置数据文件路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            ielts_file = os.path.join(project_root, "assets", "data", "ielts_1000_words.json")
            
            if os.path.exists(ielts_file):
                with open(ielts_file, 'r', encoding='utf-8') as f:
                    ielts_data = json.load(f)
                
                # 添加雅思词汇到单词列表
                for word_data in ielts_data:
                    word = Word.from_dict(word_data)
                    # 检查是否已存在（避免重复）
                    if not self.get_word(word.word):
                        self.words.append(word)
                
                # 保存到用户数据文件
                self.save_words()
                print(f"✅ 已加载 {len(ielts_data)} 个雅思高频词汇")
            else:
                print("⚠️ 雅思词汇数据文件不存在")
        except Exception as e:
            print(f"❌ 加载雅思词汇失败: {e}") 