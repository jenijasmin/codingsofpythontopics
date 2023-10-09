tam=int(input("Enter the tamil marks:"))
eng=int(input("Enter the english marks:"))
mat=int(input("Enter the maths marks:"))
total=tam+eng+mat
avg=total/3.0
print("Total=",total)
print("Average=",avg)
if tam>=35 and eng>=35 and mat>=35:
    print("pass")
    if avg>=90 and avg<=100:
        print("grade:A")
    elif avg>=80 and avg<=89:
        print("grade:B")
    elif avg>=70 and avg<=79:
        print("grade:D")
    else:
        print("no grade")
else:
    print("fail")
    print("no grade") 
    
        
