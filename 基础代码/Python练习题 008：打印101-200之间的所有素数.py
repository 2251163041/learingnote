'''
先建立101-200的整数列表，再进行判断，如果某个数字能被“从2至这个数字前一位”整除，则将这个数字从列表剔除。挨个走一遍后，剩下的就都是素数了。
'''

lst = []
for i in range(100):  # 建立 101-200 的列表
    lst.append(101 + i)

for i in range(101, 201):  # 除数为 101-200 这200个数字
    for j in range(2, i):  # 除数为从2至i本身的前一个数字
        if i % j == 0:  # 如果能除尽
            lst.remove(i)  # 则从 lst 列表剔除
            break
print(lst)  # 剩下的都是素数


