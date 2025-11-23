# 單元 1：物件導向基礎（OOP）
# 程式範例 2：使用多個物件和排序


class Student:
    """學生類別 - 用於管理學生資訊及成績"""

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

    def get_info_string(self):
        """取得學生資訊字串"""
        avg = self.calculate_average()
        return f"{self.name}: 平均分數 {avg:.2f}"


def create_students():
    """建立學生物件集合"""
    students = [
        Student("小明", 85, 78, 92),
        Student("小紅", 88, 90, 85),
        Student("小王", 92, 87, 89),
        Student("小李", 75, 82, 80),
        Student("小張", 90, 91, 88),
    ]
    return students


def display_all_students(students):
    """顯示所有學生資訊"""
    print("=== 所有學生成績 ===\n")
    for student in students:
        print(student.get_info_string())
    print()


def sort_by_average(students):
    """按平均分數排序（從高到低）"""
    return sorted(students, key=lambda s: s.calculate_average(), reverse=True)


def display_ranking(students):
    """顯示學生排行榜"""
    sorted_students = sort_by_average(students)
    print("=== 成績排行榜 ===\n")
    for rank, student in enumerate(sorted_students, 1):
        avg = student.calculate_average()
        print(f"第 {rank} 名: {student.name} - 平均分數 {avg:.2f}")
    print()


if __name__ == "__main__":
    # 建立學生物件
    students = create_students()

    # 顯示所有學生成績
    display_all_students(students)

    # 顯示排行榜
    display_ranking(students)
