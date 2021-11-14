"""
This is my python reimplementation of Parth58's Key_gen.exe
I'm using it to make the crackme challenge easier
"""
password = 'ABCDEFGH'
usr_input = 'thisisjustateststring'
usr_len = len(usr_input)

# first char
usr_char = ord(usr_input[0])
pass_char = ord(password[0])

a = 0x7a - usr_char
a = a % 0x1a
a += 0x41
password = chr(a) + password[1:]
# password[0] = chr(a)

# next 7 chars
for i in range(1,8):
    AL = ord(password[i])
    BL = ord(usr_input[i])
    DL = ord(password[i-1])

    AL += i
    AL += BL
    AL -= DL

    AL += usr_len & 0xff
    AL = AL %  0x1a
    AL += 0x41

    # password[i] = AL
    password = password[:i] + chr(AL) + password[i+1:]

print(password)

