import unittest
from Tests.emitter_test import TestEventEmitter
from Tests.asyncemitter_test import TestAsyncEmitter

def getTestCases():
    EventEmitter = unittest.TestLoader().loadTestsFromTestCase(TestEventEmitter);
    AsyncEmitter = unittest.TestLoader().loadTestsFromTestCase(TestAsyncEmitter);
    return [EventEmitter,AsyncEmitter];

def task_test():
    """test"""

    def test(targets):
        for cases in getTestCases():
            unittest.TextTestRunner(verbosity=2).run(cases);

    return {
        'actions': [test],
        'verbosity': 2
        }
