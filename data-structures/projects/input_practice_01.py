while True:
    try:
        n = int(input("Введите целое число:"))
        break
    except ValueError:
        print("Error: This is not a complete number")

print("Your input:", n)
