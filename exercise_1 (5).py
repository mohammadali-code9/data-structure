class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list:
    def __init__(self):
        self.head = None

    # درج در ابتدا
    def ins_frist(self , x):
        if self.head is None:
            self.head = dnode(x)
            return
        a = dnode(x)
        a.next = self.head
        self.head.back = a
        self.head = a

    # درج در انتها
    def ins_last(self , x):
        if self.head is None:
            self.ins_frist(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = dnode(x)
        c.next = a
        a.back = c

    # درج بعد از مقدار x
    def ins_after(self , x , y):
        if self.head is None:
            print("error")
            return
        
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.ins_last(y)
                    return
                a = dnode(y)
                a.next = c.next
                a.back = c
                c.next.back = a
                c.next = a
                return
            c = c.next
        
        print("not found")

    # درج قبل از مقدار x
    def ins_befor(self , x , y):
        if self.head is None:
            print("error")
            return
        
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.ins_frist(y)
                    return
                a = dnode(y)
                a.next = c
                a.back = c.back
                c.back.next = a
                c.back = a
                return
            c = c.next
        
        print("not found")

    # حذف اول
    def del_first(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        self.head = c.next
        if self.head:
            self.head.back = None
        del c

    # حذف آخر
    def del_last(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.del_first()
            return
        c.back.next = None
        del c

    # حذف قبل از x
    def del_befor(self , x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            print("error")
            return
        
        c = self.head
        while c:
            if c.Data == x:
                a = c.back
                if a.back:
                    a.back.next = c
                    c.back = a.back
                else:
                    self.head = c
                    c.back = None
                del a
                return
            c = c.next
        
        print("x not found")

    # نمایش لیست
    def display(self):
        c = self.head
        while c:
            print(c.Data , end=" <-> ")
            c = c.next
        print("None")
