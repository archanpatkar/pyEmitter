import unittest
from pyEmitter.emitter import EventEmitter

class TestEventEmitter(unittest.TestCase):

    def setUp(self):
        self.emitter = EventEmitter();

    def test_AddingHandlerToEvent(self):
        self.assertIsNone(self.emitter.on("Test On", lambda *x: print(x)));

    def test_EmittingEvent(self):
        self.assertIsNone(self.emitter.emit("Test On","Successful"));

    def test_EmittingEventWhichDoesNotExist(self):
        self.assertIsNone(self.emitter.emit("Test Emit DNE","Successful"));

    def test_TestingCompleteEcosystem(self):
        self.emitter.on("Test Emit",lambda *x: self.assertEqual(x[1], "Successful"));
        self.emitter.emit("Test Emit","Successful");

    @unittest.expectedFailure
    def test_VarargsCompulsory(self):
        self.emitter.on("Test Var Args",lambda x: self.assertEqual(x, "UnSuccessful"));
        self.emitter.emit("Test Var Args","UnSuccessful","Hello");