#coding=utf8

'''
import random
#生成随机数列
for i in range(13):
    A.append(random.randint(0, 1000))
'''

class Node:#定好节点的属性
    def __init__(self, data=None, name=None, left=None, right=None, parent=None):
        self.data = data
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent

#==================================================================
class Baniry_search_tree:
    def __init__(self):
        self.root = None# 应该有一个根节点
        
    def add(self,node):
        if self.root == None:#检查根节点是否为空
            self.root = node  #填入根节点
        else:#根节点已经有数据了
            self._add(node, self.root)#使用_add函数向下增加数据
    
    def _add(self, node, current_node):
        if node.data < current_node.data:
            if current_node.left:
                self._add(node, current_node.left)
            else:
                node.parent = current_node
                current_node.left = node
                
        else:
            if current_node.right:
                self._add(node, current_node.right)
            else:
                node.parent = current_node
                current_node.right = node 
        
    
    
    def list_nodes(self):#遍历
        if self.root == None:
            print("树是空的")
        else:
            print("先序遍历")
            self.nodes = []
            self._pre_order_list(self.root)#先序遍历
            print(self.nodes)
            
            print("中序遍历")
            self.nodes = []
            self._in_order_list(self.root)#中序遍历,就是从小到大排序
            print(self.nodes)
            
            print("后序遍历")
            self.nodes = []
            self._last_order_list(self.root)#后序遍历
            print(self.nodes)
            
            print("层级遍历")
            self.nodes = []
            self._BFS_list(self.root)
            print(self.nodes)
            
    
    def _in_order_list(self, node):#中序遍历,递归查找
        temp = [None]*20
        top = -1
        while(top!=-1 or node!=None):
            if node != None:
                top = top + 1
                temp[top] = node
                node = node.left
            else:
                node = temp[top]
                top = top - 1
                self.nodes.append(node.data)
                node = node.right
            
    def _pre_order_list(self, node):#先序遍历,递归查找
        temp = [None]*20
        top = -1
        while(top!=-1 or node!=None):
            if node != None:
                self.nodes.append(node.data)
                if node.right != None:
                    top = top + 1
                    temp[top] = node.right
                node = node.left
            else:
                node = temp[top]
                top = top - 1
        
    def _last_order_list(self, node):#后序遍历,递归查找
        temp = [None]*20
        top = -1
        r = None
        while node or top!=-1:
            #if node:
             #   print(node.data)            
            if node:
                top = top + 1
                temp[top] = node
                node = node.left
            else:
                node = temp[top]
                if node.right and node.right!=r:
                    node = node.right
                    top = top + 1
                    temp[top] = node
                    node = node.left
                else:
                    node = temp[top]
                    top = top - 1
                    self.nodes.append(node.data)
                    r = node
                    node = None



    def _BFS_list(self, node):#层级遍历,广度优先搜索
        temp = []
        temp.append(node)
        rear = 1
        front = 0
        while rear != front:
            node = temp[front]
            front = front + 1
            self.nodes.append(node.data)
            if node.left:
                temp.append(node.left)
                rear = rear + 1
            if node.right:
                temp.append(node.right)
                rear = rear + 1




#随便一个数列,没有重复数字
A = [252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919]

def build_tree():        
    tree = Baniry_search_tree() #建立一个树的实体
    for i in range(len(A)):
        node = Node(data = A[i], name = i)#建立一个节点的实体
        tree.add(node)#将节点加入树中
    return tree


def test(tree):
    tree.list_nodes()#遍历


tree = build_tree()#建立一个树,加入节点
test(tree)