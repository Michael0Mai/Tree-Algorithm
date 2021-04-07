#coding=utf8

import binary_search_tree

class AVL_Node(binary_search_tree.Node):#定好节点的属性
    def __init__(self, data=None, name=None, left=None, right=None, parent=None, height = 1):
        self.data = data
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height#节点的高度,默认是1
        
class AVL_tree(binary_search_tree.Baniry_search_tree):#继承搜索二叉树
    #下面是改写的方法
    def __init__(self):
        self.root = None# 应该有一个根节点
        self.height = 0
    
    def get_height(self, node):# 算出一个节点的高度
        if self.root == None:#空的树度是0
            return 0
        else:
            node.height = self._get_height(node)#算一个节点的高度
            return node.height
            
    def _get_height(self, node):      
        if node.left != None:#判断有没有左孩子
            node.left_height = self.get_height(node.left)#递归算左孩子的高度
        else:
            node.left_height = 0#没有就返回0高度
        if node.right != None:
            node.right_height = self.get_height(node.right)
        else:
            node.right_height = 0
        return max( node.left_height,  node.right_height) + 1#节点的高度就是最高一个孩子的高度+1

    def add(self,node):
        if self.root == None:#检查根节点是否为空
            self.root = node  #填入根节点
        else:#根节点已经有数据了
            self._add(node, self.root)#使用_add函数向下增加数据,不管是否平衡,先插入节点
            print(node.data)
            self.balance(node)#平衡节点
        
    
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
                
    def balance(self, node):
        #判断节点是否平衡
        root_height = self.get_height(self.root)
        print(root_height)
        if root_height < 3:#什么也不需要旋转
            pass
        elif  root_height == 3 and (self.root.left == None or self.root.right) == None:#根节点需要旋转
            if self.root.left == node.parent and node.parent.left == node:#LL情况
                self.right_rotate(self.root)
            elif self.root.left == node.parent and node.parent.right == node:#LR情况
                self.left_rotate(node.parent)
                self.right_rotate(self.root)
            elif self.root.right == node.parent and node.parent.right == node:#RR情况
                self.left_ratate(self.root)
            else:#RL情况
                self.right_rotate(node.parent)
                self.left_ratate(self.root)
        
        else:#根节点不需要旋转
            lheight = self.get_height(node.parent.parent.parent)
            rheight = self.get_height(node.parent.parent.parent.parent.right)
            pass
            
    def right_rotate(self, node):
        #左孩子代替自己的位置,自己变成左孩子的右孩子
        node.left.parent = node.parent #左孩子的父节点
        if node.parent.left == node: #父结点的孩子
            node.parent.left = node.left
        else:
            node.parent.tight = node.left
        if node.left.right != None:
            node.left.right.parent = node
            node.left = node.left.right
     
    def left_rotate(self, node):
        #右孩子代替自己的位置,自己变成右孩子的左孩子   
        node.right.parent = node.parent
        if node.parent.left == node: #父结点的孩子
            node.parent.left = node.right
        else:
            node.parent.tight = node.right
        if node.left.right != None:
            node.right.left.parent = node
            node.left = node.right.left        


A = [252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919]

def build_tree():        
    tree = AVL_tree() #建立一个树的实体
    for i in range(len(A)):
        node = binary_search_tree.Node(data = A[i], name = i)#建立一个节点的实体
        tree.add(node)#将节点加入树中
    return tree
tree = build_tree()#建立一个树,加入节点

#tree.list_nodes()
