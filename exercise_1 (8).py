# ==============================
# Simple Queue (Array Based)
# ==============================

class Queue:
    def __init__(self , max = 100):
        # ایجاد آرایه با اندازه ثابت
        self.list = [None] * max
        self.front = -1
        self.rear = -1

    # درج در صف
    def insert(self, x):
        # بررسی پر بودن صف
        if self.rear >= len(self.list) - 1:
            print("Queue is Full")
            return

        # اولین درج
        if self.front == -1:
            self.front += 1
            self.rear += 1
            self.list[self.rear] = x
            return

        # درج معمولی
        self.rear += 1
        self.list[self.rear] = x

    # حذف از صف
    def Del(self):
        # بررسی خالی بودن
        if self.front == -1:
            print("Queue is empty")
            return

        # اگر فقط یک عنصر باشد
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k

        # حذف معمولی
        k = self.list[self.front]
        self.front += 1
        return k


# تست صف ساده
test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39)  # Queue is Full
test.Del()
test.insert(39)  # الان جا دارد


# ==============================
# Circular Queue
# ==============================

class C_Queue:
    def __init__(self, max):
        # ایجاد آرایه دایره‌ای
        self.list = [None] * max
        self.front = -1
        self.rear = -1

    # درج در صف دایره‌ای
    def insert(self, x):
        if (self.rear + 1) % len(self.list) == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return

        self.rear = (self.rear + 1) % len(self.list)
        self.list[self.rear] = x

    # حذف از صف دایره‌ای
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return

        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k

        k = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)
        return k

    # بررسی خالی بودن
    def is_empty(self):
        return self.front == -1

    # بررسی پر بودن
    def is_full(self):
        return (self.rear + 1) % len(self.list) == self.front
