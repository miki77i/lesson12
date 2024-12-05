from functions import salary, hello_who

if salary(2, 10) != 40:
    print('Error')

if hello_who('Max') != 'Hello,Max':
    print('Error')

else:
    print('Good')

if hello_who('Leo') != 'Hello,Leo':
    print('Error')
else:
    print('Good')