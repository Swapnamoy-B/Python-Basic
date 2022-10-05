while(True):
    print("press q to quit\n")
    a = input("Enter a number\n")
    if a == 'q':
        break
    try:
        print("trying")
        a=int(a)
        if a>6:
            print("You have entered a number greater than 6")
    except Exception as e:
        print(f"Your iput resulted in an error : {e}")

print("thanks for playing")