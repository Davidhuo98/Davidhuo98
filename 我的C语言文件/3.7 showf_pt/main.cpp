//以两种方式显示float类型的值
#include<stdio.h>
int main(void)
{
    float about = 32000.0;
    double abet = 2.14e9;
    long double dip = 5.32e-5;

    printf("%f can be written %e\n", about, about);
    //下一行要求编译器C99或其中的相关特性
    printf("And it's %a in hexadecimal, powers of 2 notation\n ", about);
    printf("%f can be written %e\n",abet,abet);
    printf("%Lf can be written %Le\n", dip, dip);

    return 0;
}