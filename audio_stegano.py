import wave

#Read the Encrypted message saved in the .txt file
file1 = open("Encrypted_Message.txt", "r")
message = file1.read()

song = wave.open("song.wav", mode='rb')
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# This appends the dummy data to fill out rest of bytes in our message
message2 = message + int((len(frame_bytes)-(len(message)*8*8))/8) * 'x'
print(message)




