

# import math
# import os
# import random
# import re
# import sys




# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])

# matrix = []
# chars = [''] * (n*m)
# for i in range(n):
#     line = input()
#     for j in range(m):
#         chars[i+(j*n)] = line[j]
# code = ''.join(chars)
# # code = ''
# # for i in range(m):
# #     for index, elem in enumerate(matrix, start=m):
# #         if index% m==i:
# #             code+=elem

# regex = r"(?<=[A-Za-z0-9])([^0-9A-Za-z]+)(?=[A-Za-z0-9])"

# result = re.sub(regex,' ', code, 0, re.MULTILINE)

# print(result.strip())
import re
p,q =map(int,(input().split()))
a,b = [],""
for _ in range(p):
    a.append(input())
    
for z in zip(*a):
    b +="".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)"," ",b))


# import math
# import os
# import random
# import re
# import sys


# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])

# matrix = []

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

# encoded_string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
# pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
# print(re.sub(pat,' ',encoded_string))
