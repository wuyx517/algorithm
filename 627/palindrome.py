import os

def palindrome_1(s):
    istr_dic = {}
    num = 0
    mid_num = False
    if len(s) == 0:
        print(0)
        return 0
    for i in s:
        if i not in istr_dic:
            istr_dic[i] = 1
        else:
            istr_dic[i] += 1
    for ikey in istr_dic:
        istr_num = istr_dic[ikey]
        if istr_num % 2:
            num += (istr_num - 1)
            mid_num = True
        else:
            num += istr_num
    if mid_num:
        num += 1
    print(num)
    return num

if __name__ == '__main__':
    line_list = open('test.txt', 'r').readlines()
    for line in line_list:
        line_strip = line.strip().split(' ')[0]
        palindrome_1(line_strip)

