from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver= webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S1812444223%3A1673330944077895&_ga=2.145603890.723131224.1673330929-641346847.1673330929&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&ltmpl=meet&o_ref=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh5xKaI7cYw74R3vgTiNzCDPFsTopDYsa1g9A5hJHAGsJ6rnnX8VKbRhqsn5I1ZbExoyHXHp") #replace video which you want to report it....

time.sleep(5)

driver.find_element_by_id("identifierId").send_keys('arjunrror') #gmail send

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() #next button click

time.sleep(2)

driver.find_element_by_name("Passwd").send_keys('gfgc@#$1') #password send

time.sleep(2)

driver.find_element(By.ID, "passwordNext").click() #next button

time.sleep(3)

driver.get("https://meet.google.com/bqn-jtvw-ayu") #google meet link here

time.sleep(7)

driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div[1]/div[1]/button/span').click() #ask to join button click

time.sleep(30)