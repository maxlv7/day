from threading import Condition,Thread

class XA(Thread):
    def __init__(self):
        super.__init__(name="小爱")

    def run(self):
        pass


class TM(Thread):
    def __init__(self):
        super.__init__(name="天猫")

    def run(self):
        pass