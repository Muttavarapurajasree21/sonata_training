def file():
    try:
        r=open('age1.txt','r')
        print(r.read())
    except(FileNotFoundError):
        return ('not exists')
emp=file()
print(emp)