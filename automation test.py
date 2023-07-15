import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome WebDriver
        cls.driver = webdriver.Chrome()

    def test_login_success(self):
        # Load the login page
        self.driver.get("file:///D:/spm%20project1/temp.html")
        
        # Wait for the page to load
        time.sleep(2)
        
        # Find the email and password input fields
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        # Enter the login credentials
        email_input.send_keys("supraja@gmail.com")
        time.sleep(1)
        password_input.send_keys("123")
        time.sleep(1)

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for the page to load and handle the alert
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        alert.accept()

        # Wait for the page to load and check if login was successful
        
        
        self.assertEqual(alert_text, "Login successful!")
        time.sleep(2)
        self.driver.get("file:///D:/spm%20project1/supp3.html")
        
        # Wait for the page to load
        time.sleep(2)

        # Find the search input and enter a city name
        search_input = self.driver.find_element(By.CSS_SELECTOR, ".search input")
        search_input.send_keys("New York")
        time.sleep(2)

        # Find the search button and click it
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".search button")
        search_button.click()

        # Wait for the weather data to load
        time.sleep(2)
        
        # Add appropriate assertions to verify the displayed weather information

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
