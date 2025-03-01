# Banking Application

A secure and user-friendly banking application built with Django that allows users to manage their accounts, perform transactions, and track their financial history.

## Features

- User Authentication and Authorization
- Account Management
- Transaction History
- Money Transfer Capabilities
- Secure Banking Operations
- Responsive Web Interface

## Tech Stack

- Python 3.x
- Django Web Framework
- HTML/CSS
- PostgreSQL

## Project Structure

```
Fi/
├── accounts/           # User authentication and account management
├── bank/              # Core banking functionality
├── templates/         # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── money.html
│   └── history.html
└── Fi/                # Project configuration
```

## Setup and Installation

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```
     .venv\Scripts\activate
     ```

3. Install dependencies:
   ```
   pip install django
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Register a new account through the signup page
2. Log in with your credentials
3. Access banking features:
   - View account balance
   - Make transfers
   - Check transaction history

## Security Features

- Secure user authentication
- Protected transaction processing
- Form validation and sanitization
- Session management

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
