from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
chrome_driver_path=r"C:\Users\91623\Downloads\Development\chromedriver.exe"
ser=Service(chrome_driver_path)
driver=webdriver.Chrome(service=ser)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# num=driver.find_element(By.XPATH,value="//*[@id='articlecount']/a[1]")

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(), options=options)

driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3413150810&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&refresh=true")
sign_in=driver.find_element(By.XPATH,value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
email=driver.find_element(By.XPATH,value="//*[@id='username']")
email.send_keys("iamop555555@gmail.com")
time.sleep(5)
password=driver.find_element(By.XPATH,value="//*[@id='password']")
password.send_keys("32145678p")
time.sleep(5)
submit=driver.find_element(By.XPATH,value="//*[@id='organic-div']/form/div[3]/button")
submit.click()
time.sleep(5)
job_list=driver.find_elements(By.CSS_SELECTOR,value=".jobs-search-results__list-item")
print(job_list)
for num in range(0,len(job_list)):
    try:
        job_found=driver.find_element(By.CLASS_NAME,value=f"jobs-search-two-pane__job-card-container--viewport-tracking-{num}")
        job_found.click()
        time.sleep(10)
    except NoSuchElementException:
        print("No Easy Apply Job Found")
        continue

    else:
        save=driver.find_element(By.XPATH,value="//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
        if save.text=="Save":
            save.click()
            time.sleep(10)
#         time.sleep(5)
#         easy_apply=driver.find_element(By.XPATH,value="//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div")
#         easy_apply.click()
#         time.sleep(5)
#         # phone_num=driver.find_element(By.ID,value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3417282436-78323507-phoneNumber-nationalNumber")
#         # if phone_num.text == "":
#         #     phone_num.send_keys("6238598850")
#         next_but=driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Continue to next step']")
#         next_but.click()
#         time.sleep(5)
#         resume=driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Choose Resume']")
#         resume.click()
#         time.sleep(5)
#         next_but_encore=driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Continue to next step']")
#         next_but_encore.click()
#         time.sleep(5)
#         try:
#             additional_question=driver.find_element(By.XPATH,value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3417282436-78323499-numeric']")
#             additional_question.send_keys(2)
#             time.sleep(5)
#         except NoSuchElementException:
#             print("what")
#         else:
#             review=driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Review your application']")
#             review.click()
#             js.executeScript("arguments[0].scrollIntoView();", Element)
#             time.sleep(100000000000000)
# #
# #
