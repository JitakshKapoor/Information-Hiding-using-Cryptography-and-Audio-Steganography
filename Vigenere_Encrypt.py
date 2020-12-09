
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

# Cipher text Undergoes columnar transposition
def encrypt(Final_cipher_Text, key):
  matrix = createEncMatrix(len(key), Final_cipher_Text)
  keywordSequence = getKeywordSequence(key)

  EncryptedText = ""
  for num in range(len(keywordSequence)):
    pos = keywordSequence.index(num+1)
    for row in range(len(matrix)):
      if len(matrix[row]) > pos:
        EncryptedText += matrix[row][pos]
  return EncryptedText


def createEncMatrix(width, Final_cipher_Text):
  r = 0
  c = 0
  matrix = [[]]
  for pos, ch in enumerate(Final_cipher_Text):
    matrix[r].append(ch)
    c += 1
    if c >= width:
      c = 0
      r += 1
      matrix.append([])

  return matrix


def getKeywordSequence(key):
  sequence = []
  for pos, ch in enumerate(key):
    previousLetters = key[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence

Final_Encrypt_Text = encrypt(Final_cipher_Text, key)

print("The Final Encrypted message is: " + Final_Encrypt_Text)

file1 = open("Encrypted_Message.txt", "w")
file1.write(Final_Encrypt_Text)
file1.close()

file2 = open("Keyword.txt", "w")
file2.write(keyword)
file2.close()

file3 = open("Key.txt", "w")
file3.write(key)
file3.close()