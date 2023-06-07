def encryption(text, language, step):
    encrypted_text = ''
    if language == 'en':
        upper_char = 'A' # английская
        lower_char = 'a'
        count_char = 26
    if language == 'ru':
        upper_char = 'А' # русская
        lower_char = 'а'
        count_char = 32

    for char in text:
        if char.isalpha():
            ascii_offset = ord(upper_char) if char.isupper() else ord(lower_char)
            encrypted_char = chr((ord(char) - ascii_offset + step) % count_char + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def decryption(text, language, step):
    return encryption(text, language, -step)

def valid_input(text, type):
    if type == 'string':
        var = input(text)
    if type == 'int':
        var = int(input(text))

dest = input('Направление шифрования (Шифрование - 1, дешифрование - 0) ')
lang = input('Язык алфавита (en / ru) ')
st = int(input('Шаг сдвига '))
s = input('Текст ')

if dest == '1':
    enc_text = encryption(s, lang, st)
    print(enc_text)
if dest == '0':
    dec_text = decryption(s, lang, st)
    print(dec_text)
