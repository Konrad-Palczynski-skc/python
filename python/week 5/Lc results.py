mark1 = int(input('What mark did you recieve in the exam ? '))
subject = input('Subject: ')
h1 = 90
h2 = 80
h3 = 70
h4 = 60
h5 = 50
h6 = 40
h7 = 30
if mark1 >= h1:
    print('You recieved a H1 in',subject)
elif mark1 >= h2:
    print('You recieved a H2 in',subject)
elif mark1 >= h3:
    print('You recieved a H3 in',subject)
elif mark1 >= h4:
    print('You recieved a H4 in',subject)
elif mark1 >= h5:
    print('You recieved a H5 in',subject)
elif mark1 >= h6:
    print('You recieved a H6 in',subject)
elif mark1 >= h7:
    print('You recieved a H7 in',subject)
elif mark1 < h7:
    print('You recieved a H8 in',subject)
    print('You have failed')
