#include "pch.h"
#include<stdlib.h>
#include<ctype.h>
#include<stdio.h>
 int isUsernameOK(char *name) {
	int i;
	while (isalpha(name[0]) == 0) {//第一个符号不是字母
		return -1;
		
	}
	+for (i = 0; name[i] != '\0'; i++)//非空字符就循环
		 {
		if (isalnum(name[i]) == 0)//包含了非字母或数字
			 {
			return -1;
			}
		}
	if (i < 9 || i>17) {//字符长度不符合要求
		return -1;
		
	}
	return 0;
	
}
 int  isPasswordOK(char* pwd)
 {
	 int len = 0;
	 int big = 0;
	 int num = 0;
	 if (pwd == NULL) {
		 return -1;

	 }
	 len = strlen(pwd);

	 if ((len < 8) || (len > 16))
	 {
		 return -1;
	 }
	 for (int i = 0; i < len; i++)
	 {
		 if (!isalnum(pwd[i]))
		 {
			 return -1;    //遇到非数字或者字符就返回 -1
		 }
		 if (isupper(pwd[i]))
		 {
			 big++;       //大写字母的个数
		 }
		 if (isdigit(pwd[i]))
		 {
			 num++;       //数字的个数
		 }
	 }
	 if ((big == 0) || (num == 0))
	 {
		 return -1;
	 }
	 return 0;
 }
 int gets_safe(char *str, size_t n)
	  {
	 int num = 0;
	 n = n - 1;
	 char ch;
	 if (str == 0)//缓冲区空
		  {
		 return -1;
		 }
	 printf("输入字符串\n");
	 while ((ch = getchar()) != '\n')//读到换行字符结束将前n-1个字符复制进buf里，后面的抛弃
		  {
		 if (ch == -1)//getchar返回错误
			  {
			 str[0] = 0;
			 return -2;
			 }
		 else {
			 if (num < n)
				  {
				 str[num] = ch;
				 num++;
				 }
			 
		 }
		 }
	 str[num] = '\0';
	 return num;
	 }
 int strcpy_safe(char* dest, size_t destsz, const char* src)
	  {
	 if (dest == 0)//dest不存在
		  {
		 return -1;
		 }
	 if (destsz == 0 || src == 0)//dest大小为0或src为空
		  {
		 return 0;
		 }
	 int n = 0;
	 destsz--;
	 while (n < destsz&&src[n] != '\0')//当读到src最后一个字符时或将dest填满了结束循环
		  {
		 dest[n] = src[n];
		 n++;
		 }
	 dest[n] = '\0';
	 return n;
	 }