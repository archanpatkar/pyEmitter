import uuid

default = None;

class EventEmitter:
    def __init__(self,context = False,globalContext = None):
        if(context):
            self.context = {};
            self.UUID = uuid.uuid4();
            global default;
            if default == None:
                default = self;
            if globalContext == None:
                self.globalContext = default;
            elif isinstance(globalContext,EventEmitter):
                self.globalContext = globalContext;
        self.emitter = {};

    def on(self,event,f):
        if(self.emitter.get(event) == None):
            self.emitter[event] = [];
            self.emitter[event].append(f);
        else:
            self.emitter[event].append(f);

    def emit(self,event,*args):
        consumers = self.emitter.get(event);
        if(consumers == None):
            pass
        else:
            if(hasattr(self,"context")):
                [consumer(self.globalContext.context,self.context,*args) for consumer in consumers]
            else:
                [consumer(self.globalContext.context,*args) for consumer in consumers]
