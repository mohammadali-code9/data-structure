# ==============================
# Stack (Array Based)
# ==============================

class stack:
    def __init__(self, limit=1000):
        self.st = []
        self.lim = limit

    # درج در پشته
    def push(self, x):
        if len(self.st) >= self.lim:
            print("stack is full")
            return -1
        self.st.append(x)

    # حذف از پشته
    def pop(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st.pop()

    # مشاهده عنصر بالای پشته
    def peek(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st[-1]

    # ---------------------------------
    # "ایندکس(x) های درون پشته را برگرداند."
    def find(self, x):
        for i in range(len(self.st)):
            if self.st[i] == x:
                print(i)

    # ---------------------------------
    # "اولین شامل (x) را برگرداند"
    def find1(self, x):
        for i in range(len(self.st)):
            if self.st[i] == x:
                print(i)
                return

    # ---------------------------------
    # "اخرین ایندکس شامل (x) را چاپ کند"
    def find2(self, x):
        for i in range(len(self.st) - 1, -1, -1):
            if self.st[i] == x:
                print(i)
                return

    # ---------------------------------
    # چاپ آخرین ایندکس (نسخه ساده)
    def find2_n(self, x):
        p = -1
        for i in range(len(self.st)):
            if self.st[i] == x:
                p = i
        print(p)

    # ---------------------------------
    # چاپ n امین رخداد (اینجا سومین)
    def find2_n_third(self, x):
        idx_list = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                idx_list.append(i)

        if len(idx_list) >= 3:
            print(idx_list[2])
        else:
            print("not enough occurrences")

    # ---------------------------------
    # جایگزینی x با y
    def replace(self, x, y):
        for i in range(len(self.st)):
            if self.st[i] == x:
                self.st[i] = y


# ==============================
# Test
# ==============================

test = stack(10)
test.push(57)
test.push(126)
test.push(-10)
test.push(57)
test.push(57)

k = test.peek()

test.find(57)
test.find1(57)
test.find2(57)
test.find2_n(57)
test.find2_n_third(57)
test.replace(57, 999)

print(test.st)
