username = input('ID :')
password = input('Password :')
if username == 'Good' and password == '1234':
    baPrice = 20
    orPrice = 10
    apPrice = 50
    print('Login Succeed!')
    print('----Ruu Herr Shop----')
    print('รับอะไรดีค้าบบบบบบบบ')
    print('1.กล้วย', baPrice, 'Baht')
    print('2.ส้ม', orPrice, 'Baht')
    print('3.แอปเปิ้ล', apPrice, 'Baht')
    userSelected = input('>>')
    if userSelected == '1':
        take = int(input('รับกี่ชิ้นดีครับ? :'))
        print('ราคาทั้งหมด :', baPrice*take, 'Baht')
        print('--------------------------------------------')
    elif userSelected == '2':
        take2 = int(input('รับกี่ชิ้นดีครับ? :'))
        print('ราคาทั้งหมด :', orPrice * take2, 'Baht')
        print('--------------------------------------------')
    elif userSelected == '3':
        take3 = int(input('รับกี่ชิ้นดีครับ? :'))
        print('ราคาทั้งหมด :', apPrice * take3, 'Baht')
        print('--------------------------------------------')
    else:
        print('เลือกดีๆหน่อยเห้ย!!')
else:
    print('อีนี้ใครเนี้ย!!')