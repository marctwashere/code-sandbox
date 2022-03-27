# 8x8 wallace tree, see partial products and all outputs
from pydoc import tempfilepager


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
        if tempfilepager==3:
            sum.insert(0, '1')
            sum.insert(0, '1')
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
    sum_str = ''.join(sum)
    carry_str = ''.join(carry)

    # print results
    print('S: {}'.format(sum_str))
    print('C: {}'.format(carry_str))

    return sum_str, carry_str
        
# drive code
if __name__ == '__main__':
    x = '11010111'
    y = '110101110'
    z = '0000000000'
    CarrySaveAdder(x, y, z)
