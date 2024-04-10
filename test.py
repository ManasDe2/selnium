from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("file:///var/lib/jenkins/workspace/selniumtest/index.html ")
  
try:
    # Find the input elements
    input1 = driver.find_element(By.ID, 'input1')
    time.sleep(1)
    input2 = driver.find_element(By.ID, 'input2')
    time.sleep(1)

    # Input values
    input1.send_keys("3")
    input2.send_keys("5")

    # Find the submit button and click it
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Wait a bit for the result to appear
    time.sleep(1)

    # Find and print the output
    output = driver.find_element(By.ID, 'output')
    print("Actual Output:", output.text)
    if output.text[-1] == '8':
        print("Test Passed ")
    else:   
        print("Test failed")

finally:
    # Close the browser
    driver.quit()
