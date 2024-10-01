import json
import os
import base64
from cryptography.fernet import Fernet

password_file = 'passwords.json'
key_file = 'key.key'

def generate_key():
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file_handle:
        key_file_handle.write(key)

def load_key():
    return open(key_file, 'rb').read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return base64.urlsafe_b64encode(encrypted_password).decode()  # Encode as a string

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(base64.urlsafe_b64decode(encrypted_password.encode()))  # Decode to bytes
    return decrypted_password.decode()

def load_passwords():
    if os.path.exists(password_file):
        with open(password_file, 'r') as f:
            return json.load(f)
    return {}

def save_passwords(passwords):
    with open(password_file, 'w') as f:
        json.dump(passwords, f)

def add_password(service, password):
    passwords = load_passwords()
    encrypted_password = encrypt_password(password)
    passwords[service] = encrypted_password  # Store as string
    save_passwords(passwords)
    print(f"Password for '{service}' added successfully.")

def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("No passwords stored.")
        return
    print("\nStored Passwords:")
    for service, encrypted_password in passwords.items():
        decrypted_password = decrypt_password(encrypted_password)
        print(f"{service}: {decrypted_password}")

def remove_password(service):
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for '{service}' removed successfully.")
    else:
        print(f"No password found for '{service}'.")

def main():
    if not os.path.exists(key_file):
        generate_key()

    while True:
        print("\nOptions:")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Remove Password")
        print("4. Exit")
        
        choice = input("Choose an option > ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add_password(service, password)
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            service = input("Enter the service name to remove: ")
            remove_password(service)
        elif choice == '4':
            print("Exiting the password manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
