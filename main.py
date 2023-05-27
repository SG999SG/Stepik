def encryption(text, language):
    pass

def decryption(text, language):
    pass

dest = input('Направление шифрования (Шифрование - 1, дешифрование - 0 )')
lang = input('язык алфавита ')
step = int(input('Шаг сдвига '))
s = input('Текст ')





n = int(input())
s = input()
for c in s:
    d = ord(c) - n
    if d < 97:
        d += 26
    print(chr(d), end='')