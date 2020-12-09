import wave
song = wave.open("song_embedded.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))


extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

decoded = string.split("xxx")[0]


print("Encrypted text hidden is: " +decoded)
file1 = open("Extracted_Message_From_Audio.txt", "w")
file1.write(decoded)
file1.close()

song.close()