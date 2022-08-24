def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        A=n%10
        rev=rev*10+A
        n=n//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
palindrome(1121)