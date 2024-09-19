from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

LOGIN = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com/"


def test_purchase():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(URL)

        driver.find_element(By.ID, "user-name").send_keys(LOGIN)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert cart_item == "Sauce Labs Fleece Jacket", f"Expected 'Sauce Labs Fleece Jacket', but got {cart_item}"

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Grzegorz")
        driver.find_element(By.ID, "last-name").send_keys("Brzęczyszczykiewicz")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        driver.find_element(By.ID, "continue").click()

        driver.find_element(By.ID, "finish").click()

        confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert confirmation_message == "Thank you for your order!", f"Expected 'Thank you for your order!', but got {confirmation_message}"

        print("Test passed successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_purchase()