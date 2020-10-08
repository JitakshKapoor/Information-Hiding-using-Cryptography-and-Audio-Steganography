"""
text = input("Enter the text to be encrypted: ")
keyword = input("Enter the keyword: ")
#Final keyword and text are made of same length

if len(text) == len(keyword):
    Final_Keyword = keyword
else:
    n = len(text) / len(keyword)
    n = int(n)
    Final_Keyword = ""
    for i in range(n):
        Final_Keyword += keyword
    rem = len(text) % len(keyword)
    for i in range(rem):
        Final_Keyword += keyword[i]

key = input("Enter the key for encryption: ")

#Converting Text to Cipher Text
cipher_text = []
for i in range(len(text)):
        x = (ord(text[i]) +
             ord(Final_Keyword[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
Final_cipher_Text = ''.join(cipher_text)
print("The converted Cipher Text: ", Final_cipher_Text)
"""
#Cipher text Undergoes columnar transposition
Final_cipher_Text = "UVAJKWZPSTJSRVWLWXYIISL"
key = "123456"
col = len(key)
if len(Final_cipher_Text) % len(key) == 0:
    row = len(Final_cipher_Text) / len(key)
else:
    row = int(len(Final_cipher_Text) / len(key)) + 1
matrix = [[]]
k = 0
for i in range(row):
    j = 0
    for j in range(col):
        matrix[i][j] = Final_cipher_Text[k]
        k = k+1
        if k > len(Final_cipher_Text):
            break
        else:
            continue
for i in range(row):
    for (j) in range(col):
        print(matrix[i][j])




