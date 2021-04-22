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

typedef struct access{
    BiTreeNode *head, *p;
}access;

BiTreeNode* link_leaf(BiTreeNode *root, access *a){
    if(root != NULL){
        link_leaf(root->left , a);
        if(root->left==NULL && root->right==NULL){
            if(a->p == NULL){
                a->head = root;
                a->p = root;
            }
            else{
                a->p->right = root;
                a->p = root;
            }
        }
        link_leaf(root->right, a);
    }
    return a->head;
    
}



int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};

void main(){
    int len;
    BiTreeNode *root, *head;
    access *a;
    a = (access*)malloc(sizeof(access));
    a->head = NULL;
    a->p = NULL;
    len = sizeof(elem) / sizeof(elem[0]);
    root = build_tree(elem, len);
    head = link_leaf(root, a);
    while(head != NULL){
        printf("%d\n", head->data);
        head = head->right;
    }
}