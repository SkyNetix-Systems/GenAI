# a = int(input('Enter a:'))
# b = int(input('Enter b:'))
# try:
#     c = a / b
#     print(c)
# except:
#     print("An exception has occurred.")
# finally:
#     print('Good bye!')
#
# x = 10
# print(x**x)
# print('some other code')


f = open('a.txt', 'w')
try:
    f.write('write something to the file.')
except:
    print('Cannon write to file!')
else:
    print('File was written successfully!')
finally:
    print('This code is always executed!!!')
    if not f.closed:
        f.close()
    print('File closed:', f.closed)

print('Some other code ...')
