from threading import Thread
from TSqueue import TSQueue

class AysncEmitter(Thread):
    def __init__(self):
        Thread.__init__(self);
        queue = TSQueue();
        self.emitter = {}

    def on(self,event,f):


    def emit(self,event,*args):
        consumers = self.emitter.get(event)
        if(consumers == None):
            pass
        else:
            [consumer(*args) for consumer in consumers]

    def EventLoop(self):
        if(self.emitter.get(event) == None):
            self.emitter[event] = []
            self.emitter[event].append(f)
        else:
            self.emitter[event].append(f)
