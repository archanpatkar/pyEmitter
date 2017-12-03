import unittest
from Tests.emitter_test import TestEventEmitter
from Tests.asyncemitter_test import TestAsyncEmitter

print("Test Runner Started");

def getTestCases():
    EventEmitter = unittest.TestLoader().loadTestsFromTestCase(TestEventEmitter);
    AsyncEmitter = unittest.TestLoader().loadTestsFromTestCase(TestAsyncEmitter);
    return [EventEmitter,AsyncEmitter];

#Running Tests
print("Running Tests")
for cases in getTestCases():
    unittest.TextTestRunner(verbosity=2).run(cases);
