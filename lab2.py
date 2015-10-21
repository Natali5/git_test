from random import randint
import string

# create text file named TF2_1
tf2 = open("TF2_1", "w")
for line_number in range(10):
    text = ''
    for symbol_index in range(10):
        text += string.printable[randint(0, 30)]
    text += '\n'
    tf2.write(text)
tf2.close()

#read created file
print "======== CREATED LINES =========="
tf2 = open("TF2_1", "r")
for line in tf2.readlines():
    print line
tf2.close()

#find all number hits and write them into TF2_2

tf2 = open("TF2_1", "r")
tf2_2 = open("TF2_2", "w")
for line in tf2.readlines():
    digit_line = ''
    for char in line:
        if char.isdigit():
            digit_line += char
    tf2_2.write(digit_line + '\n')
tf2.close()
tf2_2.close()

print "======== DIGITS FROM LINES =========="

tf2_2 = open("TF2_2", "r")
for line in tf2_2.readlines():
    print line
tf2_2.close()
