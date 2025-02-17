from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_check_out():

    driver=webdriver.Chrome()
    time.sleep(2)
    driver.maximize_window()


    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    addtocarts= driver.find_element(By.CLASS_NAME, "btn_inventory")
    addtocarts.click()
    time.sleep(2)
    carts=driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

    carts.click()
    time.sleep(2)
    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    time.sleep(2)
    first_name=driver.find_element(By.ID,"first-name")
    last_name=driver.find_element(By.ID,"last-name")
    postal_code=driver.find_element(By.ID, "postal-code")
    time.sleep(2)
    first_name.send_keys("arun")
    time.sleep(2)
    last_name.send_keys("kumar")
    time.sleep(2)
    postal_code.send_keys("700 134")
    time.sleep(2)

    continue_order=driver.find_element(By.CSS_SELECTOR,"#continue")
    continue_order.click()
    time.sleep(2)

    finish_order=driver.find_element(By.XPATH,"//button[@id='finish']")
    finish_order.click()
    time.sleep(2)

    print("Thank you for your order!")



    time.sleep(7)

    driver.quit()

if __name__=="__main__":
    test_check_out()




