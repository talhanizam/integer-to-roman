

def intToRoman(num):
    m=["","M","MM","MMM",]
    c=["","C","C","CCC","CD","D","DC","DCC","DCCC","CM"]
    x=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    i=["","I","II","III","IV","V","VI","VII","IX"]
    #converting to roman
    thousands=m[num//1000]
    hundreds=c[(num%1000)//100]
    tens=x[(num%100)//10]
    ones=i[num%10]

    ans=(thousands+hundreds+tens+ones)

    return ans

if __name__ ==  "__main__":
    number=int(input("write  the number here:"))
    print("the number in roman is:",intToRoman(number))
    

    
    
    

