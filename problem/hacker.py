# # def print_rangoli(size):
# #     alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# #     use = alpha[0:size]
# #     def mid(size):
# #         m = []
# #         for i in range(size):
# #             m.insert(0,alpha[i])
# #             m.insert(-1,alpha[i])
# #         m.pop()
# #         global main ,main2
# #         main = m.copy()
# #         main2 = m.copy()
# #         m = '-'.join(m)
# #         return m
# #     midline = mid(size)
# #     def down(size):
# #         width = len(midline)
# #         for i in range(size-1):
# #             line = []
# #             c = main.count(alpha[i])
# #             for _ in range(c):
# #                 main.remove(alpha[i])
# #             if i <size-1:
# #                 main.remove(alpha[i+1])
            
# #             line = '-'.join(main).center(width,'-')
# #             print(line)
# #     def upper(size):
# #         width = len(midline)
# #         line = []
# #         copy=[]
# #         for i in range(size,1,-1):
# #             if i == size:
# #                 line.insert(0,alpha[i-1])

# #             else:
# #                 copy = line[::-1].copy()
# #                 line.insert(0,alpha[i-1])
# #             prt = '-'.join(copy+line).center(width,'-')
# #             print(prt)

# #     up = upper(size)
# #     print(midline)
# #     down = down(size)
    
# # def minion_game(string):
    
# #     point = 0
# #     words = set()
# #     for i in range(len(string)):
# #         for j in range(i+1,len(string)+1):
# #             word = string[i:j]
# #             if word[0] not in 'AEIOU':
# #                 words.add(word)
# #     for s in words:
# #         for i in range(len(string)):
# #             if string[i:i+len(s)] == s:
# #                 point += 1
# #     kevin = point
# #     point = 0
# #     words = set()
# #     for i in range(len(string)):
# #         for j in range(i+1,len(string)+1):
# #             word = string[i:j]
# #             if word[0] in 'AEIOU':
# #                 words.add(word)
# #     for s in words:
# #         for i in range(len(string)):
# #             if string[i:i+len(s)] == s:
# #                 point += 1
# #     stuart = point
# #     if stuart > kevin:
# #         print("Stuart",stuart)
# #     elif kevin>stuart:
# #         print("Kevin", kevin)
# #     else:
# #         print("Draw")

# # if __name__ == '__main__':
# #     s = input()
# #     minion_game(s)

# # def minion_game(string):
# #     s=len(string)
# #     v = 0
# #     c = 0
     
# #     for i in range(s):
# #         if string[i] in 'AEIOU':
# #            v+=(s-i)
# #         else:
# #            c+=(s-i)
                
# #     if v < c:
# #         print('Stuart',c)
# #     elif v > c:
# #         print('Kevin',v )
# #     else:
# #         print('Draw')
# # if __name__ == '__main__':
# #     s = input()
# #     minion_game(s)

# def merge_the_tools(string, k):
#     words=[]
#     c=1
#     x=""
#     y=''
#     for s in string:
#         if c<k:
#             x += s
#             c +=1
#         else:
#             c = 1
#             words.append(x + s)
#             x = ''
#     for word in words:
#         answer=''
#         i=0
#         for s in word:
            
            
#             if word.count(s)!=1:
#                 if y!=s:
#                     answer+=s
#                     y=s
#             else:
#                 answer+=s
#             if i==(k-1):
#                 y =''
#             i+=1
#         print(answer)
    
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


# from collections import Counter
# x = int(input())

# money = 0
# shoes = input().split()
# n = int(input())
# need = []
# for i in range(n):
#     s,p = input().split()
#     need+=[[s,p]]
# for i in need:
#     if i[0] in shoes:
#         shoes.remove(i[0])
#         money += int(i[1])
# print(money)
