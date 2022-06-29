import math
import Info_student 

class StudentManagement:
    listStudent = []
    # Xây dựng 1 hàm tự động sinh ra mã học sinh
    def autogenous_ID(self):
        id = 1
        if (self.count_student() > 0):
            id = self.listStudent[0]._id
            for st in self.listStudent:
                if (id < st._id):
                    id = st._id
            id = id +1
        return id
    def count_student(self):
        return self.listStudent.__len__()
    def input_student(self):
        id_st = self.autogenous_ID()
        full_name_st = input("Nhập họ tên của học sinh: ")
        birthday_st = input("Nhập ngày tháng năm sinh của học sinh: ")
        sex_st = input("Nhập giới tính của học sinh: ")
        score_math_st = float(input("Nhập điểm môn toán của học sinh: "))
        score_literature_st = float(input("Nhập điểm môn văn của học sinh: "))
        score_english_st = float(input("Nhập điểm môn anh của học sinh: "))
        st = Info_student.Student(id_st,full_name_st,birthday_st,sex_st,score_math_st,score_english_st,score_literature_st)
        self.score_Avg(st)
        self.rank_score(st)
        self.listStudent.append(st)
    def score_Avg(self, st: Info_student.Student):
        scoreavg = (st._scoremath + st._scoreliterature + st._scoreenglish)/3
        st._scoreavg = math.ceil(scoreavg * 100) / 100
        
    def rank_score(self, st:Info_student.Student):
        if st._scoreavg < 5 and st._scoreavg >= 0:
            st._rankscore = "Yếu"
        elif st._scoreavg < 8 and st._scoreavg > 5:
            st._rankscore = "Trung bình"
        elif st._scoreavg > 8 and st._scoreavg <= 10:
            st._rankscore = "Tốt"
    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showStudent(self, listStudent):
        print(listStudent)
        print("\n")
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<18} {:<8} {:<8} {:<8} {:<8} {:<8}"
            .format("ID", "Ten", "Gioi tinh", "Ngay thang nam sinh", "Toan", "Van", "Anh", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if (listStudent.__len__() > 0):
            for st in listStudent:
                print("{:<8} {:<18} {:<8}  {:<18}  {:<8} {:<8} {:<8} {:<8} {:<8}"
                    .format(st._id, st._fullname, st._sex, st._birthdate, st._scoremath, st._scoreliterature, 
                            st._scoreenglish,st._scoreavg,st._rankscore))
        print("\n")

    def getListStudent(self):
        return self.listStudent       