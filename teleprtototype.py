print('1:','add a cotact')
print('2:','search contact')
print('3:','delete contact')

a=int(input('enter 1 , 2 or 3: '))

if a==1:
    c=input('Name: ')
    b=(input('Contact: '))
    d=(input('Email ID: '))
    k=0

    f1=open('contacts2.txt','r')

    for line in f1:
        if c in line:
            k+=1
            print('name exists')
            break
        elif b in line:
            k+=1
            print('number exists')
            break
        elif c in line:
            k+=1
            print('mail exists')
            break
    f1.close

    if k==0:
        f1=open('contacts2.txt','a')
        f1.write('Name: ')
        f1.write(c)
        f1.write('\n')
        f1.write('Number: ')
        f1.write(b)
        f1.write('\n')
        f1.write('E-mail ID: ')
        f1.write(d)
        f1.write('\n')
        f1.write('\n')
        f1.close

    else:
        print('nothing was added')
            


elif a==2:
    string1=input('enter name: ')
    f1=open('contacts2.txt','r')
    index=0
    flag=0

    for line in f1:
        index += 1
        if string1 in line:
            flag=1
            break
    
    if flag == 0:
        print(string1,'not found')
    else:
        f1.close
        f1 = open('contacts2.txt')
        content=f1.readlines()
        print(content[index:index+2])
        


elif a==3:
    delet1 = input('enter the name to delete ')
    f1 = open('contacts2.txt','r')
    lin=0
    hoist=0

    for line in f1:
        lin+=1
        if delet1 in line:
            hoist = 1
            break

    if hoist == 0:
        print('Contact doesnt exist')

    else:
        f1 = open('contacts2.txt','r')
        rem = f1.readlines()
        f1.close

        del rem[lin-1:lin+2]
        new_file = open('contacts2.txt','w+')

        for line in rem:
            new_file.write(line)

        new_file.close
        print(delet1,'was succesfully deleted')
