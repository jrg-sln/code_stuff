


#include<stdio.h>
#include"node.c"
#include"read.c"
#include"print.h"

int main(){
	struct node n = read();
	print(n);
	return 1;
}
