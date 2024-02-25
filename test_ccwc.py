import unittest

import ccwc


class TestCcwc(unittest.TestCase):

    def test_input_measurements(self):
        self.assertEqual(
            ccwc._measure_content(ccwc._read_file('test.txt')),
            (7145, 58164, 342190, 339292), 'Incorrect measurements.')


if __name__ == '__main__':
    unittest.main()
