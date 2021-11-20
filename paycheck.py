hours = input( 'Hours ? = ')
pay = input( 'Rate ? = ')
h = float(hours)
p = float(pay)

while True :
    if h == 0.0 :
        ct = input('Check total? ')
        c = float(ct)
        c = c / p
        print('Hours worked ? = ', c)
        quit()
    if p == 0.0 :
        ct = input('Check total ? ')
        c = float(ct)
        c = c / h
        print('Hourly rate = $', c)
        quit()
    if h > 40.0 :
        reg = h * p
        otp = (h - 40.0) * (p * 0.5)
        x = reg + otp
    else :
        x = h * p
        print('pay','$',x)
    print('check another?')
    c = input(' y or n ? ')
    if c == 'y':
        Hours = input( 'Hours ? = ')
        Pay = input( 'Rate ? = ')
        H = float(Hours)
        P = float(Pay)
        if H == 0.0 :
            CT = input('Check total? ')
            C = float(CT)
            C = C / P
            print('Hours worked ? = ', C)
            quit()
        if P == 0.0 :
            CT = input('Check total ? ')
            C = float(CT)
            C = C / H
            print('Hourly rate = $', C)
            quit()
        if H > 40.0 :
            REG = H * P
            OTP = (H - 40.0) * (P * 0.5)
            X = REG + OTP
        else :
            X = H * P
        print('pay','$',X)
        break
    if c == 'n':
        print('Thanks')
        break
