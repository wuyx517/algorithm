def max_pali_len(s):
    pli_dic = {}
    for i in s:
        if i not in pli_dic:
            pli_dic[i] = 1
        else:
            pli_dic[i] += 1
    longest = 0
    have_odd = 0
    for num in pli_dic.values():
        if num % 2 == 0:
            longest += num
        else:
            longest += (num - 1)
            have_odd = 1

    return longest + have_odd



if __name__ == '__main__':
    line_list = open('test.txt', 'r').readlines()
    for line in line_list:
        line_sp = line.replace('\n', '').split('---')
        s = line_sp[0]
        answer = line_sp[1]
        result = max_pali_len(s)
        print(result, '--', answer)





