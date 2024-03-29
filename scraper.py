# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time



# Defines function for retrieving vehicle details
def retrieve_vehicle_details(vehicle_plate) -> str:
    # Define executable path for chrome driver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Define website
    driver.get("https://vrl.lta.gov.sg/lta/vrl/action/pubfunc?ID=EnquireRoadTaxExpDtProxy")

    # Exception handler for service being down
    try:
        # Wait for input_element to appear
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "vehNoField"))
        )

    except TimeoutException:
        # Return error
        return "-1", "", ""
    
    # Selects, clears and enters vehicle plate into textbox
    input_element = driver.find_element(By.ID, "vehNoField")
    input_element.clear()
    input_element.send_keys(vehicle_plate)

    # Clicks terms checkbox
    terms_element = driver.find_element(By.ID, "agreeTCbox")
    terms_element.click()

    # Clicks next
    next_element = driver.find_element(By.ID, "btnNext")
    next_element.click()

    # Exception handler for "No records found"
    try:
        # Wait for results element to appear
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[3]/div[4]/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div[2]/p"))
        )
    except TimeoutException:
        # Return error
        return "0", "", ""

    # Retrieve results
    vehicle_model = driver.find_element(By.XPATH, "/html/body/section/div[3]/div[4]/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div[2]/p").text
    road_tax_expiry = driver.find_element(By.CLASS_NAME, "vrlDT-content-p").text

    # Exit browser
    driver.quit()
    
    # Return results
    return "1", vehicle_model, road_tax_expiry



# Defines main program
def main(vehicle_plate) -> None:

    status_code, vehicle_model, road_tax_expiry = retrieve_vehicle_details(vehicle_plate)

    # Print results
    if  status_code == "1":
        results = f"{vehicle_plate.upper()}\n{vehicle_model}\n{road_tax_expiry}"
        return results
    
    elif status_code == "0":
        return"No record found!"
    
    else:
        return "Service may be down, try again later!"



if __name__ == "__main__":
    vehicle_plate: str = input("Enter a vehicle plate: ")
    print(main(vehicle_plate))