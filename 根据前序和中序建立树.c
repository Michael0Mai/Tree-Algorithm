#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 0
#define MaxSize 100

/*========================首先搞定树节点的结构=======================*/
typedef struct tree_node{
    int data;
    struct tree_node *left, *right;
}tree_node;

tree_node* build(int pre_order[], int in_order[], int pre_h, int pre_r, int in_h, int in_r){
    tree_node *root = (tree_node*)malloc(sizeof(tree_node));
    int i;
    root->data = pre_order[pre_h];
    for(i=in_h; in_order[i]!=root->data;i++);
    int left_len = i - in_h;
    int right_len = in_r - i;
    printf("%d\n", right_len);
    if(left_len){
        root->left = build(pre_order, in_order, pre_h+1, pre_h+left_len, in_h, in_h+left_len-1);
    }
    else{
        root->left = NULL;
    }
    if(right_len){
        root->right = build(pre_order, in_order, pre_r-left_len+1, pre_r, in_r-right_len+1, in_r);
    }
    else{
        root->right = NULL;
    }
    return root;
}

int pre_order[] = {252, 229, 170, 3, 235, 924, 391, 375, 858, 808, 585, 458, 771, 818, 909, 919};
int in_order[] = {3, 170, 229, 235, 252, 375, 391, 458, 585, 771, 808, 818, 858, 909, 919, 924};

void main(){
    int len, pre_h, pre_r, in_h, in_r;
    len = sizeof(pre_order) / sizeof(int);
    pre_h = 0;
    in_h = 0;
    pre_r = len-1;
    in_r = len - 1;
    tree_node *root = build(pre_order, in_order, pre_h, pre_r, in_h, in_r);
    printf("%d\n", root->data);
}