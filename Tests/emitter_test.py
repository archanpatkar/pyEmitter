import unittest
from pyEmitter.emitter import EventEmitter

class TestEventEmitter(unittest.TestCase):

    def setUp(self):
        self.emitter = EventEmitter();

    def test_on_dne(self):
        self.assertIsNone(self.emitter.on("Test On DNE", lambda *x: print(x)));

    def test_on(self):
        self.assertIsNone(self.emitter.on("Test On", lambda *x: print(x)));

    def test_emit(self):
        self.assertIsNone(self.emitter.emit("Test On","Successful"));

    def test_emit_dne(self):
        self.assertIsNone(self.emitter.emit("Test Emit DNE","Successful"));

    def test_pubsub(self):
        self.emitter.on("Test Emit",lambda *x: self.assertEqual(*x, "Successful"));
        self.emitter.emit("Test Emit","Successful");

    @unittest.expectedFailure
    def test_varargs(self):
        self.emitter.on("Test Var Args",lambda x: self.assertEqual(x, "UnSuccessful"));
        self.emitter.emit("Test Var Args","UnSuccessful","Hello");
