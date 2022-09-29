import re


def take_num_out(input_str):
    # result_list = []
    # for i in input_str:
    #     if i.isdigit():
    #         result_list.append("")
    #     else:
    #         result_list.append(i)
    # return "".join(result_list)
    return re.sub(r'\d', '', input_str)


def take_spaces_out(input_str):
    return input_str.replace(" ", "")


def leave_five_symb(input_str):
    return input_str[:5]


def sum_all_prev_func(input_str):
    first_f = take_num_out(input_str)
    second_f = take_spaces_out(first_f)
    third_f = leave_five_symb(second_f)
    return third_f


your_str = input("Введите строку: ")
print(sum_all_prev_func(your_str))


def words_tester(string_list):
    words_list = []

    for word in string_list:
        len_word = str(len(word))
        word = re.sub(r'\w', 'shwa', str(word), count=1)
        words_list.append(f'{word} {len_word}')

    return re.sub(r'a[aeoiuy]', 'a', str(words_list))


def words_tester_(string_list):
    word_list = []

    for word in string_list:
        len_word = str(len(word))
        vowels = 'ayouie'

        if word[1] in vowels:
            word_list.append(f'shwa{word[2:]} {len_word}')
        else:
            word_list.append(f'shwa{word[1:]} {len_word}')

    return word_list


test_list = ["shwatro2013", 'apple', 'biiba', 'boba']
print(words_tester(test_list))


def solution(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
# the function will break up camel casing, using a space between words, or
# def solution(s):
#     result_word = ''
#
#     for letter in s:
#
#         if letter.isupper():
#             result_word += ' ' + letter
#         else:
#             result_word += letter
#
#     return result_word
