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

/*========================搞定计数的结构=======================*/
typedef struct child_num{
    int none, singal, dual;
}child_num;

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

BiTreeNode *build(int n[], int len){
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

child_num* build_count(){
    child_num *c;
    c = (child_num*)malloc(sizeof(child_num));
    c->dual = 0;
    c->none = 0;
    c->singal = 0;
    return c;
}
    

int count_child(BiTreeNode *root, child_num *c){
    if(root->left!=NULL && root->right!=NULL){
        c->dual++;
        count_child(root->left, c);
        count_child(root->right, c);
    }
    else if(root->left!=NULL && root->right==NULL){
        c->singal++;
        count_child(root->left, c);
    }
    else if(root->left==NULL && root->right!=NULL){
        c->singal++;
        count_child(root->right, c);
    }
    else{
        c->none++;
    }

}



/*准备好数据*/
int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};


void main(){
    int len;
    child_num *count;
    len = sizeof(elem) / sizeof(elem[0]);
    BiTreeNode *root = build(elem, len);
    count = build_count();
    count_child(root, count);
    printf("dual: %d\n", count->dual);
    printf("singal: %d\n", count->singal);
    printf("none: %d\n", count->none);
}