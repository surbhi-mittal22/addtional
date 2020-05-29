largest = -1
smallest =None
num=0

while True:
    num = input("Enter a number: ")
    if(num =='done'):
        break
    
    
    try:
        n=int(num)
    except:
        print("Invalid input")
        continue

    if(n>largest):
       largest=n
    
    if( smallest  is None):
        smallest=n
    elif(n<smallest):
       smallest=n
    
n=n+1
print("Maximum is", largest)
print("Minimum is", smallest)
        