#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 0
#define MaxSize 100

/*========================首先搞定树节点的结构=======================*/
typedef struct BiTreeNode{
    int data;
    struct BiTreeNode *left, *right;
} BiTree;


/*========================然后搞定栈的东西=======================*/
/*栈的顺序储存类型*/
#define StackMaxSize 50
typedef struct{
    BiTree *node[StackMaxSize];
    int top;
} SqStack;

/*初始化*/
void InitStack(SqStack S){
    S.top = -1;
}

/*判断空？*/
int StackEmpty(SqStack S){
    if(S.top == -1)
        return true;
    else
        return false;
}

/*进栈*/
void Push(SqStack S, BiTree *x){
    S.node[++S.top] = x;
    printf("%d\n", x->data);
}

/*出栈*/
BiTree *Pop(SqStack S){
    BiTree *x;
    x = S.node[S.top--];
    //printf("%d\n", x->data);
    return x;
}

/*=============================可以搞树的函数了========================*/
/*用来建立树的函数*/
void add(BiTree *node, BiTree *current_node){/*递归地将一个节点加入树中*/
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

BiTree *build(int n[]){
    //int len = sizeof(n) / sizeof(n[0]);
    int len = 16;
    BiTree *T, *temp;
    T = (BiTree *)malloc(sizeof(BiTree));
    T->data = n[0];
    T->left = NULL;
    T->right = NULL;
    for(int i=1;i<len;i++){
        BiTree *temp = (BiTree *)malloc(sizeof(BiTree));
        temp->data = n[i];
        temp->left = NULL;
        temp->right = NULL;
        add(temp, T);
    }
    return T;
}
    
  


/*中序遍历用的函数*/
void InOrder(BiTree *T){/*T是根节点，数据类型是BiTree*/
    SqStack S;
    InitStack(S);
    BiTree *p = T;/*p是一个节点，数据类型是BiTree*/
    while(p || StackEmpty(S)==false){
        printf("%d\n",p->data);
        if(p){
            Push(S, p);
            p = p->left;
            printf("push\n");
        }
        else{
            p = Pop(S);
            printf("%d\n", p->data);
            p = p->right;
            printf("pop\n");
        }
    }
}


int CalWPL(BiTree *p){ //计算叶节点在路径总权重，data为节点的权重
    int wpl = 0;
    int weights[MaxSize], levels[MaxSize];
    BiTree *Queue[MaxSize];
    int front = -1;
    int rear = -1;
    Queue[++rear] = p;
    levels[rear] = 1;
    weights[rear] = levels[rear] * p->data;
    while(front != rear){
        printf("%d\n", wpl);
        p = Queue[++front];
        if(p->left==NULL && p->right==NULL)
            wpl = wpl + weights[front];
        if(p->left!=NULL){
            Queue[++rear] = p->left;
            levels[rear] = levels[front] + 1;
            weights[rear] = levels[rear] * p->left->data + weights[front]; 
        }
        if(p->right!=NULL){
            Queue[++rear] = p->right;
            levels[rear] = levels[front] + 1;
            weights[rear] = levels[rear] * p->right->data + weights[front]; 
        }
    }
    return wpl;
}





/*准备好数据*/
int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};

/*===================正式开始============================*/
int main()
{
    BiTree *root = build(elem);
    printf("%d\n",root->left->left->left->data);
    InOrder(root);
    //int wpl = CalWPL(root);
    //printf("%d", wpl);
}

//[252, 229, 170, 3, 235, 924, 391, 375, 858, 808, 585, 458, 771, 818, 909, 919]