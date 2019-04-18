import ssl
import requests
import webbrowser
import MetaWeblog.oschinaApi3

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    APP_KEY = 'f2VBFmOXhx49E2iGK4hY'
    APP_SECRET = 'qAiDME8QboQq0jrPdc1hhHM8DNGSyHcg'
    REDIRECT_URL = 'http://jsmind.sinaapp.com/'

    client = MetaWeblog.oschinaApi3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
    url = client.get_authorize_url()
    # print(url)
    webbrowser.open_new(url)
    result = client.request_access_token(
        input("please input code : "))  # Enter the CODE obtained in the authorized address
    print(result)
    client.set_access_token(result.access_token, result.expires_in)

    # client.post_pub()
    url_post_pic = "https://www.oschina.net/action/openapi/blog_pub"
    # 构建文本类POST参数
    playload = {
        "access_token": result.access_token,
        "title": "This is a title",
        "content": "This is my content!",
        "classification": 0,
    }
    # 构建二进制multipart/form-data编码的参数

    # POST请求，发表微博
    print(requests.post(url_post_pic, data=playload))


if __name__ == '__main__':
    main()
