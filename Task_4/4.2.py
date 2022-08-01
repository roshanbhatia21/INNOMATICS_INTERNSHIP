def swap_case(s):
    ns =''
    for i in s:
        if(i.isupper()==True):
            ns+=(i.lower())
        elif(i.islower()==True):
            ns+=(i.upper())
        elif(i.isspace()==True):
            ns+=i 
        elif(i.isnumeric()==True):
            ns+=i
        else:
            ns+=i               
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)