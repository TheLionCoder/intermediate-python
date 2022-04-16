from math import floor


def main():
    cube_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(cube_dict)

    squares_dict = {i: floor(i**(1/2)) for i in range(1, 1001)}
    print(squares_dict)


if __name__ == "__main__":
    main()