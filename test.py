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
    try:
        n = int(input("Nhập số lượng học sinh của lớp: "))
        if n <= 0:
            exit()
    except:
        print("Bạn phải nhập vào là 1 số tự nhiên!")
        exit()
    self.a = []
    for i in range(n):
        self.a.append(input("Nhập tên thứ %d: " %(i+1)),self.autogenous_ID(i))
    return self.a
