text = str(input('word:'))
password1_caesar = []
password2_reverse = []

'''
two simple step to encryption
1 : encrypt to caesar
2 : reversed caesar and encrypt to num(ascii code)
'''
print('Encrypt 2step')
# caesar
for i in text:
    temp = ord(i) + 3
    password1_caesar.append(chr(temp))
print('caesar:', ''.join(password1_caesar))

# reverse + ascii
for i in password1_caesar[::-1]:  # revers
    password2_reverse.append(ord(i))
print('reversed + ascii code:', password2_reverse)

'''
two simple step to decryption
1 : in order those reversed ascii
2 : decrypt caesar
'''
print('Decrypt 2step')
# Target
decryption_keyword = password2_reverse
decrypt1_ascii = []   # first step
decrypt2_caesar = []  # sec step
for i in decryption_keyword[::-1]:  # revers
    decrypt1_ascii.append(i)
print('in order keyword(ascii code):', decrypt1_ascii)

for i in decrypt1_ascii:
    temp = i - 3
    decrypt2_caesar.append(chr(temp))
print('decrypt caesar:', ''.join(decrypt2_caesar))




