def check_if_common_char(first, second):
    curr = first ^ second
    if 32 <= curr <= 122 and curr not in [96]:
        return True
    return False

def decrypt(ascii, key):
    return ''.join(chr(x ^ ord(y)) for x, y in zip(ascii, key))

letters = {x:chr(x) for x in range(97, 123)}
#print(letters[97], letters[122])

f = open('p059_cipher.txt')

text = f.read().strip().split(',')
n = len(text)
#print(text, text[0])

text = [int(x) for x in text]

first = set()
second = set()
third = set()

for key in letters.keys():
    first.add(key)
    for position in range(0, n, 3):
        if not check_if_common_char(text[position], key):
            first.remove(key)
            break

for key in letters.keys():
    second.add(key)
    for position in range(1, n, 3):
        if not check_if_common_char(text[position], key):
            second.remove(key)
            break

for key in letters.keys():
    third.add(key)
    for position in range(2, n, 3):
        if not check_if_common_char(text[position], key):
            third.remove(key)
            break

print(first, second, third)
# e, x, p

encryption_key = chr(list(first)[0]) + chr(list(second)[0]) + chr(list(third)[0])

message = ''

for i in range(0, n, 3):
    message += decrypt(text[i : i + 3], encryption_key)

print(message)
print(sum(map(ord, message)))