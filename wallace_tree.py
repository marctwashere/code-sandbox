#### 8x8 wallace tree, see partial products and all outputs
####
####
####

def CarrySaveAdder(x: str, y: str, z: str) -> tuple[str, str]:
    # get lengths
    xbits = len(x)
    ybits = len(y)
    zbits = len(z)

    # figure out the largest
    largest = x
    if ybits > len(largest):
        largest = y
    if zbits > len(largest):
        largest = z
    
    # fill others with 0s
    largestbits = len(largest)
    x = '0'*(largestbits-xbits) + x
    y = '0'*(largestbits-ybits) + y
    z = '0'*(largestbits-zbits) + z

    # perform the carry-save addition
    sum = []
    carry = []
    for i in reversed(range(len(largest))): # low to high order bits
        # snag the bits
        a = int(x[i])
        b = int(y[i])
        c = int(z[i])
        
        # sum the bits
        temp = a + b + c

        # prepend correct outputs
        if temp==3:
            sum.insert(0, '1')
            carry.insert(0, '1')
        elif temp==2:
            sum.insert(0, '0')
            carry.insert(0, '1')
        elif temp==1:
            sum.insert(0, '1')
            carry.insert(0, '0')
        elif temp==0:
            sum.insert(0, '0')
            carry.insert(0, '0')
    
    # "hardwire" the carry's 0
    carry.append('0')

    # prepare results
    # FIXME this code block should be its own function
    sum_str = ''
    j = 0
    for i in reversed(range(len(sum))):
        j += 1
        sum_str = sum[i] + sum_str
        if j % 4 == 0:
            sum_str = ' ' + sum_str

    carry_str = ''
    j = 0
    for i in reversed(range(len(carry))):
        j += 1
        carry_str = carry[i] + carry_str
        if j % 4 == 0:
            carry_str = ' ' + carry_str

    # print results
    print('S: {}'.format(sum_str))
    print('C: {}'.format(carry_str))
    print()

    # remove spaces
    sum_str = sum_str.replace(' ', '')
    carry_str = carry_str.replace(' ', '')

    return sum_str, carry_str
        
# FIXME this isn't implemented
def ParallelAdder(x: str, y: str) -> str:
    pass

# drive code
if __name__ == '__main__':
    # x = '11010111'
    # y = '110101110'
    # z = '0000000000'
    # CarrySaveAdder(x, y, z)

    #### 8 x 8 wallace tree
    x = '11010111'
    y = '10001011'

    # get partial products
    prods = []
    for i in reversed(range(8)):
        if y[i] == '0':
            prods.append('0'*8+'0'*(7-i))
        else:
            prods.append(x+'0'*(7-i))
    print("Got partial products:")
    print(prods)

    # use 8x8 carry-save adder with parallelism
    s0, c0 = CarrySaveAdder(prods[0], prods[1], prods[2])
    s0, c0 = CarrySaveAdder(s0, c0, prods[7])

    s1, c1 = CarrySaveAdder(prods[3], prods[4], prods[5])
    s1, c1 = CarrySaveAdder(s1, c1, prods[6])
    
    s0, c0 = CarrySaveAdder(s0, c0, c1)
    s0, c0 = CarrySaveAdder(s0, c0, s1)

    # final will never come bc i need to implement para adder
    # still, simply adding the final s0, c0 will give you the proper result
    final = ParallelAdder(s0, c0)
