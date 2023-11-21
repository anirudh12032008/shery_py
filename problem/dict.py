# 49) Write a Python program to iterate over dictionaries using for loops
# def fun(d):
#     for i in d.items():
#         print(i)
# fun(d)


# 50) Write a Python script to merge two Python dictionaries.
# def fun(d1,d2):
#     d1.update(d2)
#     return d1


# 51) Write a Python program to sum all the values in a dictionary.
# def fun(d):
#     s = 0
#     for i in d.values():
#         s += i
#     return s
# fun(d)


# 52) Convert a list to dictionary 
# def fun(l):
#     d = dict()
#     for i in range(0,len(l)-1, 2):
#         d.update({l[i]:l[i+1]})
#     return d
# fun(l)


# 53) count the frequency of each elements 
# def fun(l):
#     d = dict()
#     for i in l:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# fun(l)


# 54) Write a Python program to combine two dictionary by adding values for common keys.
# def fun(d1,d2):
#     d = dict()
#     for i in d2:
#         if i in d1:
#             d1[i] += d2[i]
#         else:
#             d1[i] = d2[i]
#     return d1
# fun(d,d2)