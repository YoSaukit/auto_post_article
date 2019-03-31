# coding:utf-8


from selenium import webdriver
import time

user_main_url = 'https://my.oschina.net/u'

username = '*******'
password = '********'

url = 'https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fmy.oschina.net%2Fu%2F564070%2Fblog'

driver = webdriver.Firefox()
driver.get(url)

# 浏览器窗口最大化
driver.maximize_window()

driver.find_element_by_id('userMail').send_keys(username)
driver.find_element_by_id('userPassword').send_keys(password)
driver.find_element_by_xpath('//*[@id="account_login"]/form/div/div[5]/button').click()


# 进入主页
while True:
    # 判断是不是在个人主页中。
    if user_main_url in driver.current_url:
        break
    else:
        # 不在个人主页中就继续加载了。
        time.sleep(1)


# 点击进入写作页。
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/div[4]/a').click()

time.sleep(1)

# 填写标题
titleInput = driver.find_element_by_xpath('//*[@id="title"]')
titleInput.send_keys(u'666666模333444444')

# 填写内容
contentInput = driver.find_element_by_id('mdeditor')
contentInput.send_keys(u'666666模拟3334444422222。。。。。')



#通过网页源代码可以查看value=428612正好对应着前端开发。
# 选择文章的类型值，
js = 'document.getElementById("sys_sort").value="428612";'
driver.execute_script(js)


# 修改选择的类型文本
js = 'document.getElementsByClassName("select-show")[2].innerText="前端开发";'
driver.execute_script(js)


# 点击提交
submit = driver.find_element_by_xpath('//*[@id="blog-form"]/div[3]/div/button[2]')
submit.click()

print('发布成功！')