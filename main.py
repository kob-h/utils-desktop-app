import copy
import string

if 4 > 3:
    if 7 == 7:
        b = 5

c = b + b

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    file = open(filename, 'w')
    file.write('Hello\n')
    file.close()

file = open('members.txt', 'r')
content = file.readlines()
file.close()

new_name = input('enter new name:')
content.append(new_name)
file = open('members.txt', 'w')
file.writelines(content)
file.close()

# More Pythonic solution https://realpython.com/python-practice-problems/
def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


def caesar_cipher(inputs: str, shift_val: int) -> str:
    lst = list(inputs)
    for idx, ch in enumerate(lst):
        lst[idx] = chr(((ord(ch) + shift_val - ord('a')) % 26) + ord('a')) if ch.isalpha() else ch
    return "".join(lst)


