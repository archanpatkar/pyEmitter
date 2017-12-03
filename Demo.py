from pyEmitter.asyncemitter import AysncEmitter


print("Creating a Aysnc Emitter");

emitter = AysncEmitter();

emitter.on("one",lambda *x: print(x));

emitter.emit("one","Hello");


while True:
    pass
