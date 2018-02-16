import unittest


def get_suite():
    "Return a unittest.TestSuite."
    import tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests)
    return suite
