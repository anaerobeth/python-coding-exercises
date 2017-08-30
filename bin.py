def binary(decimal) :
    otherBase = ""
    while decimal != 0 :
        otherBase  =  str(decimal % 2) + otherBase
        decimal    /=  2
    return otherBase

print binary(10)
