rajasree=[1,2,3,4,4,4,4,46,52,23,33,3,4,44,56,77,77]
print(list(set(rajasree)))


def dictionary(dict):
    print('We know the birthdays of:')
    for key in dict:
        print(key)

def main():
    Bdays = {"rajasree": "21/08/2000","jayasree": "19/05/1999","kavyasree": "26/10/2000"}
    print('Welcome to the birthday dictionary.')
    dictionary(Bdays)
    a = input("Who's birthday do you want to look up?")
    result = Bdays[a] if a in Bdays else None
    if result == None:
        print('No Data')
    else:
        print("{}'s birthday is {}".format(a, Bdays[a]))
        if _name_ == "_main_":
            main()


