# for i in range(20,0,-1):
#     if i%15==0:
#         print("Pawan Here")
#     elif i%5==0:
#         print("Here")
#     elif i%3==0:
#         print("Pawan")
#     else:
#         print(i)
"""
Convert number into list of digits
"""
# a=1234
# k=str(a)
# b=[]
# for i in range(0, len(k)):
#     b.append(int(k[i]))
#     print(b)
#
# print(b)
"""
Calculate minimum non recurring
"""
a = [1, 1, 1, 2, 2,4,5]

k = min(a, key=a.count)

print(k)