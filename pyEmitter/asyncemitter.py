from threading import Thread
from pyEmitter.Event import Event
from pyEmitter.TSQueue import TSQueue

class AsyncEmitter(Thread):
    def __init__(self,isDaemon=False):
        Thread.__init__(self);
        self.setDaemon(isDaemon);
        self.queue = TSQueue();
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
        self.queue.enqueue(Event(name = event,value = args));

    def EventLoop(self):
        while True:
            Event = self.queue.dequeue();
            consumers = self.emitter.get(Event.name)
            if(consumers == None):
                pass
            else:
                [consumer(*Event.value) for consumer in consumers]
