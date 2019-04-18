import time
import authorize
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# 简书
class JianShu(object):
    @staticmethod
    def post(main, timeout, self_timeout=3):
        # 1.跳转登陆
        login = 'https://www.jianshu.com/sign_in'
        driver = webdriver.Chrome()
        driver.get(login)

        # 2.窗口最大化
        driver.maximize_window()

        # 3.使用QQ授权登录
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/ul/li[3]/a/i').click()
        driver.close()
        authorize.qq(driver, timeout)

        # 4.点击"写文章"
        write_blog = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('/html/body/nav/div/a[2]'))
        write_blog.click()
        driver.close()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

        # 5.点击指定分类
        classify = WebDriverWait(driver, timeout).until(lambda d: d.find_elements_by_class_name('_3DM7w'))
        for c in classify:
            html = c.get_attribute('innerHTML')
            if main.category in html:
                c.click()
            else:
                # TODO 如果分类不存在，还可以直接新建分类
                pass

        # 6.点击'新建文章'
        time.sleep(self_timeout)
        new_article = WebDriverWait(driver, timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/div[1]/i'))
        new_article.click()
        article = WebDriverWait(driver, timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/ul/li[1]'))
        article.click()

        # 7.填写标题, 内容
        time.sleep(self_timeout)
        title = driver.find_element_by_class_name('_24i7u')
        title.clear()
        title.send_keys(main.title)
        content = driver.find_element_by_id('arthur-editor')
        content.clear()
        content.send_keys(main.content)

        # 7.1 插入图片
        time.sleep(self_timeout)
        insert_img = driver.find_element_by_class_name('_2zLpt')
        insert_img.click()
        #（1）本地图片
        # img = driver.find_element_by_id('kalamu-upload-image')
        # img.send_keys('/Users/didi/Documents/PycharmProjects/jianshu/test.jpg')
        #（2）网络图片
        driver.find_element_by_class_name('md7x2').click()
        online_img = driver.find_element_by_id('email')
        online_img.send_keys('https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1173876271,802372409&fm=26&gp=0.jpg')
        time.sleep(self_timeout)
        confirm_btn = WebDriverWait(driver, timeout).until(
            lambda d: d.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[4]/button[1]'))
        confirm_btn.click()

        # 8.保存草稿
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/ul/li[8]/a').click()
        # 8.发布文章
        time.sleep(self_timeout)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a/i').click()
        time.sleep(self_timeout)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a/i').click()
        time.sleep(self_timeout)
        #复制链接
        # time.sleep(self_timeout)
        # driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/ul/li[3]/i').click()
        #查看文章
        # driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/a[2]').click()
        # time.sleep(self_timeout)