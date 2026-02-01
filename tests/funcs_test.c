#include <stdio.h>
int main() {
    int func(void) { //function inside of another function test
    printf("test");
    }
    func();
    return 0;
}