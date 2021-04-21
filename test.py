class Node:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.value = key
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def getLeft(self):
        return self.left_child
    def setLeft(self, value):
        self.left_child = value
    def getRight(self):
        return self.right_child
    def setRight(self, value):
        self.right_child = value


class root:
    def __init__(self):
        self.root = None

    def searchNode(self,key):
        cur = self.root
        while cur != None:
            if (key == cur):
                return cur
            elif (key < cur):
                cur = node.left_child
            else:
                cur = node.right_child #Right
        return None


    def insertNode(self,node):
        if (self.root == None):
            self.root = node
            node.left_child = None
            node.right_child = None
        else:
            cur = self.root
            while(cur != None):
                if (key < cur):
                    if(cur.left_child == None):
                        cur.left_child = node
                        cur = None
                    else:
                        cur = cur.left_child
                else:
                    if(cur.right_child = None):
                        cur.right_child = node
                        cur = None
                    else:
                        cur = cur.right_child
            node.left_child = None
            node.right_child = None



    def deleteNode(self,key):
        par = null
        cur = self.root
        while 
