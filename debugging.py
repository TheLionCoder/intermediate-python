def divisors(num):
    divisors = [i for i in range (1, num + 1) if num % i == 0]
    return divisors


def main():
    try:
        num = int(input("please type a num: \n"))
        print(divisors(num))
        print("Finish.")

    except ValueError:
            print("Please type only numbers.")


if __name__ == "__main__":
    main()