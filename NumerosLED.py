
digits = [ '1111110',
           '0110000',
           '1101101',
           '1111001',
           '0110011',
           '1011011',
           '1011111',
           '1110000',
           '1111111',
           '1111011']

def print_number(num):
    global digits
    digs = str(num)
    lines = [ '' for lin in range(5) ]
    
    for d in digs:
        seg = [[' ',' ',' '] for lin in range(5)]
        pattrn = digits[ord(d) - ord('0')]
        if pattrn[0] == '1':
            seg[0][0] = seg[0][1] = seg[0][2] = '#'
        if pattrn[1] == '1':
            seg[0][2] = seg[1][2] = seg[2][2] = '#'  
        if pattrn[2] == '1':
            seg[2][2] = seg[3][2] = seg[4][2] = '#'  
        if pattrn[3] == '1':
            seg[4][0] = seg[4][1] = seg[4][2] = '#'  
        if pattrn[4] == '1':
            seg[2][0] = seg[3][0] = seg[4][0] = '#'  
        if pattrn[5] == '1':
            seg[0][0] = seg[1][0] = seg[2][0] = '#'  
        if pattrn[6] == '1':
            seg[2][0] = seg[2][1] = seg[2][2] = '#'  
        for lin in range(5):
            lines[lin] += ''.join(seg[lin]) + ' '
    for lin in lines:
        print(lin)
print_number(int(input("Ingrese el número a mostrar en pantalla: \n")))