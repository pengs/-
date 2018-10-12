#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
作业
1. 编程实现对一个元素全为数字的列表，求最大值、最小值

2. 编写程序，完成以下要求：
	统计字符串中，各个字符的个数
	比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

3. 编写程序，完成以下要求：
	完成一个路径的组装
	先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share

4. 编写程序，完成“名片管理器”项目
	需要完成的基本功能：
		添加名片
		删除名片
		修改名片
		查询名片
		退出系统
	程序运行后，除非选择退出系统，否则重复执行功能
'''

# 1、列表是纯数字，求最大值和最小值
ls=[1,2,3,4,5,6]
print("列表的最大值:",max(ls))
print("列表的最小值:",min(ls))

# 2、(1)统计字符串，各个字符的个数
s="I like you,I love you！Laotie Double click 666!"
result=0
for i in s:
	if (ord(i)>97 and ord(i)<123) or (ord(i)>65 and ord(i)<91):
		result+=1
print("字符串统计后出现字母个数为:%d个"%result)	

result1=0
for i in s:
	if i in  '0123456789':
		result1+=1
print("字符串统计后出现数字的个数为:%d个"%result1)	

print("此字符串出现非字母和数字的个数为:%d个"%(len(s)-result-result1))	
	
# 2、(2)比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
#通过程序计算统计
s="hello world"
d={}
for i in s:
	d[i]=s.count(i)
print("字符串统计的结果为: ",d)	

# 第二种方法 
s1="hello world"
d1={}
for i in s1:
	if not i in d1:
		d1[i]=1
	else:	
		d1[i]+=1
print("字符串统计的结果为: ",d1)	


# 内置函数
from  collections import Counter
c = Counter()  # Counter 是一个简单的计数器，例如，统计字符出现的个数：
s3 = "hello world"
for i in s3:
	c[i] += 1
print("字符串统计的结果为: ",c)

