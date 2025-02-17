from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def sauce_demo():

    driver=webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    print(driver.title)

    username_field=driver.find_element(By.ID,"user-name")
    password_field=driver.find_element(By.ID,"password")
    login_button=driver.find_element(By.ID,"login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    assert "Products" in driver.page_source


    time.sleep(15)
    driver.quit()








if __name__=="__main__":
    sauce_demo()