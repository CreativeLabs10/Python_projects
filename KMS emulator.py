import time

print('')
print('')
print('')

print('KMS Services ©️ 2024')
print('Starting...')
print('')
print('')
time.sleep(3)

print('kms/> Failed to connect the net')
print('kms/> Only Local connecting...')
time.sleep(3)
print('kms/> Connected to Local Server')
print('      Last data: 19.02.24 (Please, connect the net)')
print('')
print('') 
time.sleep(1)
print('Select the type of activator:')
print('')

p1 = 'MS Windows 10                  Available            1                        14.08.22'
p2 = 'MS Windows 11                  Available            2                        20.11.23'
p3 = 'Office 360                     No network           -                        --.--.--'
p4 = 'Office 2016                    Available            4                        20.11.23'
p5 = 'Key Gen.exe                    Only admins          5                        05.02.24'
p6 = 'kms-port.com                   No network           -                        --.--.--'
print('Name                           Status               Key to select            Last update')
print('')
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print('')
print('Waiting for input:')
i = input()

while i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6':
    if i == '1':
        print('kms/> Looking for MS Windows 10')
        print('      Scanning...')
        print('      Your copy is activated')
        print('      You can also replace key')
        print('      Replace - 1       Cancel - 2')
        c = input()
        if c == '1':
            print('kms/> Your previous key will be replaced, do you want to continue? (yes or no)')
            c2 = input()
            if c2 == 'yes':
                print('      Generating... (about 10 sec)')
                time.sleep(7)
                print('      Replacing...')
                time.sleep(2)
                print('kms/> The key has been successfully installed')
            elif c2 == 'no':
                print('      Thanks for using KMS. Waiting for input:')
                i = input()
        elif c == '2':
            print('      Thanks for using KMS. Waiting for input:')
        i = input()
    
    elif i == '2':
        print('kms/> Looking for MS Windows 11')
        print('      Scanning...')
        print('      Your copy is activated')
        print('      You can also replace key')
        print('      Replace - 1       Cancel - 2')
        c = input()
        if c == '1':
            print('kms/> Your previous key will be replaced, do you want to continue? (yes or no)')
            c2 = input()
            if c2 == 'yes':
                print('      Generating... (about 10 sec)')
                time.sleep(14)
                print('      Replacing...')
                time.sleep(2)
                print('kms/> The key has been successfully installed')
            elif c2 == 'no':
                print('      Thanks for using KMS. Waiting for input:')
                i = input()
        elif c == '2':
            print('      Thanks for using KMS. Waiting for input:')
        i = input()
    
    elif i == '3':
        print('kms/> NET_ERR_720')
        print('      You can activate Office 360 only with Network. Waiting for input:')
        i = input()
    
    elif i == '4':
        print('kms/> Looking for Office 2016')
        print('      Scanning...')
        print('      Your copy is activated')
        print('      You can also replace key')
        print('      Replace - 1       Cancel - 2')
        c = input()
        if c == '1':
            print('kms/> Your previous key will be replaced, do you want to continue? (yes or no)')
            c2 = input()
            if c2 == 'yes':
                print('      Generating... (about 5 sec)')
                time.sleep(4)
                print('      Replacing...')
                time.sleep(2)
                print('kms/> The key has been successfully installed')
            elif c2 == 'no':
                print('      Thanks for using KMS. Waiting for input:')
                i = input()
        elif c == '2':
            print('      Thanks for using KMS. Waiting for input:')
        i = input()
    
    elif i == '5':
        print('kms/> PASS_ERR_403')
        print('      Access denied. Waiting for input:')
        i = input()
    
    elif i == '6':
        print('NET_ERR_720')
        print('You can visit kms-port.com only with Network. Waiting for input:')
        i = input()