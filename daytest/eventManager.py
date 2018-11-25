from queue import Queue,Empty
from threading import Thread

class EventManager():
    def __init__(self):
        # 事件对象
        self.__eventQueue = Queue()
        # 事件管理开关
        self.__active = False
        #事件处理线程
        self.__thread = Thread(target=self.__Run)

        # 这里的__handlers是一个字典，用来保存对应的事件的响应函数
        # 其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers={}

    def __Run(self):
        '''
        运行
        :return:
        '''
        while self.__active == True:
            try:
                # 获取事件的阻塞时间设为1秒
                event = self.__eventQueue.get(block=True,timeout=1)
                # 取到事件之后,调用相应的事件处理程序
                self.__EventProcess(event)
            except Empty:
                print("没有获取到事件...")

    def __EventProcess(self,event):
        '''
        处理事件
        :param event: Event Ojbect
        :return:
        '''
        # 检查是否存在对该事件处理的函数
        if event.type_ in self.__handlers:
            # 存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type_]:
                handler(event)

    def Start(self):
        '''
        启动
        :return:
        '''
        # 事件管理器启动
        self.__active = True
        # 启动事件处理线程
        self.__thread.start()

    def Stop(self):
        '''
        停止
        :return:
        '''
        # 事件管理器停止
        self.__active = False
        # 等待事件处理线程退出
        self.__thread.join()

    def AddEventListener(self,type_,handler):
        '''
        绑定事件和监听器处理函数
        :param type_: str
        :param handler: funciton
        :return:
        '''
        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []

        #保存当前事件及其响应函数到事件管理器的字典中
        self.__handlers[type_] = handlerList
        # 若要注册的处理器不在该事件的处理器列表中，则注册该事件
        if handler not in handlerList:
            handlerList.append(handler)

    def RemoveEventListener(self,type_,handler):
        pass

    def SendEvent(self,event):
        '''
        发送事件，向事件队列中存入事件
        :param event:
        :return:
        '''
        # 进队
        self.__eventQueue.put(event)


class Event():
    '''
    事件对象
    '''
    def __init__(self,type_=None):
        # 事件类型
        self.type_ = type_
        # 字典用于保存具体的事件数据
        self.dict = {}

