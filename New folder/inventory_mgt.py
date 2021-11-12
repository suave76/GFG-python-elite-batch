import json
import time

fd=open("Record.json",'r')
js=fd.read()
fd.close()

dct=json.loads(js)

for i in dct:
    print(i,dct[i])

print()
u_id=(input('enter product ID           : '))
u_qt=int(input('enter quantity          : '))
u_name=input('enter your name           : ')
u_phoneNo=input('enter your phone No    : ')
u_email=input('enter your email         : ')


if u_id in dct:
    if u_qt<=dct[u_id]['Qn']:
        print("-"*15)
        print("Name     :" , dct[u_id]['Name'])
        print("Price    :" ,dct[u_id]['Price'])
        print("Quantity :" ,u_qt)
        print("-"*15)
        print("Total    :" ,dct[u_id]['Price'] * u_qt)
        print("CGST     :" ,(dct[u_id]['Price'] * u_qt)*.09)
        print("SGST     :" ,(dct[u_id]['Price'] * u_qt)*.09)
        print("-"*15)
        print("Sub Total:" ,(dct[u_id]['Price'] * u_qt) + (dct[u_id]['Price'] * u_qt)*.18)
        print("-"*15)
        
        dct[u_id]['Qn']-=u_qt

        txn = dct[u_id]['Name']+","+str(dct[u_id]['Price'])+","+str(u_qt)+","+str((dct[u_id]['Price'] * u_qt) + (dct[u_id]['Price'] * u_qt)*.18)+","+time.ctime()+","+u_name+","+u_phoneNo+","+u_email+"\n"
        
    else:
        print()
        print('-'*25)
        print('Sorry, we do not have the requested quantity')
        print('would you like to have',dct[u_id]['Qn'],'of them?')
        print('Yes: 1  ;  No: 0')
        ch=int(input())
        if ch==1:
            print("-"*15)
            print("Name     :" , dct[u_id]['Name'])
            print("Price    :" ,dct[u_id]['Price'])
            print("Quantity :" ,dct[u_id]['Qn'])
            print("-"*15)
            print("Total    :" ,dct[u_id]['Price'] *dct[u_id]['Qn'] )
            print("CGST     :" ,(dct[u_id]['Price'] *dct[u_id]['Qn'])*.09)
            print("SGST     :" ,(dct[u_id]['Price'] *dct[u_id]['Qn'])*.09)
            print("-"*15)
            print("Sub Total:" ,(dct[u_id]['Price'] *dct[u_id]['Qn']) + (dct[u_id]['Price'] *dct[u_id]['Qn'])*.18)
            print("-"*15)

            dct[u_id]['Qn']=0

            txn = dct[u_id]['Name']+","+str(dct[u_id]['Price'])+","+str(dct[u_id]['Qn'])+","+str((dct[u_id]['Price'] * dct[u_id]['Qn']) + (dct[u_id]['Price'] * dct[u_id]['Qn'])*.18)+","+time.ctime()+","+u_name+","+u_phoneNo+","+u_email+"\n"
            
        
        else:
            print('Sorry for the inconvenience')
    print('-'*15,'THANK YOU','-'*15)

    x=json.dumps(dct)
    fd=open("Record.json",'w')
    fd.write(x)
    fd.close()

    fd=open('Sales.txt','a')
    fd.write(txn)
    fd.close()
    
else:
    print('product unavailable')
    
