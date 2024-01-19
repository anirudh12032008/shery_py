l = [2, 96, 69, 77, 145, 20]
# 38) Accept List elements and reprint it
# def fun(l):
#   for i in l:
    #   print(i)



# 39) Print  List elements in reverse order
# def fun(l):
#   return(l[::-1])



# 40) Print positive and negative elements of an List
# def fun(l):
    # pos=[]
    # neg=[]
    # for i in l:
    #     if i>0:
    #         pos+= [i]
    #     else:
    #         neg+=[i]
    # return("Positive",pos, "Negative",neg) 
    
    
# 41) Print list in ascending or descending order
# def fun(l):
    # return(sorted(l),sorted(l,reverse=True))




# 42) Accept size n from user and create a n size List then take n inputs into the and finally 
#    Print the sum of all elements in the List in the following manner
#    10 + 20 + 30 = 60
# n = int(input())
# def fun(n):
    # items=[]
    # for _ in range(n):
    #     items+=[int(input())]
    # sum = 0
    # for i in items:
    #     sum = sum + i
    # return(sum)
    
    
    
# 43) Mean of List elements.
# def fun(l):
    # sum = 0
    # for i in l:
        # sum = sum + i
    # return(sum/len(l))




# 44) Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# def m(l):
#     max = l[0]
#     ind = 0
#     for i, e in enumerate(l):
#         if e>max:
#             max = e
#             ind = i
#     return f'Max element = {max} found at {ind} index'



# 45) Find the smallest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index
# def m(l):
#     min = l[0]
#     smin = l[0]
#     ind = 0
#     sind=0
#     for i, e in enumerate(l):
#         if e<min:
#             sind = ind
#             smin = min
#             min = e
#             ind = i
#         elif e<smin:
#             sind = i
#             smin = e
#     return f'Min element = {min} found at {ind} index and second min element = {smin} found at {sind} index'




# 46) Find the second greatest element 
#    {2, 96, 69, 77, 145, 20} = Second greatest element = 96
# def m(l):
#     max = l[0]
#     smax = l[0]
#     ind = 0
#     sind=0
#     for i, e in enumerate(l):
#         if e>max:
#             sind = ind
#             smax = max
#             max = e
#             ind = i
#         elif e>smax:
#             sind = i
#             smax = e
#     return f'Max element = {max} found at {ind} index and second max element = {smax} found at {sind} index'



# 47) Check if List is sorted or not.
# def sortedornot(l):
#     for i in range(len(l)-1):
#         if l[i+1]<l[i]:
#             return False
#     return True



# 48) Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]
# def fun1(l):
    # if l == l[::-1]:
    #     return("Pallindrom list")
    # else:
    #     return("Not a pallindrom list")
# def fun2(l):
#     for i in range((len(l)//2)):
#         if l[i] != l[-(i+1)]:
#             return False
#     return True




# BUBBLE SORT 
# 2nd try 
# def fun(l):
    # for j in range(len(l), 0, -1):
    #     for i in range(j-1):
    #         if l[i] > l[i+1]:
    #             l[i], l[i+1] = l[i+1], l[i]
    # return l