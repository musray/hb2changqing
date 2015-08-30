# -*- coding: utf-8 -*-
import web

urls = (
        '/', 'index'
)

#render = web.template.render('template/')

content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Happy Birthday, My Sweet Heart!</title>
    <style>
        body {
            background: #ff7682;
            font-family: "Courier New", monospace;
            margin: 0;
            color: #57595B;
        } 
        h1 {
            margin:0 auto; 
            text-shadow: 0px 1px 1px #ffffff;
            padding: 1.5em;
            text-align: center;
        }
        .content {
            /* width: 600px; */
            margin: 0 auto;
            padding: 0 1em .5em;
            max-width: 640px;
            line-height: 1.5em;
        }
        img {
            display: block;
            margin: 0 auto;
        }
        #footer {
            margin: 1em auto;
            font-size: 1.5em;
            padding: 0 0 2em;
            text-align: center;
        }
        h3 {
            font-size: 1.6em;
            text-shadow: 0px 1px 1px #ffffff;
            display: inline;
        }
        .emoji{
            display: inline;
        }
    </style>
</head>
<body> 
    <div>
      <h1>Happy Birthday, My Little Sweet Heart!</h1>
    </div>
   <div class="content">我的小常青，再次感谢你的到来！2015年6月17号，是爸爸妈妈第一次为你过生日。没想到你会长得如此飞快，只用了365天的时间，就从一个闭着眼睛的小肉团儿，变成了一个蹒跚学步、爱笑爱闹的小姑娘。</div>
   <div class="content">不知道你会在生日当天许下什么愿望，是满满一屋子的玩具，还是一次全家出动的奇幻旅行呢？</div>
   <div class="content">无论怎么样，爸爸妈妈的愿望只有一个，就是陪伴你健康快乐的长大！</div>
   <img src="./static/foot_resize.jpg" alt="foot.resize"  />
   <div id="footer">
     <img class="emoji" src="./static/family1.png" alt="family" width="36" height="36">
     <img class="emoji" src="./static/horse2.png" alt="horse" width="36" height="36">
     <img class="emoji" src="./static/present1.png" alt="present1" width="36" height="36">
     <img class="emoji" src="./static/present2.png" alt="present2" width="36" height="36">
     <h3>Sweet child o' mine</h3>
     <img class="emoji" src="./static/note.png" alt="note" width="36" height="36">
     <img class="emoji" src="./static/note2.png" alt="note2" width="36" height="36">
     <img class="emoji" src="./static/note3.png" alt="note3" width="36" height="36">
     <img class="emoji" src="./static/note5.png" alt="note5" width="36" height="36">
   </div>
</body>
</html>
"""

class index:
    def GET(self):
        return content

application = web.application(urls, globals()).wsgifunc()

# for ACE.
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8080, application)
    httpd.server_forever()

# for local use.
#if __name__ == '__main__':
#    app = web.application(urls, globals())
#    app.run()
