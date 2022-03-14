#-*- codeing = utf-8 -*-
#@Time : 2022/3/14 11:33
#@Author : qyc
#@File : wangke.py
#@Software : PyCharm Community Edition
import base64

from aip import AipOcr
from selenium import webdriver
import time
from PIL import Image
import pytesseract
from selenium.webdriver.common.keys import Keys




def get_file_content(filePath):
    """ 读取图片 """
    with open(filePath, 'rb') as f:
        return f.read()

if __name__ == '__main__':
    # 百度api
    APP_ID = '25761652'
    API_KEY = 'aOdASs7tivhsGhzV5Uyw42d1'
    SECRET_KEY = '2IRKG97oyZhayCSXjyX5S5DOaLLBqLeU'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    #chrome驱动
    driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://e.ecust.edu.cn/mh")
    driver.maximize_window()
    time.sleep(2)
    #页面截图
    file_name="D:/pythonProject/Img/test.png"
    driver.find_element_by_xpath("//input[@type='text' and @name='userName' and @id='userName' and @class='userTxt']").send_keys(Keys.TAB)
    driver.save_screenshot(file_name)


    account="2231160114"
    password="Xz237211."
    driver.find_element_by_xpath("//input[@type='text' and @name='userName' and @id='userName' and @class='userTxt']").send_keys(account)
    driver.find_element_by_xpath("//input[@type='password' and @name='passWord' and @id='passWord' and @class='userTxt fl']").send_keys(password)

    #自动填充验证码（识别出来不太准 想玩可以把下面注释放开来）
    # im=Image.open(file_name)
    # img_size=im.size
    # h = img_size[1]  # 图片高度
    # w = img_size[0]  # 图片宽度
    # x = 0.75 * w
    # y = 0.55  * h
    # w = 0.08 * w
    # h = 0.06 * h
    # img=im.crop((x,y,x+w,y+h))
    # img.save(file_name)
    # path="Img/test.png"
    # captcha=get_file_content(path)
    # result=client.basicAccurate(captcha)
    #
    # print(result)
    #
    # for text in result.get('words_result'):
    #     code_check=text.get('words')
    #     print(text.get('words'))
    #
    # codeWithOut=code_check.replace(' ','').replace('.','').replace(',','').replace('。','').replace('，','')\
    #     .replace('·','').replace('`','').replace('/','').replace('-','').replace('~','').replace('+','').replace('*','')
    #
    # driver.find_element_by_xpath("//input[@type='text' and @name='verifyCode'and @class='userTxt fl']").send_keys(codeWithOut)

    time.sleep(10)

    #登录点击
    driver.find_element_by_xpath("//a[@class='w_blue_btn tologin']").click()

    #选择课程
    time.sleep(2)
    sreach_window = driver.switch_to.frame("frame_content")
    #a=driver.find_element_by_xpath("//a[@href=‘/studyApp/setViewTime?_enctoken=5a6ed44ec8a52c0ebe8fe15a0f73604c&xkid=702846’and @class='fr topBtn']")#C语言
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/a[1]").click()#形式政策

    # c=driver.find_element_by_xpath("body > div.wrap870 > div.bxCourse > div:nth-child(6) > a.fr.topBtn")#大学英语
    # d=driver.find_element_by_xpath("body > div.wrap870 > div.bxCourse > div:nth-child(8) > a.fr.topBtn")#中国近代史纲要
    # e=driver.find_element_by_xpath("body > div.wrap870 > div.bxCourse > div:nth-child(10) > a.fr.topBtn")#计算机应用基础
    # f=driver.find_element_by_xpath("body > div.wrap870 > div.bxCourse > div:nth-child(12) > a.fr.topBtn")#离散数学
    # g=driver.find_element_by_xpath("body > div.wrap870 > div.bxCourse > div:nth-child(14) > a.fr.topBtn")#现代远程教育概论

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    #选择从第几课时开始
    driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div[1]/div[1]/h3/span[3]/a").click()
    for i in range(22):
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='iframe']"))
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='ext-gen1042']/iframe"))
        time.sleep(2)
        # 播放
        driver.find_element_by_xpath("//*[@id='video']/button").click()
        time.sleep(900)
        #暂停
        driver.find_element_by_xpath("//*[@id='video']/div[5]/button[1]").click()
        time.sleep(1)
        #获取当前进度
        jindu=driver.find_element_by_xpath("//*[@id='video']/div[5]/div[5]/div").get_attribute("aria-valuenow")
        if(jindu>80):
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[-1])
            #下一章
            driver.find_element_by_xpath("//*[@id='mainid']/div[1]/div[2]").click()




