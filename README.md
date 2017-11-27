# pyEmitter
### An Event Emitter implementation in Python inspired by Node.js

***

### A Simple Example

```
from emitter import EventEmitter

e = EventEmitter();

e.on("hello",lambda *x: print(x)); # Emitter uses varargs

e.emit("hello",10,20,30);

```
