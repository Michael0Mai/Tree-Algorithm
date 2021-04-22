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

/*=====================搞一个盏节点=======================*/
typedef struct heap_node{
    BiTreeNode *data;
    int tag;
    struct heap_node *next;
}heap_node;

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

heap_node* build_heap(){
    heap_node *head;
    head = (heap_node*)malloc(sizeof(heap_node));
    head->data = NULL;
    head->next = NULL;
    return head;
}

void push(heap_node *head, BiTreeNode *p){
    heap_node *temp;
    temp = (heap_node*)malloc(sizeof(heap_node));
    temp->data = p;
    temp->next = head->next;
    head->next = temp;
}

BiTreeNode* pop(heap_node *head){
    BiTreeNode *temp;
    temp = head->next->data;
    head->next = head->next->next;
    return temp;
}

int is_heap_empty(heap_node *head){
    if(head->next == NULL){
        return true;
    }
    else{
        return false;
    }
}

void find_forefather(BiTreeNode *root, int x){
    heap_node *h, temp, *p = h->next;
    h = build_heap();
    while(root!=NULL || !is_heap_empty(h)){
        while(root!=NULL && root->data!=x){
            push(h, root);
            h->next->tag = 0;
            root = root->left;
        }
        if(root->data == x){
            printf("found");
            while(p != NULL){
                printf("%d\n", p->data->data);
                p = p->next;
            }
        }
        while(!is_heap_empty(h) && h->next->tag==1){
            pop(h);
        }
        if(!is_heap_empty(h)){
            h->next->tag = 1;
            root = h->next->data->right;
        }
    }
}


/*准备好数据*/
int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};


void main(){
    int len, x = 808;
    len = sizeof(elem) / sizeof(elem[0]);
    BiTreeNode *root = build_tree(elem, len);
    
    find_forefather(root, x);
    
}