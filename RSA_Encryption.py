import random
def PGP_encryption():
    p=input("enter the 1st prime number:")#prompts the user to enter the value for p
    q=input("enter the 2nd prime number:")#prompts the user to ented the value for q
    message=input("enter message:")

    def isPrime(n):         #this function ristricts the user to only enter prime numbers
        for i in (range (2,n)):
            if n%i==0:
                return False
            return True
    if isPrime (int(p))==False or isPrime(int(q))==False:
        return "not prime numbers"           #if and of the numbers are not prime  the system prompts the user
    return encrypt(int(p),int(q),str(message))#if the numbers entered are prime the function the runs the encrypt function
            

def encrypt(p,q,string):      #Main encryption algorithm
    n=p*q                    #calculate the value for n which is the product of p x q
    z=(p-1)*(q-1)             #calculate the value for z which represent phi n

    def gcd(x, y):            #this is the general function the computes the greatest common divisor between two numbers
        while x != 0:
            (x, y) = (y % x, x)
        return y


    for i in range (2,n):    #this function computes the value fo e which is relatively prime to z 
        if gcd(i,z)==1:
            e=i
 
    
    def Extended_Euclid(m,n):# this function utilizes the gcd function to compute the value for d using modulo inverse 
        if gcd(m,n)!=1:
            return "Invalid"
        A1,A2,A3 = 1,0,m
        B1,B2,B3 = 0,1,n
        while B3!=0:
            Q = A3//B3
            T1,T2,T3 = A1-Q*B1,A2-Q*B2,A3-Q*B3
            A1,A2,A3 = B1,B2,B3
            B1,B2,B3 = T1,T2,T3
            d=A1%n
        return d
    print ("The values for n :", n,",The value for e:",e,",The value for z:",z,",The value for d:",Extended_Euclid(e,z))
 
    x=[]
    for i in range(0,len(string)): #perform conversions to produce the encrypted message in string format
        x+=[ord(string[i])]
    msg=[]
    for a in x:
        c=(a**e)%n
        msg+=[c]
    fin_msg=""
    for ele in msg:
        fin_msg+=str(ele)+ " "
    print("Message:")
    print (fin_msg)
    

    def decrypt(fin_msg,n,z,e):# decrypts the encrypted message
        dec_msg=""
        msg=fin_msg.split(" ")
        d=(Extended_Euclid(e,z))
        for i in range (0,len( msg)-1):
            m= int((int(msg[i])**d)%n)
            dec_msg+=chr(m)           
        return dec_msg
    print ("Decrypted Message : ")
    return decrypt(fin_msg,n,z,e)      









        
    
    

    
 
    


 














        
        

    



              
