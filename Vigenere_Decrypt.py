file1 = open("Extracted_Message_From_Audio.txt", "r")
message = file1.read()

file2 = open("Keyword.txt", "r")
keyword = file2.read()

file3 = open("Key.txt", "r")
keywordSequence = file3.read()


def decrypt(message, keyword):
  matrix = createDecrMatrix(getKeywordSequence(keyword), message)

  plaintext = "";
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def createDecrMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = len(message) / width
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height, len(message))

  pos = 0
  for num in range(len(keywordSequence)):
    column = keywordSequence.index(num+1)

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


def getKeywordSequence(keyword):
  sequence = []
  for pos, ch in enumerate(keyword):
    previousLetters = keyword[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence
