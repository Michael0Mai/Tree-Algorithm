#coding=utf8


class Node:#定好节点的属性
    def __init__(self, data=None, name=None, left=None, right=None, parent=None, height = 1):
        self.data = data
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height#节点的高度,默认是1
        
        
class AVL_tree:
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
        
    def get(self, value):#查找一个值
        if self.root == None:#先判断有没有根节点
            return None
        else:#从根节点开始搜索
            result = self._get(value, self.root)
            if result == None:
                print("找不到节点 %s" %value)
            return result
        
    def _get(self, value, current_node):
        if current_node == None:#找不到节点
            return None
        elif value == current_node.data:#找到了
            return current_node
        elif value < current_node.data:#向左边找
            if current_node.left == None:#判断有没有左孩子
                return None
            else:
                return self._get(value, current_node.left)
        else:#向右边找
            if current_node.right == None:#判断有没有右孩子
                return None    
            else:
                return self._get(value, current_node.right)
        
    def delete(self, value):
        if value == self.root.data:#检查要删除的节点是不是根节点
            if self.root.left == None and self.root.right == None:#检查根节点还有没有孩子
                self.root = None #清空整棵树
                print("成功清空根节点!!")
            else:#根节点有孩子,调用删除_delete(self, node)
                self._delete(self.root)
        else:#不是根节点就向下查找
            node_to_remove  = self.get(value) #根据值找节点
            if node_to_remove == None:#找不到
                return None 
            else:#找到了
                self._delete(node_to_remove)#删除
            
    def _delete(self, node):
        if node.left==None and node.right==None: #是叶节点
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            node.parent = None
            print("成功删除叶节点 %s" %node.data)
        elif node.left!=None and node.right==None:  #只有左节点
            if node != self.root:#要删除的节点不是根节点
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:#要删除的节点是根节点
                self.root = node.left
            node.parent = None
            node.left = None            
            print("成功删除节点 %s" %node.data)
        elif node.left==None and node.right!=None:  #只有右节点
            if node != self.root:#要删除的节点不是根节点
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else :#要删除的节点是根节点
                self.root = node.right
            node.parent = None
            node.right = None   
            print("成功删除节点 %s" %node.data)
        else:   #左右都有节点
            '''选择和删除节点最接近的节点代替被删除节点,可以用左子树最大的或右子树最小的'''
            nearest  = self.find_min(node.right)#找到最接近的节点
            if nearest.parent.left == nearest:#如果最接近的节点是左孩子
                if nearest.right != None:#如果最接近的节点有孩子
                    nearest.right.parent = nearest.parent
                    nearest.parent.right = nearest.right
                nearest.parent.left = None
                nearest.left = node.left
                nearest.right = node.right  
            if node != self.root:#要删除的节点不是根节点
                nearest.parant = node.parent
                if node.parent.left == node:#判断要删除的节点是左孩子还是右孩子
                    node.parent.left = nearest
                else:
                    node.parent.right = nearest
                node.left = None
                node.right = None
                print("成功删除节点 %s" %node.data)
            else:#要删除的节点是根节点
                nearest.parant = None
                self.root = nearest
                node.left = None
                node.right = None 
                print("成功删除原来根节点 %s!!" %node.data)
                print("新的根节点 %s!!" %self.root.data)
                
    def find_min(self, node):#找最小值
        temp = node
        while temp.left != None:
            temp = temp.left
        return temp
    
    def find_max(self, node):#找最大值
        temp = node
        while temp.right != None:
            temp = temp.right
        return temp    
    
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
            
    
    def _pre_order_list(self, node):#先序遍历,递归查找
        self.nodes.append(node.data)#注意这句的位置
        if node.left != None:
            self._pre_order_list(node.left)
        if node.right != None:
            self._pre_order_list(node.right)  
    
    def _in_order_list(self, node):#中序遍历,递归查找
        if node.left != None:
            self._in_order_list(node.left)
        self.nodes.append(node.data)#注意这句的位置
        if node.right != None:
            self._in_order_list(node.right)        
        
    def _last_order_list(self, node):#后序遍历,递归查找
        if node.left != None:
            self._last_order_list(node.left)
        if node.right != None:
            self._last_order_list(node.right)   

        self.nodes.append(node.data)#注意这句的位置


        
#随便一个数列,没有重复数字
A = [252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919]

def build_tree():        
    tree = AVL_tree() #建立一个树的实体
    for i in range(len(A)):
        node = Node(data = A[i], name = i)#建立一个节点的实体
        tree.add(node)#将节点加入树中
    return tree
tree = build_tree()#建立一个树,加入节点


#==========================测试专区=================
node = tree.find_max(tree.root)
print(tree.get_height(tree.root))
print(tree.root.height)
print(tree.root.left.height)

