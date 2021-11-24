while 1:    
    n1 = (int)(input("\nEnter first number :"))
    n2 = (int)(input("Enter second number :"))

    print("\n\nMENU\n1.LCM\n2.HCF\n3.Addition\n4.Exit\n")
    choice = (int)(input("Enter choice :"))

    if n1 > n2:
        big  = n1
        small = n2
    elif n2 > n1:
        big = n2 
        small = n1
    else:
        big = small = n1
        
    if choice == 1:
        i = 1
        while 1:
            if (small*i)%big==0:
                lcm = small * i   
                break
            i+=1
        print ("LCM of ",n1," and ",n2," is ",lcm)

    elif choice == 2:
        hcf = 1
        for i in range(1,small+1):
            if n1 % i == 0 and n2 % i == 0:
                hcf = i
        print("HCF of ",n1," and ",n2," is ",hcf)

    elif choice == 3:
        print("Sum of ",n1," and ",n2," is ",(n1+n2))

    elif choice == 4:
        exit()
    else:
        print("Wrong choice")

