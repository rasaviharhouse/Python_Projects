from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the EdgeDriver (make sure to provide the path to your WebDriver executable)
driver = webdriver.Edge()

try:
    # Test Case 1: Verify the existence of elements on the Country Search Page
    driver.get('http://127.0.0.1:8080/')
    assert driver.find_element(By.ID, 'searchPage').is_displayed()
    assert driver.find_element(By.XPATH, '//h2[text()="Country Search Page"]').is_displayed()
    assert driver.find_element(By.ID, 'name').is_displayed()

    # Test Case 2: Search for a Country
    name_input = driver.find_element(By.ID, 'name')
    name_input.send_keys('John Doe')
    country_dropdown = driver.find_element(By.ID, 'country')
    country_dropdown.send_keys('India')
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()
    country_details = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'countryDetails')))
    assert "India" in country_details.text

    # Test Case 3: Navigate to Details Page and Provide Feedback
    details_page_button = driver.find_element(By.XPATH, "//button[text()='Back']")
    details_page_button.click()
    country_dropdown = driver.find_element(By.ID, 'country')
    country_dropdown.send_keys('India')
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()
    feedback_yes_radio = driver.find_element(By.ID, 'feedback_yes')
    feedback_yes_radio.click()
    residence_country_input = driver.find_element(By.ID, 'rcname')
    residence_country_input.send_keys('United States')
    submit_button = driver.find_element(By.XPATH, "//button[text()='Next']")
    submit_button.click()
    assert driver.find_element(By.ID, 'homePage').is_displayed()

    # Test Case 4: Verify the existence of elements on the Home Page
    assert driver.find_element(By.ID, 'homePage').is_displayed()
    assert driver.find_element(By.XPATH, '//h2[text()="Country App"]').is_displayed()
    assert driver.find_element(By.ID, 'cname').is_displayed()

    # Test Case 5: Verify correctness of location and size of elements on the Home Page
    home_page_element = driver.find_element(By.ID, 'homePage')
    location = home_page_element.location
    size = home_page_element.size
    print(location, size)
    assert location['x'] == 116 and location['y'] == 21
    assert size['width'] > 0 and size['height'] > 0

    # Test Case 7: Verify content of an element on the Home Page - Button
    assert driver.find_element(By.XPATH, '//button[text()="Home"]').text == 'Home'

    # Test Case 8: Verify correctness of the link (flow) to the Country Search Page
    driver.find_element(By.XPATH, '//button[text()="Home"]').click()
    assert "Country Search App" in driver.title

finally:
    # Close the browser window
    driver.quit()
