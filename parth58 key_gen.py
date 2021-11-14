"""
This is my python reimplementation of Parth58's Key_gen.exe
I'm using it to make the crackme challenge easier
"""
password = 'ABCDEFGH'
usr_input = 'AFPEQXKHdog'
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

# on to solving the challenge
# find the username that creates the password "AFMWAFPE"
# edit: username (soln) must also be in all caps
"""
FIRST CHAR
ord(pass[0]) = (ord(cap_alphabet[0]) + ord(usr[0])) % 0x1a + 0x41
ord('A') = (ord('A') + ord(usr[0])) % 26 + 65
0 = (65 + usr[0]) % 26
so set usr[0] to any multiple of 26 --> some options '`' and 'z' and 'F'

GENERAL CHAR for i>0
ord(pass[i]) = (ord(cap_alphabet[i]) + i + ord(usr[i]) - ord(pass[i-1] + len(usr)) % 0x1a + 0x41)
then SOLVE FOR usr[i]
and use the % property to keep adding 0x1a until it is an ASCII char

SECOND CHAR
ord('F') = (ord('B') + 1 + usr[1] - ord('A') + 11) % 0x1a + 0x41
5 = (13 + usr[1]) % 26
set usr[1] to 26-13+5 = 18 --> not a nice ASCII char
so add 26*n, n = 0, 1, 2, ... until nice ASCII char
usr[1] = 'F'

THIRD CHAR
ord('M') = (ord('C') + 2 + usr[2] - ord('F') + 11) % 0x1a + 0x41
12 = (10 + usr[1]) % 26
set usr[1] to 26-10+12 = 28 --> not a nice ASCII char
so add 26*n, n = 0, 1, 2, ... until nice ASCII char
usr[2] = 'P'

The process repeats from there
"""

def generate_usr(str_len=8, password='AFMWAFPE'):
    cap_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    username = []

    # make first char
    needed_remainder = ord(password[0]) - 0x41
    operand = ord(cap_alphabet[0])

    if operand >= 0x1a:
        possible_char = operand - 0x1a + needed_remainder
    else:
        possible_char = 0x1a - operand + needed_remainder

    while possible_char < 0 or not chr(possible_char).isupper():
        possible_char += 0x1a
    username.append(chr(possible_char))

    # make remaining chars
    for i in range(1, len(password)):
        needed_remainder = ord(password[i]) - 0x41
        operand = ord(cap_alphabet[i]) + i - ord(password[i-1]) + str_len

        if operand >= 0x1a:
            possible_char = operand - 0x1a + needed_remainder
        else:
            possible_char = 0x1a - operand + needed_remainder
     
        while possible_char < 0 or not chr(possible_char).isupper():
            possible_char += 0x1a
        username.append(chr(possible_char))

    # output and close
    username = ''.join(username)
    print('Username to generate that password would be {}'.format(username))
    return username

generate_usr()
print('debug')