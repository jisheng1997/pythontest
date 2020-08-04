#!/usr/bin/python3

a = 10
b = 10.1
c = '10'
d = True

type(a) # <class 'int'>
type(b) # <class 'float'>
type(c) # <class 'str'>
type(d) # <class 'bool'>

isinstance(a, int) # True
isinstance(b, float) # True
isinstance(c, str) # True
isinstance(d, bool) # True
isinstance(a, (int, float, str, bool)) # True，只要是元祖中某一个类的实例就是True

# 继承
class A:
	pass

class B(A):
	pass

a = A()
b = B()

type(a) == A # True
type(b) == B # True
type(b) == A # False

isinstance(a, A) # True
isinstance(b, B) # True
isinstance(b, A) # False