from unittest import TestCase
from cli_args.args import Args


class TestNumbers(TestCase):

    def test_true(self):
        args = Args(args=['a', 'b'], consider_first=True)
        # the args size must be 2
        self.assertTrue(args == 2)
        self.assertTrue(args >= 2)
        self.assertTrue(args <= 2)
        self.assertTrue(args < 3)
        self.assertTrue(args > 1)

    def test_False(self):
        args = Args(args=['a', 'b', 'c', 'd'])
        # the args size must be 3
        self.assertFalse(args < 3)
        self.assertFalse(args > 10)


class TestLists(TestCase):

    def test_lists(self):
        args = Args(args=['a', 'b', 'c', 'd'])
        self.assertTrue(args == ['b', 'c', 'd'])
        self.assertTrue(args != ['b', 'd', 'd'])
        self.assertFalse(args == ['b', 'd', 'd'])


class TestTuples(TestCase):

    def test_lists(self):
        args = Args(args=['a', 'b', 'c', 'd'])
        self.assertTrue(args == ('b', 'c', 'd'))
        self.assertTrue(args != ('b', 'd', 'd'))
        self.assertFalse(args == ('b', 'd', 'd'))


class TestDicts(TestCase):

    def test_lists(self):
        args = Args(args=['a', 'b', 'c', 'd', '--a', 'a1', 'a2'])
        expected = {'default': ['b', 'c', 'd'], 'a': ['a1', 'a2']}

        self.assertTrue(args == expected)
        # modifying dict with a ky
        expected['d'] = None
        self.assertTrue(args != expected)
        self.assertFalse(args == expected)


class In(TestCase):

    def test_in(self):
        args = Args(args=['a', 'b', 'c', 'd', '--x', 'a1', 'a2'])

        self.assertTrue('b' in args)

        # test false
        self.assertFalse('$' in args)

    def test_not_in(self):
        args = Args(args=['a', 'b', 'c', 'd', '--x', 'a1', 'a2'])

        self.assertTrue('#' not in args)
        # test false
        self.assertFalse('d' not in args)
