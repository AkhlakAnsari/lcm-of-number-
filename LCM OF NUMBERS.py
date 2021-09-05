#L.C.M of user inut number
print('PLEASE FILL THE REMAINING NUMBER YOU CAN PUT  = 1')
#YOU CAN TAKE UPTU 6 NUMBER LCM
a=int(input('ENTER 1st NUMBER:'))
b=int(input('ENTER 2nd NUMBER:'))
c=int(input('ENTER 3rd NUMBER:'))
d=int(input('ENTER 4th NUMBER:'))
e=int(input('ENTER 5th NUMBER:'))
f=int(input('ENTER 6th NUMBER:'))

for x in range ( 1, (a * b * c  *d *e* f ) + 1 ):
    if x%a==0 and x%b==0 and x%c==0 and x%d==0 and x%e==0 and x%f==0:
        print("LCM OF NUMBER=",x)
        break
# Thanks akhlakansari94@gmail.com