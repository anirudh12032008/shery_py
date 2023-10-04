# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # import math
# # ab = 100
# # bc = 1
# # ca = math.hypot(ab,bc)
# # mc = ca/2
# # bca = math.asin(1*ab/ca)
# # mb = math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
# # mbc = math.asin(math.sin(bca)* mc/mb)
# # ans = int(round(math.degrees(mbc),0))
# # # mb/sin(mb)=mc/sin(mc)
# # #sin(mc) =mc/mb*sin(mb)
# # # we know sin(mb) we know mc and mb
# # print(ans,'\u00B0',sep='')
# if __name__ == '__main__':
#     dets = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         stud = [name,score]
#         dets += [stud]
#     sort = sorted(dets, key=lambda x: x[1])
#     f_score = sorted(dets, key=lambda x: x[1])[1][1]
#     f_sort = []
#     for s in sort:
#         if s[1]==f_score:
#             f_sort += [s[0]]
#     ans = sorted(f_sort)
#     for s in ans:
#         print(s)
# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(t):
   return hash(t)

t = ( 1, 2)
print(solve(t))