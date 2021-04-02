import re
import sys

dic = {'a': 2, 'b': 5, 'c': 4, 'd': 4, 'e': 1, 'f': 6,
       'g': 5, 'h': 5, 'i': 1, 'j': 7, 'k': 6, 'l': 3,
       'm': 5, 'n': 2, 'o': 3, 'p': 5, 'q': 7, 'r': 2,
       's': 1, 't': 2, 'u': 4, 'v': 6, 'w': 6, 'x': 7,
       'y': 5, 'z': 7}
word_map = {}

with open('wordsEn.txt') as file:
    list_o = file.readlines()
    for i in range(len(list_o)):
        word = ''.join(list_o[i].rsplit('\n'))
        sorted_word = ''.join(sorted(list(word)))
        if sorted_word in word_map:
            word_list = word_map[sorted_word]
            word_list.append(word)
            word_map[sorted_word] = word_list
        else:
            word_map[sorted_word] = [word]


def get_score(w):
    res_score = 0
    for k in range(len(w)):
        res_score += dic[w[k]]
    return res_score


def str_extra_combination(s):
    extra_set = set(s)
    if len(s) > 1:
        for i in range(1, len(s)):
            j = 0
            while j + i <= len(s):
                extra_set.add(s[:j] + s[j + i:])
                extra_set |= str_extra_combination(s[:j] + s[j + i:])
                j += 1
    return extra_set


if __name__ == '__main__':
    res = []
    score = 0
    in_str = str(input().replace(' ', ''))
    char_arr = sorted(list(in_str))
    word_set = set()

    if bool(re.search(r'\d', in_str)) == False and 3 <= len(in_str) <= 10:
        for i in range(1, len(char_arr) + 1):
            j = 0
            while j + i <= len(char_arr):
                word_set.add(''.join(char_arr[j:j + i]))
                j += 1
        word_set |= str_extra_combination(''.join(char_arr))

        for word in word_set:
            if word in word_map:
                sc = get_score(word)
                if score < sc:
                    score = sc
                    res = word_map[word]
                elif score == sc:
                    res.extend(word_map[word])

    print(res)
    print(score)