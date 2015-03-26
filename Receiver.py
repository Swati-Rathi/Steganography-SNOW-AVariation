  f=open('out2.html','r')
x = repr(f.read())
#print x
e = []
for y in range(0,27):
    e.append([])
e[0]='h'
e[1]=repr('\r')
e[2]=repr('\r\r')
e[3]=repr('\r\r\r')
e[4]=repr('\r\r\r\r')
e[5]=repr('\r\r\r\r\r')
e[6]=repr('\r\r\r\r\r\r')
e[7]=repr('\r\r\r\r\r\r\r')
e[8]=repr('\r\r\r\r\r\r\r\r')
e[9]=repr('\r\r\r\r\r\r\r\r\r')
e[10]=repr('\r\r\r\r\r\r\r\r\r\r')
e[11]=repr('\r\r\r\r\r\r\r\r\r\r\r')
e[12]=repr('\r\r\r\r\r\r\r\r\r\r\r\r')
e[13]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[14]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[15]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[16]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[17]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[18]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[19]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[20]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[21]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[22]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[23]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[24]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[25]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')
e[26]=repr('\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r')


#for l in range(0,19):
while(e[1].strip("'") in x):
    if e[26].strip("'") in x:
        x= x.replace(e[26].strip("'"),'Z')
    elif e[25].strip("'") in x:
        x= x.replace(e[25].strip("'"),'Y')
    elif e[24].strip("'") in x:
        x= x.replace(e[24].strip("'"),'X')
    elif e[23].strip("'") in x:
        x= x.replace(e[23].strip("'"),'W')
    elif e[22].strip("'") in x:
        x= x.replace(e[22].strip("'"),'V')
    elif e[21].strip("'") in x:
        x= x.replace(e[21].strip("'"),'U')
    elif e[20].strip("'") in x:
        x= x.replace(e[20].strip("'"),'T')
    elif e[19].strip("'") in x:
        x= x.replace(e[19].strip("'"),'S')
    elif e[18].strip("'") in x:
        x= x.replace(e[18].strip("'"),'R')
    elif e[17].strip("'") in x:
        x= x.replace(e[17].strip("'"),'Q')
    elif e[16].strip("'") in x:
        x= x.replace(e[16].strip("'"),'P')
    elif e[15].strip("'") in x:
        x= x.replace(e[15].strip("'"),'O')
    elif e[14].strip("'") in x:
        x= x.replace(e[14].strip("'"),'N')
    elif e[13].strip("'") in x:
        x= x.replace(e[13].strip("'"),'M')
    elif e[12].strip("'") in x:
        x= x.replace(e[12].strip("'"),'L')
    elif e[11].strip("'") in x:
        x= x.replace(e[11].strip("'"),'K')
    elif e[10].strip("'") in x:
        x= x.replace(e[10].strip("'"),'J')
    elif e[9].strip("'") in x:
        x= x.replace(e[9].strip("'"),'I')
    elif e[8].strip("'") in x:
        x = x.replace(e[8].strip("'"),'H')
    elif e[7].strip("'") in x:
        x= x.replace(e[7].strip("'"),'G')
    elif e[6].strip("'") in x:
        x= x.replace(e[6].strip("'"),'F')
    elif e[5].strip("'") in x:
        x= x.replace(e[5].strip("'"),'E')
    elif e[4].strip("'") in x:
        x= x.replace(e[4].strip("'"),'D')
    elif e[3].strip("'") in x:
        x= x.replace(e[3].strip("'"),'C')
    elif e[2].strip("'") in x:
        x= x.replace(e[2].strip("'"),'B')
    elif e[1].strip("'") in x:
        x= x.replace(e[1].strip("'"),'A')

print x



