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
    # 百度智能云api
    #APP_ID = ''
    #API_KEY = ''
    #SECRET_KEY = ''
    #client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    #chrome驱动
    driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://e.ecust.edu.cn/mh")
    driver.maximize_window()
    time.sleep(2)
    #页面截图
    file_name="D:/pythonProject/Img/test.png"
    #driver.find_element_by_xpath("//input[@type='text' and @name='userName' and @id='userName' and @class='userTxt']").send_keys(Keys.TAB)
    #driver.save_screenshot(file_name)


    account=""   #学号
    password=""  #密码
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

    #选择课程 ，刷哪个放出来哪个，其余注释掉
    time.sleep(2)
    sreach_window = driver.switch_to.frame("frame_content")
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[1]")#C语言
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/a[1]").click()#形式政策
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/a[1]")#大学英语
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[4]/a[1]")#中国近代史纲要
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[5]/a[1]")#计算机应用基础
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[6]/a[1]")#离散数学
    #driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[7]/a[1]")#现代远程教育概论

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)
    #选择从第几课时开始,F12复制第几课时的xpath路径放入下面双引号中
    driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div[3]/div[1]/h3/span[3]/a").click()
    for i in range(22):
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='iframe']"))
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='ext-gen1042']/iframe"))
        time.sleep(2)
        # 播放
        driver.find_element_by_xpath("//*[@id='video']/button").click()
        time.sleep(600)
        for i in range(20):
            #暂停
            driver.find_element_by_xpath("//*[@id='video']/div[5]/button[1]").click()
            time.sleep(1)
            #获取当前进度
            jindu=int(float(driver.find_element_by_xpath("//*[@id='video']/div[5]/div[5]/div").get_attribute("aria-valuenow")))
            print(jindu)
            time.sleep(1)
            if (jindu<50):
                driver.find_element_by_xpath("//*[@id='video']/div[5]/button[1]").click()
                time.sleep(600)
                break
            if(jindu>=70 or jindu<=1):
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                #下一章
                driver.find_element_by_xpath("//*[@id='mainid']/div[1]/div[2]").click()
                break
            else:
                #播放
                driver.find_element_by_xpath("//*[@id='video']/div[5]/button[1]").click()
                time.sleep(120)



