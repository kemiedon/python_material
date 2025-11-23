# 單元 2 OOP 進階 - 練習題解答

# ==================== 練習 1：基礎父類別設計 ====================
print("=" * 50)
print("練習 1：基礎父類別設計")
print("=" * 50)


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print(f"我是 {self.name}，學號是 {self.student_id}")


# 建立兩個學生實例
student1 = Student("小明", "S001")
student2 = Student("小花", "S002")

student1.show_info()
student2.show_info()


# ==================== 練習 2：子類別覆寫方法 ====================
print("\n" + "=" * 50)
print("練習 2：子類別覆寫方法")
print("=" * 50)


class BaseStudent:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print(f"我是 {self.name}，學號是 {self.student_id}")


class ComputerStudent(BaseStudent):
    def __init__(self, name, student_id, programming_language):
        super().__init__(name, student_id)
        self.programming_language = programming_language

    def show_info(self):
        print(f"我是 {self.name}，專長是 {self.programming_language}")


class EnglishStudent(BaseStudent):
    def __init__(self, name, student_id, language_level):
        super().__init__(name, student_id)
        self.language_level = language_level

    def show_info(self):
        print(f"我是 {self.name}，英文程度是 {self.language_level}")


# 建立不同科系的學生
comp_student = ComputerStudent("小明", "S001", "Python")
eng_student = EnglishStudent("小花", "S002", "Advanced")

comp_student.show_info()
eng_student.show_info()


# ==================== 練習 3：多型應用 ====================
print("\n" + "=" * 50)
print("練習 3：多型應用")
print("=" * 50)


class StudentBase:
    def __init__(self, name):
        self.name = name

    def demonstrate(self):
        print(f"{self.name} 進行演示")


class ComputerStudentDemo(StudentBase):
    def demonstrate(self):
        print(f"{self.name}展示了一個 Python 程式")


class EnglishStudentDemo(StudentBase):
    def demonstrate(self):
        print(f"{self.name}朗讀了一篇英文文章")


def student_showcase(students_list):
    """
    多型應用：接收學生清單，對每個學生呼叫 demonstrate() 方法
    不用管具體是什麼類型的學生，只要都有 demonstrate() 方法就行
    """
    for student in students_list:
        student.demonstrate()


# 建立包含不同科系學生的清單
students = [
    ComputerStudentDemo("小明"),
    EnglishStudentDemo("小花"),
    ComputerStudentDemo("大衛"),
]

# 進行學生成果分享
student_showcase(students)


# ==================== 練習 4：綜合應用 - 課程管理系統 ====================
print("\n" + "=" * 50)
print("練習 4：綜合應用 - 課程管理系統")
print("=" * 50)


class EnrollStudent:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name}選課 {course_name}：成功！")

    def get_courses(self):
        return self.courses


class ComputerEnrollStudent(EnrollStudent):
    ALLOWED_KEYWORDS = ["資訊", "程式", "Python", "Java", "資料結構"]

    def enroll_course(self, course_name):
        # 檢查課程是否適合資訊系
        if any(keyword in course_name for keyword in self.ALLOWED_KEYWORDS):
            super().enroll_course(course_name)
        else:
            print(f"{self.name}選課 {course_name}：此課程不適合資訊系")


class EnglishEnrollStudent(EnrollStudent):
    ALLOWED_KEYWORDS = ["英文", "英語", "文學", "莎士比亞"]

    def enroll_course(self, course_name):
        # 檢查課程是否適合英文系
        if any(keyword in course_name for keyword in self.ALLOWED_KEYWORDS):
            super().enroll_course(course_name)
        else:
            print(f"{self.name}選課 {course_name}：此課程不適合英文系")


# 建立小明（資訊系）
ming = ComputerEnrollStudent("小明")
ming.enroll_course("Python")  # 成功
ming.enroll_course("莎士比亞")  # 失敗
print(f"小明已修課程：{ming.get_courses()}\n")

# 建立小花（英文系）
xiaohui = EnglishEnrollStudent("小花")
xiaohui.enroll_course("英文文學")  # 成功
xiaohui.enroll_course("資料結構")  # 失敗
print(f"小花已修課程：{xiaohui.get_courses()}")
