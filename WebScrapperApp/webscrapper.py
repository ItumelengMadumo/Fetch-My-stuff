from selenium import webdriver

url="https://www.news24.com/sport"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_path('//*[@id="main-content"]/header/div/a/img').click()