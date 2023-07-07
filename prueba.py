def num_primo (num):
    d=2
    list1=[]
    while d<=num:
        if num%d==0:
            num=num/d
            list1.append(d)
        else:
            d +=1
    return list1
        
resultado=int(input("Dame un numero: "))
salida=num_primo(resultado)
print (salida)