import re
x=input().split(",")
for i in range(0,len(x)):
    x1 = re.findall("[a-z]", x[i])
    x4 = re.findall("[A-Z]", x[i])
    x5 = re.findall("[0-9]", x[i])
    x2 = re.findall("[*$_#=@]", x[i])
    x3 = re.findall("[%!)(]", x[i])
    if len(x[i])<6:
        print(x[i],"Failure Password must be at least 6 characters long.")
    elif len(x[i])>12:
        print(x[i],"Failure Password must be at max 12 characters long.")
    elif (not x1):
        print(x[i],"Failure Password must contain at least one letter from a-z.")
    elif (not x2):
        print(x[i],"Failure Password must contain at least one letter from [*$_#=@].")
    elif (not x4):
        print(x[i],"Failure Password must contain at least one letter from A-Z.")
    elif (not x5):
        print(x[i],"Failure Password must contain at least one letter from 0-9.")
    elif (x3):
        print(x[i],"Failure Password cannot contain %!)(.")
    else:
        print("success")

  
