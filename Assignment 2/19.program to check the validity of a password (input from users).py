print("To check validity of password:")
l, u , d , s = 0 , 0 , 0 , 0
Password = '@@@@@aA1234'
lowercasealphabets='asdfghjklpoiuytrewqzxcvbnm'
uppercasealphabets='ASDFGHJKLPOIUYTREWQZXCVBNM'
digits="0123456789"
specialchar='!@#$%^&*'
if (len(Password) >= 8):
    for i in Password:
        if (i in lowercasealphabets):
            l+=1
        if (i in uppercasealphabets):
            u+=1    
        if (i in digits):
            d+=1    
        if (i in specialchar):
            s+=1
if (l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(Password)):
    print("Password is valid")   
else:
    print("Password is  not valid")