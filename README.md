# 游泳日报

参见[http://swim.reverland.org](http://swim.reverland.org)

爬虫与更新脚本

主脚本：

`update.sh`负责每日更新

    sh ./update.sh 84268 7 3

`rebuild.sh`重建所有页面

    sh rebuild.sh

辅助脚本：

`topswim.py`是爬虫，参数分别为帖子号tid，爬取层数，生成结果(3表示生成pdf和html)

    python topswim python topswim.py 73347 11 3

`update_index.py`更新主页

    python update_index.py

`update_toc`更新总目录

    python update_toc.py

