# Password Manager

The password manager is a Python project designed to securely store and manage user passwords. It provides functionalities for storing passwords for various accounts, generating strong passwords, and retrieving passwords when needed.

## Scope

The project involves the implementation of encryption algorithms to ensure the secure storage of passwords. It includes the design of a user interface for inputting and retrieving passwords and the development of functions for generating strong passwords and managing them in a database.

## Libraries Used

### Cryptography

The `cryptography` package provides cryptographic recipes and primitives in Python. It is used in this project for encrypting and decrypting user passwords.

Installation:
```bash
pip install cryptography
```

Documentation: [cryptography Documentation](https://cryptography.io/en/latest/)

### Database

MySQL is a fast, reliable, and easy-to-use database system where data is stored in tables. In this project, it is used to store and maintain data received from users.

Installation:
```bash
pip install mysql-connector-python
```

Documentations:
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [mysql-connector-python Documentation](https://dev.mysql.com/doc/connector-python/en/)

### Hashing

The `hashlib` module implements a common interface to many different secure hash and message digest algorithms. It is used in this project to hash the master password and verify it.

Documentation: [hashlib Documentation](https://docs.python.org/3/library/hashlib.html)

### Graphical User Interface

Tkinter is the standard GUI library for creating GUI applications in Python. It is used in this project to create a simple graphical user interface for the application.

Documentation: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/another-person/password-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-manager
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main Python script to start the password manager:

   ```bash
   python password_manager.py
   ```

2. Follow the on-screen instructions to register or log in to your account.

3. Once logged in, you can perform various actions such as adding, updating, or deleting passwords for different accounts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to OpenAI for providing the GPT model used to generate this README template.
