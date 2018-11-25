from threading import Timer
from daytest.eventManager import EventManager,Event

#事件名称  新文章
EVENT_ARTICLE = "Event_Article"

#事件源 公众号
class PublicAccounts:
    def __init__(self,eventManager):
        self.__eventManager = eventManager

    def WriteNewArtical(self):
        #创建事件对象，写了新文章
        event = Event(type_=EVENT_ARTICLE)
        event.dict["article"] = '如何提高自我'
        #发送事件
        self.__eventManager.SendEvent(event)
        print('公众号发送新文章')

#监听器 订阅者
class Listener:
    def __init__(self,username):
        self.__username = username

    #监听器的处理函数 读文章
    def ReadArtical(self,event):
        print('%s 收到新文章' % self.__username)
        print('正在阅读新文章内容：%s'  % event.dict["article"])


def test():
    listener1 = Listener("Li")  # 订阅者1
    listener2 = Listener("lxh")  # 订阅者2

    eventManager = EventManager()

    # 绑定事件和监听器响应函数(新文章)
    eventManager.AddEventListener(EVENT_ARTICLE, listener1.ReadArtical)
    eventManager.AddEventListener(EVENT_ARTICLE, listener2.ReadArtical)
    eventManager.Start()

    publicAcc = PublicAccounts(eventManager)
    # publicAcc.WriteNewArtical()
    # 定时器
    timer = Timer(5, publicAcc.WriteNewArtical)
    timer.start()
    # eventManager.Stop()


if __name__ == '__main__':
    test()
