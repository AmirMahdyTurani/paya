# In the name of Allah

# reading data from user
words = input().split()  # s'
s = input()  # s


# find the minimum of two number
def min(a, b):
    return b if a > b else a


# check if only one character is different in two strings
def check_diff(str1, str2):
    diff = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            diff += 1
    return diff == 1


# check if two strings have the same length
def same_len(str1, str2):
    return len(str1) == len(str2)


# proccesing and correcting the s'
def correct_wrong_word(words):
    for i in range(len(words)):
        word = words[i]
        if check_diff(word, s) and same_len(word, s):
            words[i] = s
    return words


correct_string = " ".join(correct_wrong_word(words))

print(correct_string)
