from unittest import TestCase
from cli_args_system.args import Args


class TestConstruction(TestCase):

    def test_all_true(self):
        args = Args(
            consider_first=True,
            args_case_sensitive=True,
            flags_case_sensitive=True,
            flag_identifier='-',
            convert_numbers=True,
            infinity_identifier=True,
            args=['A', 'B', 'c', '-A', '1', '2', '3', '--B', 'b1', 'B2', 'b3']
        )
        dict_expected = {
            'default': ['A', 'B', 'c'],
            'A': [1, 2, 3],
            'B': ['b1', 'B2', 'b3']
        }
        self.assertDictEqual(args._flags, dict_expected)
        list_expected = ['A', 'B', 'c', '-A', 1, 2, 3, '--B', 'b1', 'B2', 'b3']
        # testing args
        self.assertListEqual(args._args, list_expected)
        # testing keys
        self.assertListEqual(args.flags_names(), ['default', 'A', 'B'])

    def test_all_false(self):
        args = Args(
            consider_first=False,
            args_case_sensitive=False,
            flags_case_sensitive=False,
            flag_identifier='#',
            convert_numbers=False,
            infinity_identifier=False,
            args=['A', 'B', 'c', '#A', '1', '2', '3', '###B', 'b1', 'B2', 'b3']
        )
        dict_expected = {
            'default': ['b', 'c'],
            'a': ['1', '2', '3'],
            '##b': ['b1', 'b2', 'b3']
        }
        self.assertDictEqual(args._flags, dict_expected)
        list_expected = ['b', 'c', '#a', '1', '2', '3', '###b', 'b1', 'b2', 'b3']
        # testing args
        self.assertListEqual(args._args, list_expected)
        # testing keys
        self.assertListEqual(args.flags_names(), ['default', 'a', '##b'])

    def test_default(self):
        args = Args(args=['A', 'B', 'c', '-A', '1', '2.3', '3', '--B', 'b1', 'B2', 'b3'])
        dict_expected = {
            'default': ['B', 'c'],
            'a': [1, 2.3, 3],
            'b': ['b1', 'B2', 'b3']
        }
        self.assertDictEqual(args._flags, dict_expected)
        list_expected = ['B', 'c', '-A', 1, 2.3, 3, '--B', 'b1', 'B2', 'b3']
        self.assertListEqual(args._args, list_expected)
        self.assertListEqual(args.flags_names(), ['default', 'a', 'b'])

    def test_size(self):
        args = Args(args=['A', 'B'], consider_first=True)
        self.assertEqual(len(args), 2)
        args = Args(args=['A', 'B'], consider_first=False)
        self.assertEqual(len(args), 1)
