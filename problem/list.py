l = [2, 96, 69, 77, 145, 20]
# 38) Accept List elements and reprint it
# for i in l:
    # print(i)

# 39) Print  List elements in reverse order
# print(l[::-1])

# 40) Print positive and negative elements of an List
# pos=[]
# neg=[]
# for i in l:
#     if i>0:
#         pos+= [i]
#     else:
#         neg+=[i]
# print("Positive",pos)
# print("Negative",neg)
# 41) Print list in ascending or descending order
# print(sorted(l))
# print(sorted(l,reverse=True))

# 42) Accept size n from user and create a n size List then take n inputs into the and finally 
#    Print the sum of all elements in the List in the following manner
#    10 + 20 + 30 = 60
# n = int(input())
# items=[]
# for _ in range(n):
#     items+=[int(input())]
# sum = 0
# for i in items:
#     sum = sum + i
# print(sum)
    
# 43) Mean of List elements.
# sum = 0
# for i in l:
    # sum = sum + i
# print(sum/len(l))

# 44) Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# max = sorted(l)[-1]
# print(f"Max element = {max} found at {l.index(max)} index")

# 45) Find the smallest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index
# min = sorted(l)[0]
# print(f"Min element = {min} found at {l.index(min)} index")

# 46) Find the second greatest element 
#    {2, 96, 69, 77, 145, 20} = Second greatest element = 96
# print(sorted(l)[-2])
# 47) Check if List is sorted or not.
# if l == sorted(l):
    # print("Sorted list")
# else:
    # print("The list is not sorted")
# 48) Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]
# if l == l[::-1]:
    # print("Pallindrom list")
# else:
    # print("Not a pallindrom list")
