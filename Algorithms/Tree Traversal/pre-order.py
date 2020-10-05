class Node:

    def __init__(self, d):

        self.left = None
        self.right = None
        self.d = d

    def insert(self, d):

        if self.d:
            if d < self.d:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)
            elif d > self.d:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.d = d

    def Print(self):
        if self.left:
            self.left.Print()
        print( self.d),
        if self.right:
            self.right.Print()


    def Preorder(self, r):
        res = []
        if r:
            res.append(r.d)
            res = res + self.Preorder(r.left)
            res = res + self.Preorder(r.right)
        return res

r = Node(26)
r.insert(13)
r.insert(34)
r.insert(19)
r.insert(18)
r.insert(30)
r.insert(41)
print(r.Preorder(r))
