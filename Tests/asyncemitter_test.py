import unittest
from threading import Thread
from pyEmitter.asyncemitter import AsyncEmitter

class TestAsyncEmitter(unittest.TestCase):

    def setUp(self):
        self.emitter = AsyncEmitter(isDaemon=True);

    def test_is_async(self):
        self.assertIsInstance(self.emitter,Thread);

    def test_on(self):
        self.assertIsNone(self.emitter.on("Test On", lambda *x: print(x)));

    def test_emit(self):
        self.assertIsNone(self.emitter.emit("Test Emit","Successful"));

    def test_pubsub(self):
        self.emitter.on("Test Emit",lambda x: self.assertEqual(x, "Successful"));
        self.emitter.emit("Test Emit","Successful");
