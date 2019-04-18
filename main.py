import re
import linecache

from MetaWeblog import Cnblog
from MetaWeblog import Oschina


class Main(object):
    # init
    def __init__(self, file):
        self.title = ''
        self.content = ''
        self.category = ''
        self.tags = ''
        # OsChina的系统分类, 设个默认值
        self.osChina_sys_category = '编程语言'
        # CSDN的文章分类, 设个默认值
        self.csdn_article_category = '原创'
        # CSDN的博客分类, 设个默认值
        self.csdn_blog_category = '后端'
        self.read_file(file)

    # 读取MD中的title, content, self_category, self_tags, osChina_sys_category, csdn_article_category, csdn_blog_category
    def read_file(self, markdown_file):
        self.title = linecache.getline(markdown_file, 2).split('title: ')[1].strip('\n')
        with open(markdown_file, 'r', encoding='UTF-8') as f:
            self.content = f.read().split('-->\n')[1]
            # 重置文件指针偏移量
            f.seek(0)
            for line in f.readlines():
                if re.search('self_category: ', line) is not None:
                    self.category = line.split('self_category: ')[1].strip('\n')
                elif re.search('self_tags: ', line) is not None:
                    self.tags = line.split('self_tags: ')[1].strip('\n')
                elif re.search('osChina_sys_category: ', line) is not None:
                    self.osChina_sys_category = line.split('osChina_sys_category: ')[1].strip('\n')
                elif re.search('csdn_article_category: ', line) is not None:
                    self.csdn_article_category = line.split('csdn_article_category: ')[1].strip('\n')
                elif re.search('csdn_blog_category: ', line) is not None:
                    self.csdn_blog_category = line.split('csdn_blog_category: ')[1].strip('\n')


if __name__ == '__main__':
    md_file = 'auto.md'
    print("Markdown File is ", md_file)

    timeout = 10
    main = Main(md_file)

    # 开源中国
    # osChina = oschina.OsChina()
    # osChina.post(main, timeout)
 # 简书
 #    jian_shu = jianshu.JianShu()
 #    jian_shu.post(main, timeout)


    # 博客园
    #mw = Cnblog.CsdnMetaWeblog('YoSaukit', 'mqiuqiu1988!')
    # 新增文章（30秒内只能发一篇博文）
    #postid = mw.newPost('metawebolg test1342334453', 'This is a content')

    # 修改文章
    #mw.editPost(postid, 'metawebolg test', 'This is the first content')
    # 获得最近的文章
    #print(mw.getRecentPosts('', 5))
    # 删除文章
    #mw.deletePost(postid)

    #51otc
    mw = Oschina.Oschina('15600282811', 'mqiuqiu1988')
    postid = mw.newPost('原创', 'category', 'metawebolg test1342334453', 'This is a content')


