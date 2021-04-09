def main():
    get_stars(get_password())


def get_password():
    passw = input("Enter password: ")
    return passw


def get_stars(passw):
    for x in range(len(passw)):
        print("*", end="")


main()
