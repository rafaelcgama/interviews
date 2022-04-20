# class Subject:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#
#     def set(self, name):
#         self._name = name
#
#     def get(self):
#         return self._name
#
#     name = property(get, set)
#
# test = Subject('name')
# test.name = 'porra'
# print(test.name)

# config = '$CONFIG_ROOT/tables/${DICTIONARY}/${LANGUAGE}.json'


# import re
# import os
#
# def substitute_enviroment_variables(path):
#     variables = find_variables(path)
#     # this generates a list of paris
#     for i in range(len(variables)):
#         variables[i] = [x for x in variables[i] if x != '']
#
#     for pattern, value in variables:
#         # need to backslash the $ otherwise no match
#         path = re.sub('\\' + pattern, os.getenv(value, '.'), path)
#
#     return path

# def f():
#     for i in range(3):
#         yield i
#
# result = []
# g = f()
# while True:
#     try:
#         result.append((next(g)))
#     except:
#         break
#
# print(result)

# words = ['apple', 'banana', 'grape', 'pear']
# print([w[0].upper() for w in words])

# print("{n:.2f}".format(n=3.142))
# # print("{:.2f}".format(**pi()))
# print("{:.2f}".format(3.142))
# print("%.2f" % 3.142)
# # print("{.2f}".format(3.142))

# class Example:
#     def example(self):
#         return self.test()
#
#     def test(self):
#         return "Example"
#
# class Test(Example):
#     def test(self):
#         return 'Test'

# Example1=Example()
# Example2=Test()
# print(Example1.example(),Example2.test())

# Example1 = Example()
# Example2 = Test()
# print(Example1.test(), Example2.test())

# print(test.Example(), test.test())
# print(Example.test(), Test.test())

# from functools import reduce
# print(reduce(lambda x, y: [y] + x, list(range(5)), []))

###
# def temp(t):
#     def celsius2fahrenheit(x):
#         return 9 * x / 5 + 32
#
#     temperature = "IT's " + str(celsius2fahrenheit(t)) + " degrees"
#
#     if (int(celsius2fahrenheit(t))) > 50 and int(celsius2fahrenheit(t)) < 100:
#         print ("HOT")
#
#     return temperature
#
# print(temp(20))

# before = [1, 2, 3, 4, 5]
#
# def bar(lst):
#     return lst.append(7)
#
# after = bar(before)
#
# print(before)
# print(after)

# class Tests(Exception):
#     pass
#
# class Topics(Tests):
#     pass
#
# class Points(Topics):
#     pass
#
# for cls in [Tests, Topics, Points]:
#     try:
#         raise cls()
#     except Tests:
#         print("Tests")
#     except Points:
#         print("Points")
#     except Topics:
#         print("Topics")

# class Services(object):
#    def __init__(self):
#       self.__testscore = 95
#
#    def getScore(self):
#       print(self.__testscore)
#
#    def setScore(self, testscore):
#       self.__testscore = testscore
#
# servicesscore = Services()
# servicesscore.getScore()
# servicesscore.setScore(100)
# servicesscore.getScore()
# print(servicesscore.__getScore)

# IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']
#
# temp = [tuple(map(int, ip.split("."))) for ip in IPlist]
# temp.sort(reverse=False)
# print([".".join(map(str, address)) for address in temp])
# IPlist.sort(key=lambda address: list(map(int, address.split('.'))))
# print(IPlist)
# tmp = [list(map(str, ip.split("."))) for ip in IPlist]
# tmp.sort()
# print([".".join(map(str, address)) for address in tmp])

# for address in range(len(IPlist)):
#     IPlist[address] = "%3s.%3s.%3s.%3s" % tuple(IPlist[address].split("."))
#     IPlist.sort(reverse=True)
#
# for address in range(len(IPlist)):
#     IPlist[address] = IPlist[address].replace(' ', '')
# print(IPlist)

# import re, datetime
# statement = "Python test will be released on 14-10-2019."
# # if (date:= re.findall(r'[\d]{1,2}-[\d]{1,2}-[\d]{4}', statement)):
# #     print(date)
#
# if (date:= re.findall(r'[\d]{1,2}-[\d]{1,2}-[\d]{4}', statement)):
#     print(date)

