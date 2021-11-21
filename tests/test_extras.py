from unittest import TestCase
from cli_args.extras import cast_list, format_args, format_flag, is_a_flag, get_flags, get_num_comparison


class FormatFlag(TestCase):

    def test_infinity_identifier(self):
        formatted_flag = format_flag(flag='--a',
                                     case_sensitive=False,
                                     flag_identifier='-',
                                     infinity_identifier=True
                                     )
        self.assertEqual(formatted_flag, 'a')

    def test_not_infinity_identifier(self):
        formatted_flag = format_flag(flag='---a',
                                     case_sensitive=False,
                                     flag_identifier='-',
                                     infinity_identifier=False
                                     )
        self.assertEqual(formatted_flag, '--a')

    def test_case_sensitive(self):
        formatted_flag = format_flag(flag='--A',
                                     case_sensitive=True,
                                     flag_identifier='-',
                                     infinity_identifier=True
                                     )
        self.assertEqual(formatted_flag, 'A')


class IsaFlag(TestCase):

    def test_is_a_flag(self):
        flag = is_a_flag('--a', case_sensitive=False, flag_identifier='-')
        self.assertTrue(flag)

    def test_single_char(self):
        flag = is_a_flag('-', case_sensitive=False, flag_identifier='-')
        self.assertFalse(flag)

    def test_case_sensitive_false(self):
        flag = is_a_flag('BA', case_sensitive=True, flag_identifier='b')
        self.assertFalse(flag)

    def test_case_sensitive(self):
        flag = is_a_flag('BA', case_sensitive=True, flag_identifier='B')
        self.assertTrue(flag)

    def test_is_not_a_flag(self):
        flag = is_a_flag('--a', case_sensitive=False, flag_identifier='#')
        self.assertFalse(flag)


class GetFlags(TestCase):

    def test_with_flags(self):
        args = ['a', 'b', 'c', '-a', 'a1', 'a2', 'a3', '--b', 'b1', 'b2', 'b3']
        flags = get_flags(args=args, case_sensitive=False, flag_identifier='-', infinity_identifier=True)
        expected = {
            'default': ['a', 'b', 'c'],
            'a': ['a1', 'a2', 'a3'],
            'b': ['b1', 'b2', 'b3']
        }
        self.assertDictEqual(flags, expected)

    def test_without_flags(self):
        args = ['a', 'b', 'c', 'a1', 'a2', 'a3', 'b1', 'b2', 'b3']
        flags = get_flags(args=args, case_sensitive=False, flag_identifier='-', infinity_identifier=True)
        expected = {
            'default': ['a', 'b', 'c', 'a1', 'a2', 'a3', 'b1', 'b2', 'b3']
        }
        self.assertDictEqual(flags, expected)

    def test_with_different_identifier(self):
        args = ['a', 'b', 'c', '#a', 'a1', 'a2', 'a3', '##b', 'b1', 'b2', 'b3']
        flags = get_flags(args=args, case_sensitive=False, flag_identifier='#', infinity_identifier=True)
        expected = {
            'default': ['a', 'b', 'c'],
            'a': ['a1', 'a2', 'a3'],
            'b': ['b1', 'b2', 'b3']
        }
        self.assertDictEqual(flags, expected)

    def test_with_flags_case_sensitive(self):
        args = ['a', 'b', 'c', '-A', 'a1', 'a2', 'a3', '--B', 'b1', 'b2', 'b3']
        flags = get_flags(args=args, case_sensitive=True, flag_identifier='-', infinity_identifier=True)
        expected = {
            'default': ['a', 'b', 'c'],
            'A': ['a1', 'a2', 'a3'],
            'B': ['b1', 'b2', 'b3']
        }
        self.assertDictEqual(flags, expected)


class FormatArgs(TestCase):

    def test_al_true(self):
        entry = ['A', 'B', 'C', 'D', '1', '2', '3', '4']
        args = format_args(
            args=entry,
            consider_first=True,
            case_sensitive=True,
            convert_numbers=True
        )
        expected = ['A', 'B', 'C', 'D', 1, 2, 3, 4]
        self.assertListEqual(args, expected)

    def test_al_false(self):
        entry = ['A', 'B', 'C', 'D', '1', '2', '3', '4']
        args = format_args(
            args=entry,
            consider_first=False,
            case_sensitive=False,
            convert_numbers=False
        )
        expected = ['b', 'c', 'd', '1', '2', '3', '4']
        self.assertListEqual(args, expected)


class CastList(TestCase):

    def test_empty(self):
        self.assertListEqual(cast_list(), [])
        self.assertListEqual(cast_list(None), [])
        self.assertListEqual(cast_list([]), [])

    def test_tuple(self):
        value = cast_list('1', 2, 3)
        self.assertListEqual(value, ['1', 2, 3])

    def test_list(self):
        value = cast_list(['1', 2, 3])
        self.assertListEqual(value, ['1', 2, 3])

    def test_string(self):
        value = cast_list('a')
        self.assertListEqual(value, ['a'])


class NumComparison(TestCase):

    def test_int(self):
        self.assertEqual(4, get_num_comparison(4))

    def test_list(self):
        self.assertEqual(3, get_num_comparison([1, 2, 3]))

    def test_tuple(self):
        self.assertEqual(3, get_num_comparison((1, 2, 3)))

    def test_none(self):
        self.assertIsNone(get_num_comparison({}))
