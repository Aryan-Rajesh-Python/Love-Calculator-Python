import pyfiglet
app=pyfiglet.figlet_format("Love Calculator")
def love_calculator():   
    print(app)
    name1=input("What is your name: ")
    name2=input("What is your partner's name: ")
    name3=(name1+name2)
    count1=0
    count2=0
    for i in name3:
        if(i=="T" or i=="t"):
            count1+=1
        if(i=="R" or i=="r"):
            count1+=1
        if(i=="U" or i=="u"):
            count1+=1
        if(i=="E" or i=="e"):
            count1+=1
    for i in name3:
        if(i=="L" or i=="l"):
            count2+=1
        if(i=="O" or i=="o"):
            count2+=1
        if(i=="V" or i=="v"):
            count2+=1
        if(i=="E" or i=="e"):
            count2+=1
    count3=(str(count1)+str(count2))
    if(int(count3)<10 or int(count3)>90):
        print(f"Your score is {count3}, you go together like coke and mentos!")
    elif(40<int(count3)<50):
        print(f"Your score is {count3}, you are alright together!")
    else:
        print(f"Your score is {count3}.")
while(True):
    choice=input("Do you want to continue using the love calculator: ")
    if(choice=="yes"):
        love_calculator()
    else:
        print("Thank you for using our application!")
        break