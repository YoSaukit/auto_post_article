from xmlrpc.client import ServerProxy, ProtocolError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class CsdnMetaWeblog(object):
    def __init__(self, username, password, verbose=False):
        self.un = username
        self.pw = password
        self.sp = ServerProxy(
            'https://rpc.cnblogs.com/metaweblog/YoSaukit', verbose=verbose)
        self.bid = self.sp.blogger.getUsersBlogs(
            '', self.un, self.pw)[0]['blogid']

    def newPost(self, title, content):
        return self.sp.metaWeblog.newPost(self.bid, self.un, self.pw, {
            'title': title,
            'description': content,
            'categories': [],
        }, True)

    def editPost(self, postid, title, content):
        try:
            return self.sp.metaWeblog.editPost(postid, self.un, self.pw, {
                'title': title,
                'description': content,
                'categories': [],
            }, True)
        except TypeError:
            # CSDN的返回值把boolean类型错写成True/False，按照标准应该是1/0
            return True
        except Exception:
            return False



    def deletePost(self, postid):
        try:
            return self.sp.blogger.deletePost('', postid, self.un, self.pw, 1)
        except ProtocolError:
            # 返回500，不知道什么鬼问题，不过删除成功
            return True
        except Exception:
            return False

    def getRecentPosts(self, blogid, count):
        return self.sp.metaWeblog.getRecentPosts(blogid, self.un, self.pw, count)