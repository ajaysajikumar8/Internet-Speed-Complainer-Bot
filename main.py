import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH =  "E:\chromedriver_win32\chromedriver.exe"
PROMISED_DOWN = 15
PROMISED_UP = 5
USER_NAME = ""
PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        cookie_enable = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_enable.click()
        time.sleep(1)
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(50)
        self.down = int(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(f"Download Speed: {self.down}")
        self.up = int(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"Upload Speed: {self.up}")

        print("Recieved internet speed")


    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")

        time.sleep(3)
        signin_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        signin_btn.click()

        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(USER_NAME)
        email.send_keys(Keys.ENTER)

        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        compose_msg  = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_msg.click()

        time.sleep(3)
        input_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for 15down/5up")
        time.sleep(2)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        tweet_btn.click()
        
        time.sleep(2)
        print("Tweet posted")
        self.driver.quit()



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
if bot.down < 15 or bot.up < 5:
    bot.tweet_at_provider()
else:
    bot.driver.quit()