# result = list(filter(lambda l: l.startwswith("error: "), open("test.txt").readlines()))
# print(result)
# result = []
# phile = open("test.txt").read()
# for i in phile:
#     if i.startswith("error: "):
#         result.append(i)
# print(result)
# result = []
# for l in open("test.txt").read().split("\n"):
#     if l.startswith("error: "):
#         result.append(l)
# print(result)
# result = [l for l in open("test.txt") if l.startswith("error: ")]
# print(result)

# class Example1:
#     n = 2020
#
#     def foo(self):
#         return 'Hello Space'
#
# print(Example1.n)

# def f():
#     yield True
#
# try:
#     g = f()
#     h = next(g)
#     assert h is True
#     print("True")
#     h = next(g)
#     assert h is None
#     print("None")
# except AssertionError:
#     print("Assertion failed")
# except GeneratorExit:
#     print("Exit")
# except StopIteration:
#     print("Stop")

# vector = [[1,2],[3,4],[5,6],[7,8],[9,10]]
#
# print(list(( x for y in vector for x in y if x % 2 == 0 )))

# def sq(x):
#     return x * x
#
#
# def recursive_map(func, seq):
#     if seq == []:
#         return seq
#     else:
#         return [func(seq[0])] + recursive_map(func, seq[1:])
#
# print(recursive_map(sq, [1, 2, 3])) # CORRECT

# def recursive_map(func, seq):
#     if seq == []:
#         return seq
#     else:
#         return recursive_map(func, seq[1:] + [func(seq[0])])
#
# print(recursive_map(sq, [1, 2,3]))

# for n in range(2,10) :
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print(n)

# title = 'Python Programming'
# result = 65
#
# res_show = f'The course is titled {title} and my result is {result}'
# print(res_show)
#
# print(F'The course is titled {title} and my result is {result}')
#
# title = 'C++ Programming'
# result = 85
#
# print(res_show)

# i = 150
# j = 300
#
# if ((True == False) and (False in (False,))) == True:
#     print(i)
# elif (True == False) in (False,) == False:
#     print(j)
# else :
#     print("No arithmetical operator proceeded")

# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
#
# print(f(10, 20, 30, 40, e=50, f=60)) # Correct

# class Result(object):
#     def __init__(self, title):
#         self.title = title
#     def getTitle(self):
#         return self.title
#     def isCourse(self):
#         return False
#
# class Course(Result):
#     def isCourse(self):
#         return True
#
# var1 = Result("Passed:")
# print(var1.getTitle(), var1.isCourse())


# data = [1,2,3,4,5,6]
#
# def f1(x):
#     return 3 * x
#
# def f2(x):
#     try:
#         return x > 3
#     except:
#         return 0
#
#
# result = list(map(f1, list(filter(f2, data))))
# print(result)
#
# print(list(map(lambda r: r * 3, filter(lambda f: f>3 or 0, data))))
# print(list(map(lambda r: r * 3, filter(f2, data))))
# print([3*i for i in data if i > 3 else 0])
# string = "avsdbc"
# n = 3
#
# import random
# print(''.join(random.sample(string, n)))
# from string import *
#
# method = "METHODS"
#
#
# def x(methods):
#     method = str.swapcase(methods)
#     print(("%(method)s" % locals()))
#
#
# methods = str.swapcase(method[:-1])
# print(x(methods))

# class k:
#     def __init__(self):
#         self.__foo = 10
#     def methodX(self):
#         self.__methodY()
#         print(self.__foo)
#     def __methodY(self):
#         self.__foo += 1
# o = k()
#
# print(o.__foo)

# #-*- coding: UTF-8 -*-
# x = isinstance('34\xc2\xb0', str)
# y = 'abc'.encode().decode('ascii')
# z = "".join(['34\xb0', "56'", '12.63"', 'S'])
# w = "a" + "b"
# print(x, y, z, w)
