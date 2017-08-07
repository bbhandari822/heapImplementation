#Binod Bhandari
#Drexel University 2017
#CS 260-002Summer 2017
# Assignment 5: heap.py

class heap:
    array = []

    def __init_(self):
        self.array = []

    def __str__(self):

        return self.array

    def makenull(self):
        self.array = []

    def insert(self, x):
        self.array.append (x)
        self.upheap (self.array.index (x))

    def parent(self, i):
        p = int((i - 1) / 2)
        return p

    def left(self, i):
        l = int((i + 1) * 2 - 1)
        return l

    def right(self, i):
        r = int((i + 1) * 2)
        return r

    def swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def upheap(self, i):

        p = self.parent(i)
        if self.array[i] < self.array[p]:
            self.swap(i, p)
            i = p
            self.upheap(i)
        else:
            return

    def downheap(self, i):

        if (self.left(i) < len(self.array)):
            l = self.array[self.left(i)]
        else:
            l = None

        if (self.right(i) < len(self.array)):
            r = self.array[self.right(i)]
        else:
            r = None

        if l and r:
            if l >= r:
                swap_nm = self.array.index(r)
                self.swap(i, swap_nm)
                self.downheap(swap_nm)
            else:
                swap_nm = self.array.index(l)
                self.swap(i, swap_nm)
                self.downheap(swap_nm)
        elif l:
            if (l < self.array[i]):
                swap_nm = self.array.index(l)
                self.swap(i, swap_nm)
                self.downheap(swap_nm)
        elif r:
            swap_nm = self.array.index(r)
            self.swap(i, swap_nm)
            self.downheap(swap_nm)
        else:
            return

    def min(self):
        if len(self.array) > 0:
            return self.array[0]

    def deletemin(self):
        if len (self.array) > 0:
            self.swap(0, len(self.array) - 1)
            self.array.pop()
            self.downheap(0)
        else:
            return

    def inorder(self,i):
        result = ""
        if i >= len(self.array):
            return ""
        result = result + self.inorder(self.left (i))
        result = result + " " + str (self.array[i])
        result = result + self.inorder(self.right (i))
        return result

    def preorder(self,i):
        result = ""
        if i >= len (self.array):
            return ""
        result = result + " " + str (self.array[i])
        result = result + self.preorder (self.left (i))
        result = result + self.preorder (self.right (i))
        return result

    def postorder(self, i):
        result = ""
        if i >= len (self.array):
            return ""
        result = result + self.postorder (self.left (i))
        result = result + self.postorder (self.right (i))
        result = result + " " + str (self.array[i])
        return result