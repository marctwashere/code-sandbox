"""
This is my python reimplementation of Parth58's Key_gen.exe
I'm using it to make the crackme challenge easier



on to solving the challenge
find the username that creates the password "AFMWAFPE"
edit: username (soln) must also be in all caps

FIRST CHAR
ord(pass[0]) = (0x7a - ord(usr[0])) % 0x1a + 0x41
ord('A') = (122 - ord(usr[0])) % 26 + 65
0 = (122 - usr[0]) % 26
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

Got tired of doing the math and made a gen_usr function
"""
def gen_password(usr_input):
    password = 'ABCDEFGH'
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

    print('User {} generates password {}'.format(usr_input, password))
    return password

def gen_usr(str_len=8, password='AFMWAFPE'):
    cap_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # needed for later calculations
    username = [] # store output here

    # all password chars are necessary for determining username
    for i in range(len(password)):
        if i == 0:
            # special case for first char
            needed_remainder = ord(password[0]) - 0x41
            operand = 0x7a
        else:
            # all remaining chars handled the same
            needed_remainder = ord(password[i]) - 0x41
            operand = ord(cap_alphabet[i]) + i - ord(password[i-1]) + str_len
        
        # perform necessary calculation
        possible_char = None
        if operand >= 0x1a:
            possible_char = operand - 0x1a + needed_remainder
        else:
            possible_char = 0x1a - operand + needed_remainder
        
        # move possible char into the range of ASCII uppercase
        while possible_char < 65:
            possible_char += 0x1a
        while possible_char > 65:
            possible_char -= 0x1a
        
        # add hex(26) until we find our uppercase char
        while not chr(possible_char).isupper():
            possible_char += 0x1a
        
        # save char
        username.append(chr(possible_char))

    # output and close
    username = ''.join(username)
    print('Username to generate password {} would be {}'.format(password, username))
    return username

# solve the challenge
usr = gen_usr(str_len=8, password='AFMWAFPE')

# check that this user creates that password
pw = gen_password(usr)

print('debug')


