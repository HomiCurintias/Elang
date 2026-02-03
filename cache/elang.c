#include <stdio.h>
#include <string.h>
int main(void) {
	char x []= "string";
	int y = 10;
	if (strcmp(x, x) != 0) {
	printf("test\n");
	}
	if (strcmp(x, "string") != 0) {
	printf("test2\n");
	}
	if (y == 10) {
	printf("test3\n");
	}
	else 
	{
	if (y > 9) {
	printf("67\n");
	}
	}

	return 0;
}