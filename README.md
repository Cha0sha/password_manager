# Password Manager

A simple command-line password manager that securely stores and manages your passwords using encryption. This application leverages the `cryptography` library for encrypting passwords and stores them in a JSON file.

## Features

- **Add Password**: Securely store passwords associated with a service name.
- **View Passwords**: Retrieve and display stored passwords.
- **Remove Password**: Delete a password associated with a service.
- **Encryption**: Passwords are encrypted using the Fernet symmetric encryption method.

## Requirements

- Python 3.x
- `cryptography` library

You can install the required library using pip:

```bash
$ pip install cryptography
$ python3 app.py
## Eample :
Options:
1. Add Password
2. View Passwords
3. Remove Password
4. Exit
Choose an option > 1
Enter the service name: Gmail
Enter the password: my_secure_password
Password for 'Gmail' added successfully.
