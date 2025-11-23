# 單元 1：物件導向基礎（OOP）
# 程式範例 1：Student 類別基礎實作


class Student:
    """學生類別 - 用於管理學生資訊及成績"""

    def __init__(self, name, chinese_score, english_score, math_score):
        """
        初始化學生物件

        Args:
            name: 學生姓名
            chinese_score: 國文成績
            english_score: 英文成績
            math_score: 數學成績
        """
        self.name = name
        self.chinese_score = chinese_score
        self.english_score = english_score
        self.math_score = math_score

    def calculate_average(self):
        """計算平均分數"""
        total = self.chinese_score + self.english_score + self.math_score
        return total / 3

    def display_info(self):
        """顯示學生資訊"""
        avg = self.calculate_average()
        print(f"學生姓名: {self.name}")
        print(f"國文成績: {self.chinese_score}")
        print(f"英文成績: {self.english_score}")
        print(f"數學成績: {self.math_score}")
        print(f"平均分數: {avg:.2f}")
        print("-" * 30)


# 範例使用
if __name__ == "__main__":
    # 建立學生物件
    student1 = Student("小明", 85, 78, 92)
    student2 = Student("小紅", 88, 90, 85)
    student3 = Student("小王", 92, 87, 89)

    # 顯示學生資訊
    print("=== 學生成績資訊 ===\n")
    student1.display_info()
    student2.display_info()
    student3.display_info()
