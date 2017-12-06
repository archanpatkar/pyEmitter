class BoundedEmitter:
    def __init__(self,*events):
        self.emitter = {};
        [self.addEvent(event) for event in events]

    def addEvent(self,event):
        self.emitter[event] = [];

    def on(self,event,f):
        if(event in self.emitter):
            self.emitter[event].append(f);

    def emit(self,event,*args):
        if(event in self.emitter):
            consumers = self.emitter.get(event);
            if(consumers == None):
                pass
            else:
                [consumer(*args) for consumer in consumers]
