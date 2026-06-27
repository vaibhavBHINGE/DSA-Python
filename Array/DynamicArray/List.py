import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # creates a c type of array size = self.size
        self.A = self.__make_Array(self.size)

    def __make_Array(self, capacity):
        # this code creates a c type array (static, referential) with size capacity
        return (capacity * ctypes.py_object)()

    # length of the array
    def __len__(self):
        return self.n

    # Appending an array
    def Append(self, item):
        if self.n == self.size:
            # resizing an array
            self.__resize(self.size * 2)  # while appending every time it will create its number size of an array
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        B = self.__make_Array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    # printing
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    # fetching using indexing
    # L = [12,13,vaibhav,29.21]
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "List out of bound error!"

    # adding pop
    def pop(self):
        if self.n == 0:
            return "Empty list!"
        print(self.A[self.n - 1])
        self.n -= 1
    #clear
    def clear(self):
        self.size=1
        self.n=0

    #find using values we are getting index of that value
    def find(self, value):
        for i in range(self.n):
            if self.A[i]==value:
                return i
        return "value error"
    #insert
    def insert(self,index,value):
        if self.n == self.size:
            # resizing an array
            self.__resize(self.size * 2)  # while appending every time it will create its number size of an array
        for i in range(self.n, index,-1):
            self.A[i]=self.A[i-1]
        self.A[index]=value
        self.n=self.n+1
    #delete using its index
    def __delitem__(self, index):
        if 
        for i in range(index,self.n-1):
            self.A[i]=self.A[i+1]
        self.n=self.n-1



L = MyList()

print("type of list: ", type(L))
L.Append(12)
L.Append(13)
L.Append("vaibhav")
L.Append(29.21)

# print(L)
print("length of the list: ", len(L))
print("printing list: ", L)
print("print element from index: ", L[0])
print("poping: ", L.pop())
L.Append("Bhinge")
print("printing list: ", L)
print("getting index number via value: ", L.find("Bhinge"))
print("inserting new item: ",L.insert(2,"ganesh"))
print("inserting new item: ",L.insert(2,"Amol"))
print("printing list: ", L)
print(del L[3])