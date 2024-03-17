from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("file:///var/lib/jenkins/workspace/selniumtest/index.html")  

try:
    # Find the input elements
    input1 = driver.find_element_by_id("input1")
    input2 = driver.find_element_by_id("input2")

    # Input values
    input1.send_keys("3")
    input2.send_keys("5")

    # Find the submit button and click it
    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

    # Wait a bit for the result to appear
    time.sleep(1)

    # Find and print the output
    output = driver.find_element_by_id("output")
    print("Result:", output.text)

finally:
    # Close the browser
    driver.quit()