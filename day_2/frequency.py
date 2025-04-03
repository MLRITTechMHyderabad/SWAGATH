def freq(a):
    dict={}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)

number=[1,1,1,2,3,5,5,5,6]
freq(number)
