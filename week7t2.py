def main():
    while True:
        try:
            number = int(input("Enter a number between 1 and 50: "))
            if 1 <= number <= 50:
                if number % 3 == 0 and number % 5 == 0:
                    print("PapaMama")
                elif number % 3 == 0:
                    print("Papa")
                elif number % 5 == 0:
                    print("Mama")
                else:
                    print(number)
                break
            else:
                print("Error: Number must be between 1 and 50. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
