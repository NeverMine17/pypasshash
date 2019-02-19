import unittest
import pypasshash

tests_version_1 = [
    ['test123', 'asd', 'w9XHj6TXSSC4'],
    ['qwerty', 'qwerty', 't8BvIfZIqw8i'],
    ['123', '123', 'd7JCE8mdIksv'],
    ['12345', '12345', 'f8Ew2fPdXNDB'],
    ['5agRrdKKPFWkT3pj5dwNddyA', 'jbuHzWA4ch7h73KugVHtqv6r', 'q1RjFnRTw2gq'],
    ['3VaY2WPxpfZU6z25MWhdexsK', 'VkaZ4EaCeepBxBynTrj6WSXm', 'h3CUKhIANOS3'],
    ['NT2Sv5q7Ne4JVVyB4J8X3epX', 'bzBsz5LMtYdjK8Sv7Ntw72KS', 'b5FbaC4bCT5a'],
    ['eXsAeVTEBf9ZdqCnyfSfZYSy', '3afGM8nZpafjQxyFYS4bZjaG', 'w7JNYoywZIlS']
]

tests_version_2 = [
    ['test123', 'asd', 'u8NFNm8i4y0I'],
    ['qwerty', 'qwerty', 'n7XKKsaXAYnk'],
    ['123', '123', 'j8CC1DMjHpuJ'],
    ['12345', '12345', 'v6ZawS4UvMTr'],
    ['5agRrdKKPFWkT3pj5dwNddyA', 'jbuHzWA4ch7h73KugVHtqv6r', 'l9Q920XQlkk9'],
    ['3VaY2WPxpfZU6z25MWhdexsK', 'VkaZ4EaCeepBxBynTrj6WSXm', 'j9HCjIiJYUoE'],
    ['NT2Sv5q7Ne4JVVyB4J8X3epX', 'bzBsz5LMtYdjK8Sv7Ntw72KS', 'n0PATXNeKgnG'],
    ['eXsAeVTEBf9ZdqCnyfSfZYSy', '3afGM8nZpafjQxyFYS4bZjaG', 'v5Nd1kEo4yvR']
]


class PassHashTest(unittest.TestCase):
    def test_version_2(self):
        for test in tests_version_2:
            self.assertEqual(pypasshash.get_pass(test[0], test[1], 2), test[2])

    def test_version_1(self):
        for test in tests_version_1:
            self.assertEqual(pypasshash.get_pass(test[0], test[1], 1), test[2])


if __name__ == '__main__':
    unittest.main()
