def judgment_1(s):
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

def longest_pali(s):

    if s is None:
        return ''
    if len(s) == 1:
        return s

    win_len = len(s)
    result = ''
    while win_len > 1:

        for i in range(len(s)):
            if i + win_len > len(s):
                break
            s_pali = s[i:i+win_len]
            if judgment_1(s_pali):
                result = s_pali
                return result
        win_len -= 1

    return result

def longestPalindrome(s):
    if not s:
        return ""

    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True
    for i in range(1, n):
        is_palindrome[i][i - 1] = True

    longest, start, end = 1, 0, 0
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
            if is_palindrome[i][j] and length + 1 > longest:
                longest = length + 1
                start, end = i, j

    return s[start:end + 1]

def Manacher(s):
    '''
    时间复杂度为O(n)
    这个是别人的算法 不过好像没有更新 最大边界，不知是不是我的理解有误
    '''
    if not s:
        return ''

    chars = []
    for c in s:
        chars.append('#')
        chars.append(c)
    chars.append('#')

    n = len(chars)
    palindrome = [0] * n
    palindrome[0] = 1

    mid, longest = 0, 1
    for i in range(1, n):
        length = 1
        if mid + longest > i:
            mirror = mid - (i - mid)
            length = min(palindrome[mirror], mid + longest - i)

        while i + length < len(chars) and i - length >= 0:
            if chars[i + length] != chars[i - length]:
                break
            length += 1

        if length > longest:
            longest = length
            mid = i

        palindrome[i] = length

    # remove the extra #
    longest = longest - 1
    start = (mid - 1) // 2 - (longest - 1) // 2
    return s[start:start + longest]

def manache_slef(s):
    if s is None:
        return ''
    if len(s) == 1:
        return s

    #采用manache的形式
    new_list = ['$']
    for i_s in s:
        new_list.append('#')
        new_list.append(i_s)
    new_list.append('#')
    new_list.append('\0')

    len_list = len(new_list)
    p_list = [0] * len_list

    max_len = 0
    max_mid = 0
    max_x = 0
    max_i = 1
    for new_i in range(len_list)[1:-1]:
        #判断当前点是否大于最大边界点
        if new_i < max_x:
            tmp_j = 2*max_i - new_i
            #判断该点的加上最大的已知边长是否大于最大边界
            if max_x - new_i >= p_list[tmp_j]:
                # 如果不是则将对称点的值赋予此点
                p_list[new_i] = p_list[tmp_j]
                continue

            else:
                # 如果大于 只需判断大于边长的部分即可
                pali_r = max_x - new_i + 1
        else:
            pali_r = 1

        while new_list[new_i + pali_r] == new_list[new_i - pali_r]:
            pali_r += 1

        tmp_x = new_i + pali_r - 1
        if max_x < tmp_x:
            max_i = new_i
            max_x = tmp_x

        if max_len < pali_r:
            max_len = pali_r
            max_mid = new_i

        p_list[new_i] = pali_r

    result = ''.join(new_list[max_mid - max_len + 1:max_mid + max_len - 1]).replace('#', '')
    return result

if __name__ == '__main__':
    line_list = open('test.txt', 'r').readlines()
    for line in line_list:
        line_sp = line.replace('\n', '').split('---')
        s = line_sp[0]
        answer = line_sp[1]
        result = manache_slef(s)
        print(result, '--', answer)





