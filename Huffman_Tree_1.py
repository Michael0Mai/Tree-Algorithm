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
    
    def add(self,node):
        if self.root == None:#检查根节点是否为空
            self.root = node  #填入根节点
        else:#根节点已经有数据了
            print("树已经存在, 不能再添加") 
    
    def encode(self, node):#遍历
        if self.root == None:
            print("树是空的")
        else:
            if node != self.root:#根节点不用编码
                if node.parent.left == node:
                    node.code = node.parent.code + '0'  #左孩子的编码是父节点的编码加一个0
                else:
                    node.code = node.parent.code + '1'  #右孩子的编码是父节点的编码加一个1
                if node.is_leaf == True:# 记录叶节点的编码
                    self.codes[node.name] = node.code
            #递归
            if node.left != None:
                self.encode(node.left)
            if node.right != None:
                self.encode(node.right)  
    
    def show_codes(self):#显示编码
        for key, value in self.codes.items():
            print(key, value)            



#---------------------编码-------------------------------
def encode_text(text): #对一段字母编码 
    def count_letter(text):#统计字母出现的频率
        letter_count = {}
        for i in text:
            if i in letter_count.keys():
                letter_count[i] = letter_count[i] + 1
            else:
                letter_count[i] = 1
        return letter_count    
    
    def find_2_mini(nodes, nodes_2_mini):#权重找到最小的两个节点
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
    
    def build_huffman_tree(letter_count):#将节点连成huffman_tree
        nodes = []
        nodes_2_mini = []
        
        for key, value in letter_count.items():#读data_set,把里面的数据变成节点
            node = Node(name=key, data=value)
            nodes.append(node)
        
        while len(nodes)>1:    
            nodes, nodes_2_mini = find_2_mini(nodes, nodes_2_mini)#将权重最小的两个节点移到外面
            #将移到外面的节点连成一颗小的霍夫曼二叉树
            p_node = Node(name=nodes_2_mini[0].name+nodes_2_mini[1].name, 
                          data=nodes_2_mini[0].data+nodes_2_mini[1].data, 
                          left=nodes_2_mini[0], right=nodes_2_mini[1], is_leaf=False)#只有要编码的节点才是叶节点
            nodes_2_mini[0].parent = p_node
            nodes_2_mini[1].parent = p_node
            #把连好的树的根节点加回到原来节点的集合中
            nodes.append(p_node)
        return nodes[0]

    letter_count = count_letter(text)#统计字母出现的频率
    huffman_tree = Huffman_tree()#建立一个实体霍夫曼树
    tree = build_huffman_tree(letter_count)#将数据做成一颗符合要求的二叉树
    huffman_tree.add(tree)#将二叉树加入霍夫曼树中
    huffman_tree.encode(huffman_tree.root)#生成单个字母的编码
    
    encoded_codes = ""
    for letter in text:#利用单个字母的编码组合成一段字母的编码
        encoded_codes = encoded_codes + huffman_tree.codes[letter]    
    return huffman_tree.codes, encoded_codes#返回一个字典,里面是字母的编码 + 编号码的字符
 


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

#利用原有是霍夫曼树解码的方法,不写了

#===========================测试时间========================================


def test():
    #随便一个数列,没有重复数字
    text = "ABCDBDDCAHOPDCEQMNFGABEFGGDFBC"  
    
    #编码一段字母
    huffman_key, huffman_codes = encode_text(text)#获得编码和编码的字典
    print(text)
    print(huffman_codes)
    
    #解码
    decode_text = decode_huffman(huffman_key, huffman_codes)
    print(decode_text)
    
#test()
