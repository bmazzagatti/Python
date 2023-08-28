#!/usr/bin/env python3

def get_data():
    the_list = []
    while True:
        data = input("Enter data ('q' to exit): ")
        if data == "q":
            break
        the_list.append(data)   # appends data to a list
    return the_list


def main():
    data = get_data()
    f = open("output", "a")
    f.writelines(data)  # expects a list, will write every element of list into a new line of file/poened file for append
    f.close()


if __name__ == "__main__":
    main()