species = []
dbh=[]
stemnumnber = []
ans = 'y'
ans  = str(input('do you want to add a record? y/n'))

while ans=='y':
    sp = str(input('scientific name of the species?'))
    d= float(input('diameter at breast hight in cm?'))
    st = int(input('number of stems?'))
    species.append(sp)
    dbh.append(d)
    stemnumnber.append(st)
    if ans =='n':
        break 
print(species,dbh,stemnumnber)