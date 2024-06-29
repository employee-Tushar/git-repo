# input  ["Tushar", "door", "london"]
# output ["Tushar"]
from openpyxl import Workbook,load_workbook


def has_unique_chars(word):
    return len(set(word)) == len(word)
def largest_non_repeating_word(l):
    largest_word = ""
    for i in l:
        if has_unique_chars(i) and len(i) > len(largest_word):
            largest_word = i
    print(largest_word)


a="Tusharp is a very good Abhisektn"
d=a.split()
largest_non_repeating_word(d)

# z="tushartus"
# print(''.join(list(set(z))))
