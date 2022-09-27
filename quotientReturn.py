#Amaan Razi HMWK #1
#quotientReturn.py


def quotientString(x,y):
    quotient = x//y
    remainder = x%y
    print ('The quotient of {} and {} is {} with a remainder of {}.'.format(x,y,quotient,remainder))

def main():
    x = int(input("Enter the first integer"))
    y = int(input("Enter the second integer"))
    quotientString(x,y)

main()
