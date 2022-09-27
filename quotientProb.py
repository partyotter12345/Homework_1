#Amaan Razi HMWK #1
#quotientProb.py



def quotientProblem(x,y):
    quotient = x//y
    remainder = x%y
    print ('The quotient of {} and {} is {} with a remainder of {}.'.format(x,y,quotient,remainder))

def main():
    x = int(input("Enter the first integer"))
    y = int(input("Enter the second integer"))
    quotientProblem(x,y)

main()
