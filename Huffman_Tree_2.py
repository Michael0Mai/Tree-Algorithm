#coding=utf8


class Node:#定好节点的属性
    def __init__(self, data=None, name=None, left=None, right=None, parent=None, is_leaf=True, code = ""):
        self.data = data
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.is_leaf = is_leaf
        self.code = code
        
class Huffman_tree():   
    def __init__(self):
        self.root = None# 应该有一个根节点
        self.codes = {}
    
    def encode(self, node):#遍历
        if self.root == None:
            print("树是空的")
        else:
            if node != self.root:#根节点不用编码
                if node.parent.left == node:
                    node.code = node.parent.code + '0'  #左孩子的编码是父节点的编码加一个0
                else:
                    node.code = node.parent.code + '1'  #右孩子的编码是父节点的编码加一个1
                if node.is_leaf == True:  # 记录叶节点的编码
                    self.codes[node.name] = node.code
            #递归
            if node.left != None:
                self.encode(node.left)
            if node.right != None:
                self.encode(node.right)  
    
    def show_codes(self):#显示编码
        for key, value in self.codes.items():
            print(key, value)  
        
    def encode_text(self, text): #对一段字母编码 
        if len(text) >= 2: #只有当要编码的字符串长度至少为2时,才需要编码
            self.build(text)
            self.encode(self.root)#生成单个字母的编码
            
            encoded_codes = ""
            for letter in text:#利用单个字母的编码组合成一段字母的编码
                encoded_codes = encoded_codes + self.codes[letter]  
        else: #当要编码的字符串长度1时,不需要编码
            self.codes = {text:0}
            encoded_codes = "0"
        return self.codes, encoded_codes #返回一个字典,里面是字母的编码 + 编号码的字符
    
    def count_letter(self, text):#统计字母出现的频率
        letter_count = {}
        for i in text:
            if i in letter_count.keys():
                letter_count[i] = letter_count[i] + 1
            else:
                letter_count[i] = 1
        return letter_count    
    
    def build(self, text):#将节点连成huffman_tree
        if self.root == None: #检查根节点是否为空
            nodes = [] #所有节点的集合
            nodes_2_mini = []
            letter_count = self.count_letter(text)#统计字母出现的频率
            
            for key, value in letter_count.items():#读data_set,把里面的数据变成节点
                node = Node(name=key, data=value, is_leaf=True)
                nodes.append(node)
            
            while len(nodes)>1:    
                nodes, nodes_2_mini = self.find_2_mini(nodes, nodes_2_mini)#将权重最小的两个节点移到外面
                #将移到外面的节点连成一颗小的霍夫曼二叉树
                p_node = Node(name=nodes_2_mini[0].name+nodes_2_mini[1].name, 
                              data=nodes_2_mini[0].data+nodes_2_mini[1].data, 
                              left=nodes_2_mini[0], right=nodes_2_mini[1], is_leaf=False)#只有要编码的节点才是叶节点
                nodes_2_mini[0].parent = p_node
                nodes_2_mini[1].parent = p_node
                #把连好的树的根节点加回到原来节点的集合中
                nodes.append(p_node)
            
            self.root = nodes[0]  #填入根节点
            
        else:#根节点已经有数据了
            print("树已经存在, 不能再添加")


    def find_2_mini(self, nodes, nodes_2_mini):#权重找到最小的两个节点
        nodes_2_mini = [nodes[0], nodes[1]]#随便取2个节点
        if nodes_2_mini[0].data > nodes_2_mini[1].data:#将两个节点排序
            nodes_2_mini[0], nodes_2_mini[1] = nodes_2_mini[1], nodes_2_mini[0]
            
        for i in range(2,len(nodes)):#找到整个节点集合的最小的2个节点
            if nodes[i].data > nodes_2_mini[1].data:
                pass
            elif nodes[i].data < nodes_2_mini[1].data and nodes[i].data >= nodes_2_mini[0].data:
                nodes_2_mini[1] = nodes[i]
            else:
                nodes_2_mini[1] = nodes_2_mini[0]
                nodes_2_mini[0] = nodes[i]    
        
        for i in nodes_2_mini:#从集合中移走2个最小的节点
            nodes.remove(i)
      
        return nodes, nodes_2_mini


#-------------------------------解码---------------------------------------------
def decode_huffman(huffman_key, huffman_codes):
    #查字典的方法
    decode_dict = {}
    decode_text = ""
    for key, value in huffman_key.items():#将编码的字典反过来
        decode_dict[value] = key
      
    i = 0
    while i < len(huffman_codes)-1:#找对应的编码规则
        temp = huffman_codes[i]
        while temp not in decode_dict.keys():#找不到就对加一个编码找
            i = i + 1
            temp = temp + huffman_codes[i]
        i = i + 1
        decode_text = decode_text + decode_dict[temp]
    
    return decode_text

#利用原有的霍夫曼树解码的方法,不写了

#===========================测试时间========================================

def test():
    #随便一个数列,没有重复数字
    text = "ABCDBDDCAHOPDCEQMNFGABEFGGDFBC" 
    text = "A" 
    
    #编码一段字母
    tree = Huffman_tree()
    tree.show_codes()
    
    huffman_key, huffman_codes = tree.encode_text(text)#获得编码和编码的字典
    
    print(text)
    print("长度: %d" %(len(text)*8))
    print(huffman_codes)
    print("长度: %d" %len(huffman_codes))
    print((len(huffman_codes)) / (len(text)*8))
    
    #解码
    decode_text = decode_huffman(huffman_key, huffman_codes)
    print(decode_text)
    
test()
