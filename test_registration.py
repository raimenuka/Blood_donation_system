import pytest
from home import home  # Import your application module

@pytest.fixture
def app():
    # Initialize your application or create an instance of the BloodDonationApp
    app = home()
    return app

def test_successful_registration(app):
    # Simulate a successful user registration
    user_info = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "secure_password"
    }
    
    registration_result = app.register_user(user_info)
    
    assert registration_result == "Registration successful"

def test_duplicate_registration(app):
    # Simulate a registration attempt with duplicate email
    user_info = {
        "username": "duplicate_user",
        "email": "test@example.com",
        "password": "another_password"
    }
    
    registration_result = app.register_user(user_info)
    
    assert registration_result == "Email already exists"

def test_login_success(app):
    # Simulate a successful user login
    login_credentials = {
        "email": "test@example.com",
        "password": "secure_password"
    }
    
    login_result = app.login_user(login_credentials)
    
    assert login_result == "Login successful"

def test_login_failure(app):
    # Simulate a login attempt with incorrect credentials
    login_credentials = {
        "email": "test@example.com",
        "password": "incorrect_password"
    }
    
    login_result = app.login_user(login_credentials)
    
    assert login_result == "Login failed"

if __name__ == "__main__":
    pytest.main()
