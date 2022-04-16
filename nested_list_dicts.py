def main():

    my_list = [1, "hello", True, 4.56]
    my_dict = {"first_name": "Orlando", "lastname": "Reyes"}

    super_list = [
        {"first_name": "Orlando", "lastname": "Reyes"},
        {"first_name": "Linoska", "lastname": "Caceres"},
        {"first_name": "Elodia", "lastname": "Ruiz"},
        {"first_name": "Rosember", "lastname": "Ruiz"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)


if __name__ == "__main__":
    main()