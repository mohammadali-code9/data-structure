def BFS(graph , start):
    queue = [start]
    visited = {start}
    while queue:
        vertex = queue.pop(0)
        for ne in graph[vertex]:
            visited.add(ne)
            queue.append(ne)


    return visited

def DFS(graph , start , visited):
    visited[start] = True
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)

def sort1(A):
    B = [] *len(A)
    for i in range(len(A)):
        for j in range(1 , len(A)):
            if A[j] < min:
                min = A[j]
                k = j
        B[i] = min
        A[k] = float("inf")
    return B 

def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:

                A[j], A[j+1] = A[j+1] , A[j]          





# پیمایش عرضی گراف
def BFS(graph , start):
    queue = [start]
    visited = {start}

    while queue:
        vertex = queue.pop(0)

        for ne in graph[vertex]:
            if ne not in visited:      
                visited.add(ne)
                queue.append(ne)

    return visited


# پیمایش عمقی گراف (بازگشتی)
def DFS(graph , start , visited):
    visited[start] = True

    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)


# مرتب سازی انتخابی (نسخه شخصی)
def sort1(A):
    B = [None] * len(A)        

    for i in range(len(A)):
        m = float("inf")      
        k = -1

        for j in range(len(A)):
            if A[j] < m:
                m = A[j]
                k = j

        B[i] = m
        A[k] = float("inf")

    return B


# مرتب سازی حبابی
def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):   
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1] , A[j]
