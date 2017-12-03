import unittest
from pyEmitter.emitter import EventEmitter

class TestEventEmitter(unittest.TestCase):

    def test_on(self):
        emitter = EventEmitter();
        self.assertIsNone(emitter.on("Test On", lambda *x: print(x)));

    def test_emit(self):
        emitter = EventEmitter();
        self.assertIsNone(emitter.emit("Test Emit","Successful"));

    def test_pubsub(self):
        emitter = EventEmitter();
        emitter.on("Test Emit",lambda *x: self.assertEqual(*x, "Successful"));
        emitter.emit("Test Emit","Successful");

    @unittest.expectedFailure
    def test_varargs(self):
        emitter = EventEmitter();
        emitter.on("Test Emit",lambda x: self.assertEqual(x, "UnSuccessful"));
        emitter.emit("Test Emit","UnSuccessful","Hello");
