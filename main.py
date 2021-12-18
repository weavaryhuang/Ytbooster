from selenium import webdriver
import time

no_of_driver = int(input("Enter number of drivers: "))
url = input("Enter URL: ")
time_to_refresh = int(input("Enter refresh rate in seconds: "))
drivers = []

for i in range(no_of_driver):
    drivers.append(webdriver.Chrome('Chromedriver\chromedriver.exe'))
    drivers[i].get(url)
    print("test")

while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()

