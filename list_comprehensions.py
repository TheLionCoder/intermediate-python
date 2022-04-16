def main(): 

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

    four_times = [i for i in range(1, 1001) if i % 36 ==0 ]
    print(four_times)


if __name__ == "__main__":
    main()
