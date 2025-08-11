# tests/e2e/test_e2e.py

import pytest
from app.core.config import get_settings

settings = get_settings()

@pytest.mark.e2e
def test_user_registration(page):
    # Navigate to the registration page
    page.goto("http://localhost:8000/register")

    # Fill the registration form fields (use valid data)
    page.fill("#username", "testuser123")
    page.fill("#email", "testuser123@example.com")
    page.fill("#first_name", "Test")
    page.fill("#last_name", "User")
    page.fill("#password", "StrongPass1!")
    page.fill("#confirm_password", "StrongPass1!")

    # Submit the form by clicking the Register button
    page.click("button[type=submit]")

    # Wait for the success alert to appear

    page.wait_for_selector("#successAlert:not(.hidden)", timeout=5000)

    # Verify that the success message is displayed and contains expected text
    success_text = page.inner_text("#successMessage")
    assert "Registration successful" in success_text

    # Optional: Verify that the error alert is hidden
    error_visible = not page.is_hidden("#errorAlert")
    assert error_visible is False

@pytest.mark.e2e
def test_user_login(page):
    page.goto("http://localhost:8000/login")

    page.fill("#username", "testuser123")
    page.fill("#password", "StrongPass1!")

    page.click("button[type=submit]")

    # Wait for redirect or UI element indicating login success
    page.wait_for_url("**/dashboard", timeout=5000)  # adjust URL pattern as needed

    # Confirm UI text for success
    success_text = page.inner_text("#userWelcome")
    assert "Welcome" in success_text

    # Confirm token stored in localStorage
    token = page.evaluate("() => localStorage.getItem('access_token')")
    assert token is not None and len(token) > 0

@pytest.mark.e2e
def test_register_with_short_password(page):
    page.goto("http://localhost:8000/register")

    page.fill("#username", "testuser123")
    page.fill("#email", "testuser123@example.com")
    page.fill("#first_name", "Test")
    page.fill("#last_name", "User")

    # Intentionally short password (less than required length or missing complexity)
    page.fill("#password", "Ab1!")  # example too short
    page.fill("#confirm_password", "Ab1!")

    page.click("button[type=submit]")

    # Wait for error message either from frontend or backend
    # Adjust selector based on your app's error message element
    page.wait_for_selector("#errorAlert:not(.hidden)", timeout=5000)

    # Assert error message text (example)
    error_text = page.inner_text("#errorMessage")
    assert "password" in error_text.lower()

@pytest.mark.e2e
def test_login_with_wrong_password(page):
    page.goto("http://localhost:8000/login")

    page.fill("#username", "testuser123")
    page.fill("#password", "WrongPass1!")

    page.click("button[type=submit]")

    # Wait for invalid credentials message
    page.wait_for_selector("#errorAlert:not(.hidden)", timeout=5000)

    error_text = page.inner_text("#errorMessage")
    assert "password" in error_text.lower()

