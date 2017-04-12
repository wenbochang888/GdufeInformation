# 广东财经大学全部学生的信息

##2017年4月7日15:13:40

环境：python2.7

小弟第一次写的完整爬虫，放到github，顺便当练练github的手

1：首先坚持可见即可爬（小弟还没有到这种境界）

2: 素拓系统可以看见所有人的学号，姓名，学院，院系，班级信息

3：直接爬就行

4：'grade':'2016' while里面的grade表示年纪. 2016级大概3000页，2015级好像7000多（哭死）



##2017年4月12日13:13:39

昨天无聊的时候再看素拓系统，发觉抓取了很多重复的元素，所以导致了抓取速度十分的慢

然后发觉每个人最少最少都申请了15个素拓左右。所以进行了算法的优化

用一个cnt记录抓到了第几个记录，每到15就取余，然后进行抓取，非15的倍数不进行抓取

然后昨晚试了一下子。大概由原来的20s一页，提高到了3s一页。相当于效率提高了7倍左右。

抓取速率很提高很多。这让我意识到了算法的重要性，所以大家搞好算法啊。

##ps.

1：爬虫效率有点慢，用了几个模块，可用python自带的pip安装

2：直接运行gdufeInformation.py文件就可以了

3：亲测爬一页大概20s（真tm慢）

![Image text](https://github.com/wenbochang888/gdufeInformation/blob/master/0.png)

![Image text](https://github.com/wenbochang888/gdufeInformation/blob/master/1.png)

![Image text](https://github.com/wenbochang888/gdufeInformation/blob/master/2.png)

![Image text](https://github.com/wenbochang888/GdufeInformation/blob/master/3.png)

![Image text](https://github.com/wenbochang888/GdufeInformation/blob/master/4.png)

![Image text](https://github.com/wenbochang888/GdufeInformation/blob/master/5.png)