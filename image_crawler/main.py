from selenium import webdriver

search_term = '박효신'
url = "https://www.google.co.in/search?q=" + search_term + "&tbm=isch"

browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)

for i in range(200):
    browser.execute_script('window.scrollBy(0,10000)')

for idx, el in enumerate(browser.find_elements_by_class_name("rg_ic")):
    el.screenshot(str(idx) + ".png")

browser.close()

first_list = ['박효신', '대장나무', '효신']
second_list = ['공연', '직캠', '얼굴', '노래', '콘서트']

for first in first_list:
    for second in second_list:
        new_query = first + " " + second
        url = "https://www.google.co.in/search?q=" + new_query + "&tbm=isch"
        browser.get(url)
        ...



