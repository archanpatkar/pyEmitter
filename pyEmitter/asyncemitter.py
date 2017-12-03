from threading import Thread
from queue import TSQueue

class AysncEmitter(Thread):
    def __init__(self):
        Thread.__init__(self);
        self.setDaemon(True);
        queue = TSQueue();
        self.emitter = {};
        self.start();

    def run(self):
        self.EventLoop();

    def on(self,event,f):
        if(self.emitter.get(event) == None):
            self.emitter[event] = []
            self.emitter[event].append(f)
        else:
            self.emitter[event].append(f)

    def emit(self,event,*args):
        self.queue.enqueue((event,args));

    def EventLoop(self):
        while True:
            Event = self.queue.dequeue();
            consumers = self.emitter.get(Event(0))
            if(consumers == None):
                pass
            else:
                [consumer(Event(1)) for consumer in consumers]
