# BoundedEmitter ----------------------------------------
# from pyEmitter.boundedemitter import BoundedEmitter
#
# # Only the events passed while creation
# # can be emitted and have listeners
# e = BoundedEmitter("hello","bye");
#
# e.on("hello",lambda *x: print(x));
# e.on("bye",lambda *x: print(x));
#
# # The on method will not accept listeners to events other than
# # the events passed while creating the BoundedEmitter
# e.on("Goodbye",lambda *x: print(x));
#
# e.emit("hello","Bounded Hello!");
# e.emit("bye","Bounded Bye!");
#
# # The emit method will not emit events other than
# # the events passed while creating the BoundedEmitter
# e.emit("Goodbye","It will not Work!");


# BoundedAsyncEmitter ----------------------------------------
# from pyEmitter.boundedasync import BoundedAsyncEmitter
#
# # Only the events passed while creation
# # can be emitted and have listeners
# e = BoundedAsyncEmitter("hello","bye");
#
# e.on("hello",lambda *x: print(x));
# e.on("bye",lambda *x: print(x));
#
# # The on method will not accept listeners to events other than
# # the events passed while creating the BoundedEmitter
# e.on("Goodbye",lambda *x: print(x));
#
# print("Before Emit")
#
# e.emit("hello","Async Bounded Hello!"); # Async Call
# e.emit("bye","Async Bounded Bye!"); # Async Call
#
# print("After Emit");
#
# # The emit method will not emit events other than
# # the events passed while creating the BoundedEmitter
# e.emit("Goodbye","It will not Work!");

#Global Context and Local Context ----------------------------------------
import pyEmitter.initializer
from pyEmitter.emitter import EventEmitter
from pyEmitter.emitter import default


def ContextMutator(namespace,context,*x):
    context["My1"] = x;

def m(namespace,context,*x):
    context["My2"] = x;

def globalContext(uuid,context,*x):
    context["global"] = "This is Amazing!";

default.on("Change Context",globalContext);

default.emit("Change Context")

e = EventEmitter(context=True);

# e.change < globalContext

e.on("hello",lambda g,context,*x: print("Namespace :",g,"\nContext :",context,"\nArgs :",x)); # The handler should accept varargs to get data if sent by the emitter
e.on("hello",ContextMutator);
e.on("hello",m);
e.on("hello",lambda g,context,*x: print("Namespace :",g,"\nContext :",context,"\nArgs :",x));

e.emit("hello",10,20,30); # You can pass data along with emitting the event
