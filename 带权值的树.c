#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 0
#define MaxSize 100

/*========================首先搞定树节点的结构=======================*/
typedef struct BiTreeNode{
    int data;
    struct BiTreeNode *left, *right;
} BiTreeNode;

/*=============================可以搞树的函数了========================*/
/*用来建立树的函数*/
void add(BiTreeNode *node, BiTreeNode *current_node){/*递归地将一个节点加入树中*/
    if(node->data < current_node->data){
        if(current_node->left)
            add(node, current_node->left);
        else{
            printf("left:%d\n", node->data);
            current_node->left = node;
        }
            
    }
    else{
        if(current_node->right)
            add(node, current_node->right);
        else{    
            current_node->right = node;
            printf("right:%d\n", node->data);
        }
    }
}  

BiTreeNode *build_tree(int n[], int len){
    BiTreeNode *T, *temp;
    T = (BiTreeNode*)malloc(sizeof(BiTreeNode));
    T->data = n[0];
    T->left = NULL;
    T->right = NULL;
    for(int i=1;i<len;i++){
        temp = (BiTreeNode*)malloc(sizeof(BiTreeNode));
        temp->data = n[i];
        temp->left = NULL;
        temp->right = NULL;
        add(temp, T);
    }
    return T;
}

int count_wpl(BiTreeNode *root){
    int in = 1, out = 0, wpl = 0;
    BiTreeNode *list[MaxSize];
    int level[MaxSize];
    list[out] = root;
    level[out] = 1;
    while(in != out){
        if(list[out]->left != NULL){
            list[in] = list[out]->left;
            level[in] = level[out]+1;
            in++;
        }
        if(list[out]->right != NULL){
            list[in] = list[out]->right;
            level[in] = level[out]+1;
            in++;
        }
        if(list[out]->left==NULL && list[out]->right==NULL){
            wpl = wpl + level[out] * list[out]->data;
        }
        out++;
    }
    return wpl;
}

int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};


void main(){
    int len, wpl_add;
    BiTreeNode *root;
    len = sizeof(elem) / sizeof(elem[0]);
    root = build_tree(elem, len);
    wpl_add = count_wpl(root);
    printf("%d", wpl_add);
}