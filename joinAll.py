#Amaan Razi HMWK #1
#joinAll.py

def joinStrings(stringList):
   
    stringsum = ""
    for string in stringList :
        stringsum = stringsum + string
    return stringsum
    


def main():
    print(joinStrings(['very', 'hot', 'day']))
    print(joinStrings(['this', 'is', 'it']))
    print(joinStrings(['1', '2', '3', '4', '5']))

main()
