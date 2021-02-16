from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(r"chromedriver.exe")

#Open the Url
#1.find_element_by_id
# driver.get("http://amazon.com")
# driver.find_element_by_id("nav-link-accountList-nav-line-1").click()
#==============================================================
driver.get("https://morvanzhou.github.io/")
#driver.find_element_by_xpath(u"img[@alt='强化学习 (Reinforcement Learning")
time.sleep(2)
driver.find_element_by_link_text("About").click()
time.sleep(2)
driver.find_element_by_link_text(u"教程 ▾").click()
time.sleep(2)
driver.find_element_by_link_text(u"推荐学习顺序").click()

html =driver.page_source  #get html
driver.get_screenshot_as_file("./screenshot1.png")
time.sleep(2)
driver.close()
print(html[:200])
#driver.close()
# maximize the browser
# driver.maximize_window()
# driver.get("http://baidu.com")
#time.sleep(5)
#driver.minimize_window()


#Get Title
# Title = driver.title
# print(Title)

# Get current Url
# correntUrl = driver.current_url
# print(correntUrl)

#Browser Refresh
# driver.refresh()
# time.sleep(2)

#Open another Url
# driver.get('https://google.com/')
# time.sleep(2)

#Browser forward
# driver.forward()
# time.sleep(2)
#Get Page Source
# pageSource=driver.page_source
# print(pageSource)
# driver.close()
#2. find_element_by_name
# driver.find_element_by_name("q").send_keys('inty python youtube\n')



# driver.back()

#3. find_element_by_link_text
# driver.find_element_by_link_text('Gmail').click()

#4 find_element_by_partial_link
#driver.find_element_by_partial_link_text('il').click()

#5. find_elements_by_tag_name
# driver.get("http://baidu.com")
# elements=driver.find_elements_by_tag_name('a')
#
#
# for element in elements:
#     if '视频' in element.text:
#         element.click()

#6. find_element_by_class_name， 用的不多，因为class多不是唯一的
# driver.get("http://douban.com")
# driver.find_element_by_class_name('lnk-movie').click()

#7. find_element_by_xpath
# driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()

#8. find_element_by_css_selector
# driver.get("http://baidu.com")
# driver.find_element_by_css_selector("#kw").send_keys('inty youtube\n')
#driver.quit()