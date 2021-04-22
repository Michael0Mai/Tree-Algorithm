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
            //printf("left:%d\n", node->data);
            current_node->left = node;
        }
            
    }
    else{
        if(current_node->right)
            add(node, current_node->right);
        else{    
            current_node->right = node;
            //printf("right:%d\n", node->data);
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

/*搞一个队列的节点*/
typedef struct queue_node{
    BiTreeNode *node_point;
    struct queue_node *next;
}queue_node;

/*搞一个队列*/
typedef struct queue{
    queue_node *front, *rear, *head;
}queue;

/*建一个队列*/
queue* build_queue(){
    queue *Q;
    Q = (queue*)malloc(sizeof(queue));
    queue_node *temp;
    temp = (queue_node*)malloc(sizeof(queue_node));
    Q->head = temp;
    Q->head->node_point = NULL;
    Q->head->next = NULL;
    Q->front = Q->head;
    Q->rear = Q->head;
    return Q;
}


void en_queue(queue *q, queue_node *n){
    q->rear->next = n;
    q->rear = n;
}

queue_node* de_queue(queue *q){
    queue_node *n;
    q->front = q->front->next;
    n = q->front;
    return n;
}

int queue_empty(queue *q){
    if(q->front == q->rear){
        return true;
    }
    else{
        return false;
    }
}

int is_complete(BiTreeNode *root){
    int c = 0;
    if(root == NULL){
        return 0;
    }
    else{
        BiTreeNode *p = root;
        queue_node *qn, *temp;
        queue *Q;
        int level;
        Q = build_queue();
        qn = (queue_node*)malloc(sizeof(queue_node));
        qn->node_point = p;
        qn->next = NULL;
        en_queue(Q, qn);
        while(!queue_empty(Q)){
            printf("c: %d\n", c);
            temp = de_queue(Q);
            if(temp->node_point->left != NULL){
                if(c == 1){
                    return 0;
                }
                qn = (queue_node*)malloc(sizeof(queue_node));
                qn->node_point = temp->node_point->left;
                qn->next = NULL;
                en_queue(Q, qn);
            }
            else{
                c = 1;
            }
            if(temp->node_point->right!=NULL){
                if(c == 1){
                    return 0;
                }
                qn = (queue_node*)malloc(sizeof(queue_node));
                qn->node_point = temp->node_point->right;
                qn->next = NULL;
                en_queue(Q, qn);
            }
            else{
                c = 1;
            }
        }
        return 1;
    }
}



/*准备好数据*/
int elem[] = {252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919};


void main(){
    int complete, len;
    len = sizeof(elem) / sizeof(elem[0]);
    BiTreeNode *root = build(elem, len);
    complete = is_complete(root);
    printf("complete: %d\n", complete);
}