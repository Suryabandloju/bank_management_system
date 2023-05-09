
usernames=['RaviTeja','Prabhas','NTR','Surya']
userpins=['1900','2525','8978','1431']
userbalance=[50000,38387,39000,80000]

user_deposit=0
user_withdrawls=0
user=0
disk1=1

while True:
    print('*'*15,'welcome to DOI Bank',15*'*')
    print("*"*55)
    print('<===============1.Open New Account================>')
    print('<===============2.Deposit Amount  ================>')
    print('<===============3.Withdraw Amount ================>')
    print('<===============4.Balance Enquiry ================>')
    print('<===============5.Exit / Quit     ================>')
    print('*'*55)

#account opening section


    option=input('Enter your query from above :')
    if option=='1':
        no_of_users=eval(input('enter no. of users :'))
        user+=no_of_users


        while disk1<= user:
                name=input('enter username:')
                usernames.append(name)

                pin=input('enter security pin:')
                userpins.append(pin)

                opening_bal=int(input('enter opening balance to deposit:'))
                userbalance.append(opening_bal)

                print(usernames)

                print(userpins)

                print(userbalance)

                disk1+=1

                print(f'congrats {name}!.Your account has been created successfully')
                print('Your user_details are added in our bank database')


#deposition section
    elif option=='2':
        v=0
        while v<1:
            w=-1
            name=input('enter your name :')
            pin=input('enter your pin :')
            while w < len(usernames) -1:
                w=w + 1
                if name == usernames[w]:
                    if pin == userpins[w]:
                        v=v+1
                        print('Your available balance is :',userbalance[w],'Rupees')
                        print("\n")
                        user_bal = (userbalance[w])
                        user_withdrawl = eval(input("enter amount to Withdraw : "))
                        if user_withdrawl > user_bal:
                            print('insufficient funds')
                        else:
                            print('your amount withdrawn successfully')
                            user_bal-=user_withdrawl
                            userbalance[w]=user_bal
                            print('Your available balance is :',user_bal,'Rupees')
            if v<1:
                print('incorrect pin or username')

#withdrawl section

    elif option=='3':
        x=0
        while x<1:
            z=-1
            name=input('enter your name :')
            pin=input('enter your pin :')
            while z < len(usernames) -1:
                z=z + 1
                if name == usernames[z]:
                    if pin == userpins[z]:
                        x=x+1
                    print('Your available balance is :',userbalance[z],'Rupees')
                    print("\n")
                    user_bal = (userbalance[z])
                    user_withdrawl = eval(input("enter amount to deposit : "))
                    if user_withdrawl > user_bal:
                        print('insufficient funds')
                    else:
                        print('your amount deposited successfully')
                        user_bal+=user_withdrawl
                        userbalance[z]=user_bal
                        print('Your available balance is :',user_bal,'Rupees')
            if x<1:
                print('incorrect pin or username')

#enquiry

    elif option=='4':
        v=0
        while v<1:
            w=-1
            name=input('enter your name :')
            pin=input('enter your pin :')
            while w < len(usernames) -1:
                w=w + 1
                if name == usernames[w]:
                    if pin == userpins[w]:
                        v=v+1
                        print("your available balance is :",userbalance[w],'Rupees')
                        print('Thank You!')
            if v<1:
                print('Incorrect Pin or Username')


#exit section
    
    elif option == "5":
            print("Thank you for using our services!")
            print("\n")
            print("Thank You! visit again")
            break
    else:
        print("Invalid option selected by the user")
        print("Please Try again!")

           
















        



        
