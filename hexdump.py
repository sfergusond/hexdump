import sys
import os

filename = sys.argv[1]

def parse(filename):
    
    out = open(filename + '_hexdump.txt', 'w')
    
    offset = 0x0
    lower = 0; upper = 16; doublespace = 0
    size = ((os.path.getsize(filename))//16); realsize = os.path.getsize(filename)
    
    with open(filename, 'rb') as f:
        data = f.read()

    if (realsize == 0):
        print('', end = '', file = out);
        return;
    
    for i in range(size + 1):
        
        line = data[lower:upper]

        if (i * 16 == realsize):
            print('{:08x}'.format(realsize), file = out)
            break;
        
        print('{:08x}'.format(offset), end = '  ', file = out)
            
        for byte in line:
            if (doublespace != 7):
                print('{:02x}'.format(byte), end = ' ', file = out)
            else:
                print('{:02x}'.format(byte), end = '  ', file = out)
            doublespace += 1
            
        if (i == size):
            if (realsize % 16 == 0):
                break;
            if (doublespace < 8):
                print(' ' * (50 - 3*doublespace - 1), end = '', file = out)
            else:
                print(' ' * (50 - 3*doublespace - 2), end = '', file = out)   
        
        print(' |', end = '', file = out)
        for byte in line:
            if (0x20 <= byte <= 0x7e):
                print(chr(byte), end = '', file = out)
            else:
                print('.', end = '', file = out)
        print('|', file = out)
    
        lower += 16
        upper += 16
        offset += 16
        doublespace = 0
    
    if (realsize % 16 != 0):   
        print('{:08x}'.format(realsize), file = out)

parse(filename)