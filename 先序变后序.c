#include <stdio.h>
#include <stdlib.h>
/*将满二叉树的先序序列变成后续序列*/

void _PreToPost(int pre[], int lh, int lr, int rh, int rr){
    if(rh-lh>0){
        int p = pre[lh-1];
        for(int i=lh-1; i<rr; i++)
            pre[i] = pre[i+1];
        pre[rr] = p;
        _PreToPost(pre, lh,(lr+lh)/2 -1, (lr+lh)/2, lr-1);
        _PreToPost(pre, rh,(rr+rh)/2 -1, (rr+rh)/2, rr-1);
    }
    
}
void PreToPost(int pre[], int len_pre){
    int midle =(len_pre+1) / 2;
    int lh = 1;
    int lr = midle -1 ;
    int rh = midle;
    int rr = len_pre-1;
    _PreToPost(pre, lh, lr, rh, rr);
}


int main(){
int pre[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};

PreToPost(pre, 15);
for(int i=0; i<15;i++)
    printf("%d \n",pre[i]);

}