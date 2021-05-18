import random
print()
print('*****Guess the number between 0 and 100*****')
n=random.randint(1,100)
g=0

while(True):
    try:
        a=int(input("Enter the number: "))
        if(a>=0 and a<=100):
            if(a==n):
                print(f"Your guess is correct. The number is {n}")
                g=g+1
                break
            elif(a>n):
                print("Your guess is wrong. Enter a smaller number")
                g=g+1
            else:
                print("Your guess is wrong. Enter a larger number")
                g=g+1
        else:
            print("Invalid number. Enter a number between 0 and 100")

    except Exception as e:
        print(e)

print(f'You took {g} guesses')
