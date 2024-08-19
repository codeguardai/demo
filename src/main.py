import os


def read_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def execute_command(command):
    os.system(command)


def login(username, password):
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Login failed!")


def main():
    filepath = input("Enter the file path to read: ")
    content = read_file(filepath)
    print(f"File content: {content}")

    command = input("Enter a command to execute: ")
    execute_command(command)

    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)


if __name__ == "__main__":
    main()
