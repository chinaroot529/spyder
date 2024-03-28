这个库里面一共爬取了三个网页，分别为：裁判文书网，最高人民法院，法律服务网


（1）最高人民法院
最高人民法院网站的代码很简单，而且也没有robots协议，拿到python代码直接运行finaltest.py即可
最后运行的结果为
<img width="920" alt="image" src="https://github.com/chinaroot529/spyder/assets/124231718/3f520131-ac37-4300-abcd-49793ea334a5">



（2）法律服务网
这个网站属于中级网站，有一定的robots协议，爬的时候自己学习就可以了，别拿来干坏事（免责声明）
关于这个网站的话，采用了selenium的自动化爬虫脚本，所以我们需要一步一步的验证，在文件夹里面一共有三个文件
<img width="328" alt="image" src="https://github.com/chinaroot529/spyder/assets/124231718/821cb446-9421-4911-a2cf-a8f04f3eadcf">
我们先运行 testinit.py，如果有输出结果，就证明这个网页还能正常的访问
运行结果示例如下：
<img width="416" alt="image" src="https://github.com/chinaroot529/spyder/assets/124231718/f6879972-f122-4973-a4b5-f172cf8423ad">

如果第一步成功运行，我们接着运行第二个文件 testnextpage.py
这是一个采用了selenium自动工具的代码，首先实例化了一个浏览器窗口,其实也很简单
<img width="800" alt="image" src="https://github.com/chinaroot529/spyder/assets/124231718/adc33a3c-8306-4ff0-850b-d04eff6ab908">
把浏览器的位置修改成自己电脑的，save_folder 文件的路径是为了存储爬取内容的，你要先创建一个存放数据的文件夹，然后替换上去
如果运行成功之后会得到一个实例化的Google浏览器窗口，这个时候回到编译器的控制台
<img width="416" alt="image" src="https://github.com/chinaroot529/spyder/assets/124231718/81cc010d-7c9c-409c-a12f-c8b773078d66">

如果控制台有如上输出，并且实例化的窗口可以自动翻页，那就代表运行成功

最后去运行Arbitration.py，前面两部没有问题，这个基本上也没有什么问题的


（3）裁判文书网
这个网站的禁制特别多，具体的运行方法不做解释，如果有需要可以联系本人微信 vx：ll_xx1216
