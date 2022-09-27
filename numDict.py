#Amaan Razi HMWK #1
#numDict.py

def createDictionary():
    '''Numerical Dictionary'''
    number = dict()
    number['one']=1
    number['two']=2
    number['three']=3
    number['four']=4
    return number
def main():
    dict = createDictionary()
    '''I know this is not what the assignment wants but
        I wanted to try something out, the way the assignment wants it
        is just print(dict['one']), etc.'''
    print(dict[input("Enter a number one through four spelled correctly")])
   
main()
