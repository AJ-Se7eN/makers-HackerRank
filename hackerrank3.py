num=int(input())
for i in range(num):
    a=input()   
    b=input()
    result = list(set(a) & set(b))
    if len(result) >0 :
       print("YES")
    elif len(result)==0:
        print ("NO")
