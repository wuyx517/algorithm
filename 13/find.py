'''
字符串查找

对于一个给定的 source 字符串和一个 target 字符串，
你应该在 source 字符串中找出 target 字符串出现的
第一个位置(从0开始)。如果不存在，则返回 -1。
'''

def find_1(source, target):
    '''
    time: 1918ms
    '''
    if target == '':
        return 0
    if source == '':
        return -1
    if len(source) < len(target):
        return -1
    len_target = len(target)
    if len_target == 1:
        source_list = [(source[i:i + len_target]) for i in range(len(source))]
    else:
        source_list = [(source[i:i+len_target]) for i in range(len(source))[:-(len_target-1)]]

    try:
        num = source_list.index(target)
    except:
        return -1
    return num

def find_kmp(source, target):
    '''
    886ms
    '''
    if target == '':
        return 0
    if source == '':
        return -1
    if len(source) < len(target):
        return -1
    num_list = [0]
    for i in range(len(target))[1:]:
        tmp_target = target[:i+1]
        #print(tmp_target)
        tmp_num = 0
        for j in range(len(tmp_target)):
            if tmp_target[:j+1] == tmp_target[-j-1:] and j != (len(tmp_target) -1):
                tmp_num = j + 1
        num_list.append(tmp_num)

    source_index = 0
    end_line = 1
    num = -1
    while source_index <= len(source) - len(target) and end_line == 1:
        if source[source_index] != target[0]:
            source_index += 1
            continue
        match_num = 1
        num_list_num = 0
        end_line = 0
        for i in range(len(target))[1:]:
            if source[source_index + i] != target[i]:
                match_num = i
                num_list_num = num_list[i - 1]
                end_line = 1
                break
        if end_line == 0:
            num = source_index
        jump_num = match_num - num_list_num
        source_index += jump_num

    return num

if __name__ == '__main__':
    line_list = open('test.txt', 'r').readlines()
    for line in line_list:
        line_sp = line.split(' ')
        if len(line_sp) == 2:
            source = line_sp[0].strip()
            target = line_sp[1].strip()
        else:
            source = ''
            target = ''
        num = find_1(source, target)
        #print(num)
        num_1 = find_1(source, target)
        print(num, '--', num_1)

