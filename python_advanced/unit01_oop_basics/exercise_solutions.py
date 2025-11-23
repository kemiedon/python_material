# 單元 1：物件導向基礎（OOP）
# 練習題解答

# 練習題 1：建立 Student 類別，包含三科成績與平均分數計算方法


class Student:
    """學生類別 - 包含三科成績與平均分數計算"""

    def __init__(self, name, chinese_score, english_score, math_score):
        """初始化學生物件"""
        self.name = name
        self.chinese_score = chinese_score
        self.english_score = english_score
        self.math_score = math_score

    def calculate_average(self):
        """計算平均分數"""
        total = self.chinese_score + self.english_score + self.math_score
        return total / 3

    def __str__(self):
        """字串表示"""
        avg = self.calculate_average()
        return f"{self.name}: 國文{self.chinese_score}, 英文{self.english_score}, 數學{self.math_score}, 平均{avg:.2f}"


# 練習題 2：設計「洗衣機」類別，包含「品牌」和「容量」兩個屬性


class WashingMachine:
    """洗衣機類別 - 包含品牌和容量屬性"""

    def __init__(self, brand, capacity):
        """
        初始化洗衣機物件

        Args:
            brand: 品牌名稱
            capacity: 容量（公斤）
        """
        self.brand = brand
        self.capacity = capacity

    def display_info(self):
        """顯示洗衣機資訊"""
        print(f"品牌: {self.brand}")
        print(f"容量: {self.capacity}kg")

    def __str__(self):
        """字串表示"""
        return f"{self.brand} 洗衣機 ({self.capacity}kg)"


# 測試代碼
if __name__ == "__main__":
    print("=== 練習題 1：Student 類別 ===\n")

    # 建立學生物件
    student1 = Student("小明", 85, 78, 92)
    student2 = Student("小紅", 88, 90, 85)

    print(student1)
    print(student2)

    print("\n=== 練習題 2：WashingMachine 類別 ===\n")

    # 建立洗衣機物件
    washing_machine1 = WashingMachine("LG", 8.0)
    washing_machine2 = WashingMachine("三星", 10.5)

    print(washing_machine1)
    washing_machine1.display_info()

    print()

    print(washing_machine2)
    washing_machine2.display_info()
