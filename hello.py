# print('hello,world')

# age=input()
# age=int(age)
# if age >=18:
	# print('your age is ',age)
	# print('adult')
# elif age >40:
	# print('your age is ',age)
	# print('old')
# else:
	# print('your age is ',age)
	# print('not adult')
# names =['sb','sd','cd']
# for name in names:
	# print(name)
	
# sum=0
# for i in range(101):
	# sum=sum+i
# print(sum)
# sum=0
# i=99
# while i>0:
	# sum=sum+i
	# i=i-2
# print(sum)
# d={'1':'sb','2':'db','3':['a','6']}
#print(d['3'][1])
# print(d.get('4',4))
# def my_abs(x):
	# if x>=0:
		# return x
	# else:
		# return -x
# print(my_abs(-9))
# def my_abs(x):
	# if x>=0:
		# return x
	# else:
		# return -x
# def my_abss(x):
	# if not isinstance(x,(int,float)):
		# raise TypeError('bad operand type')
	# if x >= 0:
		# return x
	# else:
		# return -x
# def power(x,n):
	# s=1
	# while n>0:
		# n=n-1
		# s=s*x
	# return s
# print(power(3,3))
# def calc(numbers):
	# sum=0
	# for n in numbers:
		# sum=sum+n*n
	# return sum
# print(calc((1,2,3)))
# print(calc({1,2,3}))
# def calc(*numbers):
	# sum=0
	# for n in numbers:
		# sum=sum+n*n
	# return sum
# print(calc(1,2,3,4))
# nums=[2,3,4]
# print(calc(*nums))
# def person(name,age,**kw):
	# print('name:',name,'age:',age,'other:',kw)
# print(person('sb',30))
# print(person('sb',30,city='beijing'))
# extra={'city':'beijing','job':'engineer'}
# print(person('sb',30,city=extra['city'],job=extra['job']))
# print(person('sb',30,**extra))
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r=[]
# n=3
# for i in range(n):
	# r.append(L[i])
# print(r)
# print(range(5))
# for i in range(20):
	# print(i)
# L=tuple(range(100))
# print(L)
# print(L[0::3])

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
	# print(key)
# for value in d.values():
	# print(value)
# for k,v in d.items():
	# print(k,v)
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))
# for i,value in enumerate(['a','b','c']):
	# print(i,value)
# L=[]
# for i in list(range(11)):
	# L.append(i*i)
# print(L)
# L=[i*i for i in range(11) if i %2==0]
# print(L)
# print([m + n for m in 'ABC' for n in 'abc'])
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
	



	
