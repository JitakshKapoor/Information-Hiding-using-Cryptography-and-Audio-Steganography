file1 = open("Extracted_Message_From_Audio.txt", "r")
message = file1.read()

file2 = open("Keyword.txt", "r")
keyword = file2.read()

file3 = open("Key.txt", "r")
key = file3.read()

def decrypt(message, key):
  matrix = createDecrMatrix(getKeywordSequence(key), message)

  plaintext = "";
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def createDecrMatrix(key, message):
  width = len(key)
  height = len(message) / width
  height = int(height)
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height, len(message))

  pos = 0
  for num in range(len(getKeywordSequence(key))):
    column = getKeywordSequence(key).index(num+1)

    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1

  return matrix


def createEmptyMatrix(width, height, length):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      if totalAdded >= length:
        return matrix
      matrix[r].append('')
      totalAdded += 1
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


cipher_text = decrypt(message, key)

if len(cipher_text) == len(keyword):
    Final_Keyword = keyword
else:
    n = len(cipher_text) / len(keyword)
    n = int(n)
    Final_Keyword = ""
    for i in range(n):
        Final_Keyword += keyword
    rem = len(cipher_text) % len(keyword)
    for i in range(rem):
        Final_Keyword += keyword[i]

orig_text = []
for i in range(len(cipher_text)):
    x = (ord(cipher_text[i]) - ord(Final_Keyword[i]) + 26) % 26
    x += ord('A')
    orig_text.append(chr(x))
Original_message = "".join(orig_text)

print('The original message communicated is: ' + Original_message)