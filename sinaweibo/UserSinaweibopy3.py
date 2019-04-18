import urllib
import webbrowser
import requests


import sinaweibo.sinaweibopy3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
def main():
    '''
    if you want to use this api,you should follow steps follows to operate.
    '''
    try:
        # step 1 : sign a app in weibo and then define const app key,app srcret,redirect_url
        APP_KEY = '4012287685'
        APP_SECRET = '6ef8902dc29f227b99bea31f79201875'
        REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'
        # step 2 : get authorize url and code
        client = sinaweibo.sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
        url = client.get_authorize_url()
        # print(url)
        webbrowser.open_new(url)
        # step 3 : get Access Token
        # Copy the above address to the browser to run, 
        #enter the account and password to authorize, the new URL contains code
        result = client.request_access_token(
            input("please input code : "))  # Enter the CODE obtained in the authorized address
        print(result)
        # At this point, the access_token and expires_in should be saved,
        # because there is a validity period.A
        # If you need to send the microblog multiple times in a short time,
        # you can use it repeatedly without having to acquire it every time.
        client.set_access_token(result.access_token, result.expires_in)

        # step 4 : using api by access_token
        #print(client.public_timeline())  # get the latest public Weibo
        # =============================================================================
        #         statuses = client.public_timeline()['statuses']
        #         length = len(statuses)
        #         for i in range(0,length):
        #             print("昵称："+statuses[i]['user']['screen_name'])
        #             print("简介："+statuses[i]['user']['description'])
        #             print("位置："+statuses[i]['user']['location'])
        # =============================================================================
        '''
        in this step,the api name have to turn '/' in to '__'
        for example,statuses/public_timeline(this is a standard api name) have to turn into statuses__public_timeline
        '''
        # Or use this method
        #print(client.get.statuses__public_timeline())
        print(client.get.statuses__user_timeline())
        # Obtain the UID of the authorized user
        #print(client.get.account__get_uid())

        # 发表图文微博的接口
        url_post_pic = "https://api.weibo.com/2/statuses/share.json"
        # 构建文本类POST参数
        playload = {
            "access_token": result.access_token,
            "status": "这是一条测试微博 http://www.mob.com/downloads/"
        }
        # 构建二进制multipart/form-data编码的参数
        files = {
            "pic": open("/Users/didi/Documents/PycharmProjects/article/test.jpg", "rb")
        }
        # POST请求，发表微博
        requests.post(url_post_pic, data=playload, files=files)
        # client.statuses_share()

    except ValueError:
        print('pyOauth2Error')

if __name__ == '__main__':
    main()
