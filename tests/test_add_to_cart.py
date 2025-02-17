from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def add_to_cart():

    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    addtocarts= driver.find_element(By.CLASS_NAME, "btn_inventory")
    addtocarts.click()
    carts=driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    carts.click()

    time.sleep(7)

    driver.quit()

if __name__=="__main__":
    add_to_cart()