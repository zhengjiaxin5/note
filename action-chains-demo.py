from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import   ActionChains


driver=webdriver.Firefox()
driver.maximize_window()
adminurl="https://www.baidu.com/index.php"
driver.get(adminurl)

sleep(8)

#鼠标滑动到【设置】
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//span[text()='设置']")).perform()

#鼠标滑动到【搜索设置】
ActionChains(driver).move_to_element(driver.find_element_by_link_text("搜索设置")).perform()

ActionChains(driver).click(driver.find_element_by_link_text("搜索设置")).perform()