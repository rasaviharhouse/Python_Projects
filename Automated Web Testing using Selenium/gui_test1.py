from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the ChromeDriver
driver = webdriver.Edge()

try:
    # Test Case 1: Verify the existence of elements on the Home Page
    driver.get('http://127.0.0.1:8080/')
    assert driver.find_element(By.ID, 'homePage').is_displayed()
    assert driver.find_element(By.XPATH, '//h2[text()="Country App"]').is_displayed()
    assert driver.find_element(By.ID, 'cname').is_displayed()

    # Test Case 2: Verify correctness of location and size of elements on the Home Page
    home_page_element = driver.find_element(By.ID, 'homePage')
    location = home_page_element.location
    size = home_page_element.size
    print(location, size)
    assert location['x'] == 268 and location['y'] == 20
    assert size['width'] > 0 and size['height'] > 0

    # Test Case 3: Verify content of an element on the Home Page - Button
    assert driver.find_element(By.XPATH, '//button[text()="Go to Country Search"]').text == 'Go to Country Search'

    # Test Case 4: Verify correctness of the link (flow) to the Country Search Page
    driver.find_element(By.XPATH, '//button[text()="Go to Country Search"]').click()
    assert "Country Search App" in driver.title

    # Test Case 5: Execute the same set of test cases for the Country Search Page
    assert driver.find_element(By.ID, 'searchPage').is_displayed()
    assert driver.find_element(By.XPATH, '//h2[text()="Country Search Page"]').is_displayed()
    assert driver.find_element(By.ID, 'name').is_displayed()

    # Test Case 6: Search for a Country
    name_input = driver.find_element(By.ID, 'name')
    name_input.send_keys('John Doe')
    country_dropdown = driver.find_element(By.ID, 'country')
    country_dropdown.send_keys('India')
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()
    country_details = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'countryDetails')))
    assert "India" in country_details.text

    # Test Case 7: Navigate to Details Page and Provide Feedback
    home_page_button = driver.find_element(By.XPATH, "//button[text()='Go to Home']")
    home_page_button.click()
    details_page_button = driver.find_element(By.XPATH, "//button[text()='Go to Country Search']")
    details_page_button.click()
    country_dropdown = driver.find_element(By.ID, 'country')
    country_dropdown.send_keys('India')
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()
    feedback_yes_radio = driver.find_element(By.ID, 'feedback_yes')
    feedback_yes_radio.click()
    residence_country_input = driver.find_element(By.ID, 'rcname')
    residence_country_input.send_keys('United States')
    submit_button = driver.find_element(By.XPATH, "//button[text()='Go to Home']")
    submit_button.click()
    assert driver.find_element(By.ID, 'homePage').is_displayed()

    # Test Case 8: Check Slider Functionality
    age_slider = driver.find_element(By.ID, 'ageSlider')
    age_slider.click()  # Click on the slider (assuming you want to test the interaction)
    age_value = driver.find_element(By.ID, 'age').text
    assert age_value.isdigit() and 1 <= int(age_value) <= 100

finally:
    # Close the browser window
    driver.quit()
