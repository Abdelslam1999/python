from cryptography.fernet import Fernet
import os

# Function to generate and write a new key to key.key file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from key.key file
def load_key():
    if not os.path.exists("key.key"):
        write_key()  # Generate key if it doesn't exist
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Load the key and create a Fernet instance
key = load_key()
fer = Fernet(key)

# Function to view stored passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("No passwords file found. Add a password first.")
    except Exception as e:
        print("An error occurred:", e)

# Function to add a new password
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
