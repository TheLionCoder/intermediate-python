def divisors(num):
    divisors = [i for i in range (1, num + 1) if num % i == 0]
    return divisors


def main():

    num = input("please type a num: \n")
    assert num.isnumeric() and int(num) > 0, "Please type only numbers and positive ones."
    print(divisors(int(num)))
    print("Finish.")


if __name__ == "__main__":
    main()