from selenium import webdriver
import time
'''
CURSOR = 15
GRANDMA = 100
FACTORY = 500
MINE = 2000
SHIPMENT = 7000
ALCHEMYLAB = 50000
PORTAL = 100000
TIMEMACHINE = 123456789
'''

chrome_driver_path = "C:/Users/sri/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout_min=time.time() + 60*5
timeout_sec = time.time()+5

while True:
    cookie.click()

    if time.time() > timeout_sec:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)
        cookie_upgrade = {}
        for i in range(len(item_prices)):
            cookie_upgrade[item_prices[i]] = items_ids[i]
        money_element =driver.find_element_by_id("money").text

        if "," in money_element:
            money_element = money_element.replace(",","")
            print(money_element)
        money = int(money_element)

        affordable_upgrades = {}
        for cost,id in cookie_upgrade.items():
            if money > cost:
                affordable_upgrades[cost]= id

        highest_price_affordable_upgrade = max(affordable_upgrades)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()

        timeout_sec=time.time() + 5

    if time.time() > timeout_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        break











