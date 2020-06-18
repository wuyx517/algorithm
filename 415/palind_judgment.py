'''
给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，忽略大小写。
'''

def judgment_1(s):
    '''
    59ms
    '''
    if s is None:
        return False
    start_i = 0
    end_i = len(s) - 1
    tmp = 0
    while end_i > start_i:
        start_str = s[start_i]
        end_str = s[end_i]
        if (not start_str.isalpha()) and (not start_str.isdigit()):
            start_i += 1
            continue

        if (not end_str.isalpha()) and (not end_str.isdigit()):
            end_i -= 1
            continue
        if start_str.lower() != end_str.lower():
            return False
        start_i += 1
        end_i -= 1
    return True


if __name__ == '__main__':
    line_list = open('test.txt', 'r').readlines()
    for line in line_list:
        line_sp = line.replace('\n','').split('---')
        s = line_sp[0]
        answer= line_sp[1]
        result = judgment_1(s)
        print(result, '--', answer)









