#导入webdriver模块
from selenium import webdriver
from time import sleep
#打开Chrome浏览器
driver = webdriver.Chrome()
#打开网址
driver.get('http://test2www.comjia.com/project/s')
sleep(2)
#设置窗口尺寸
driver.set_window_size(1000,2000)
sleep(2)
#设置最大化窗口
driver.maximize_window()
#打开网址
driver.get('http://test2www.comjia.com/project/3.html')
sleep(2)
#返回上一页
driver.back()
#返回下一页
driver.forward()
#截图
driver.get_screenshot_as_file('D:\\360downloads\q1.png')
#退出浏览器
driver.quit()


