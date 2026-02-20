class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list :
    def __init__(self):
        self.head = None
    def del_after(self , x):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next :
                    a = c.next
                    c.next = a.next
                    if a.next:
                        a.next.back = c
                    del a
                    return
                print("error 1")
                return
            c = c.next
            print("not found")
    def del_x(self , x):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.del_last()
                    return
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c = c.next
            print("not found")





#یا به صورت زیر

class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list:
    def __init__(self):
        self.head = None

    # حذف نود بعد از مقدار x
    def del_after(self , x):
        if self.head is None:
            print("error")
            return
        
        c = self.head
        while c:
            if c.Data == x:
                if c.next:
                    a = c.next
                    c.next = a.next
                    if a.next:
                        a.next.back = c
                    del a
                    return
                print("error 1")
                return
            c = c.next
        
        print("not found")

    # حذف نود با مقدار x
    def del_x(self , x):
        if self.head is None:
            print("error")
            return
        
        c = self.head
        while c:
            if c.Data == x:
                # اگر نود اول باشد
                if c.back is None:
                    self.head = c.next
                    if self.head:
                        self.head.back = None
                    del c
                    return
                
                # اگر نود آخر باشد
                if c.next is None:
                    c.back.next = None
                    del c
                    return
                
                # نود وسط
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            
            c = c.next
        
        print("not found")
            
