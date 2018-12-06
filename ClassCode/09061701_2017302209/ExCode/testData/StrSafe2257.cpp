#include <ctype.h>
#include <iostream>
#include "StrSafe.h"
using namespace std;

int isUsernameOK(const char*name)
{
	char s;
	if (name == NULL)
		return -1;
	s = name[0];
	int element = 0;
	if (strlen(name) >= 8 && strlen(name) <= 16)   //长度合法
	{
		if (!isalpha(s))   //首位字母
		{
			return -1;
		}
		for (int i = 1; i < strlen(name); i++)
		{
			if (!isalnum(name[i])) //字母或数字
			{
				return -1;
			}
		}
		return 0;
	}
	else {
		return -1;
	}
}

	
int isPasswordOK(const char*pwd)
{
	int num=0,bigword=0;
	if (pwd == NULL)
		return -1;
	if (strlen(pwd) >= 8 && strlen(pwd) <= 16)   //长度合法
	{
		for (int i = 0; i < strlen(pwd); i++)
		{
			if (!isalnum(pwd[i]))
				return -1;
			if (isdigit(pwd[i]))
				num = 1;
			if (isupper(pwd[i]))
				bigword = 1;
		}
		if (bigword == 1 && num == 1)
			return 0;
	}
	return -1;
}

int gets_safe(char*str, rsize_t n)
// 从stdin读入用户输入，直到用户敲入Enter终止

//使用getchar()获取用户输入的单个字符，ferror函数测试读取错误
{

	char a;
	int i = 0;
	if (ferror(stdin))
		return -2;
	if (str == NULL || n == 0)
		return -1;
	while (a = getchar() != '\n')   //读入
	{
		str[i] = a;
		i++;
		if (i == n - 1)
		{
			break;
		}
	}
	if (i < n)
	{
		for (int j = i; j < n; j++)
		{
			str[j] = ' ';

		}
	}
	rewind(stdin);
	return i;
}

int strcpy_safe(char* dest, rsize_t destsz, const char* src)
{
	rsize_t length;
	if (!dest)
		return -1;
	if (!src || !destsz)
		return 0;
	length = strlen(src);
	if (length >= destsz)
	{
		for (rsize_t i = 0; i < destsz; i++)
		{
			dest[i] = src[i];
		}
		dest[destsz] = ' ';
		return destsz - 1;   
	}
	else
	{
		int i = 0;
		for (int i = 0; i < length; i++)
		{
			dest[i] = src[i];
		}
		for (rsize_t i = length; i < destsz; i++)
		{
			dest[i] = ' ';
		}
		return length;  
	}

}
