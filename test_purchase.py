import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


LOGIN = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def driver():
    """Фикстура для настройки и закрытия веб-драйвера."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def login(driver):
    """Функция для авторизации на сайте."""
    driver.get(URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    driver.find_element(By.ID, "user-name").send_keys(LOGIN)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


def add_item_to_cart(driver):
    """Добавление товара в корзину."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
    ).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text
    assert cart_item == "Sauce Labs Fleece Jacket", f"Expected 'Sauce Labs Fleece Jacket', but got {cart_item}"


def checkout(driver):
    """Оформление заказа."""
    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Grzegorz")
    driver.find_element(By.ID, "last-name").send_keys("Brzęczyszczykiewicz")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    assert confirmation_message == "Thank you for your order!", \
        f"Expected 'Thank you for your order!', but got {confirmation_message}"


def test_purchase(driver):
    login(driver)
    add_item_to_cart(driver)
    checkout(driver)