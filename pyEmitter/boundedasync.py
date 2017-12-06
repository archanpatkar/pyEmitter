from threading import Thread
from pyEmitter.Event import Event
from pyEmitter.TSQueue import TSQueue

class BoundedAsyncEmitter(Thread):
    def __init__(self,*events,isDaemon=False):
        Thread.__init__(self);
        self.setDaemon(isDaemon);
        self.queue = TSQueue();
        self.emitter = {};
        [self.addEvent(event) for event in events]
        self.start();

    def addEvent(self,event):
        self.emitter[event] = [];

    def run(self):
        self.EventLoop();

    def on(self,event,f):
        if(event in self.emitter):
            self.emitter[event].append(f);

    def emit(self,event,*args):
        if(event in self.emitter):
            self.queue.enqueue(Event(name = event,value = args));

    def EventLoop(self):
        while True:
            Event = self.queue.dequeue();
            consumers = self.emitter.get(Event.name)
            if(consumers == None):
                pass
            else:
                [consumer(*Event.value) for consumer in consumers]
