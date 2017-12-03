import unittest
from threading import Thread
from pyEmitter.asyncemitter import AsyncEmitter

class TestAsyncEmitter(unittest.TestCase):

    def test_is_async(self):
        self.assertIsInstance(AsyncEmitter(),Thread);

    def test_on(self):
        emitter = AsyncEmitter();
        self.assertIsNone(emitter.on("Test On", lambda *x: print(x)));

    def test_emit(self):
        emitter = AsyncEmitter();
        self.assertIsNone(emitter.emit("Test Emit","Successful"));

    def test_pubsub(self):
        emitter = AsyncEmitter();
        emitter.on("Test Emit",lambda *x: self.assertEqual(*x, "Successful"));
        emitter.emit("Test Emit","Successful");

    def test_varargs(self):
        emitter = AsyncEmitter();
        expectedTuple = ("Successful","Hello",)
        emitter.on("Test Emit",lambda x: self.assertTupleEqual(x , expectedTuple));
        emitter.emit("Test Emit","Successful","Hello");
