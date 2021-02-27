username = input('ID :')
password = input('Password :')
if username == 'ตัวจริงจ้ะ' and password == '1234':
    print('ตัวจริงมาละจ้ะ')
    print('----Ru Her Service----')
    print('1.Vat Calculator')
    print('2.Price Calculator')
    userSelected = input('>>')
    if userSelected == '1':
        price = int(input('Price :'))
        vat = 7
        result = price+(price*vat/100)
        print(result)
    elif userSelected == '2':
        print('Welcome to Price Calculator')
    else:
        print('เลือกดีๆเถอะขอร้อง')
else:
    print('เลิกปลอมนะขอร้อง')