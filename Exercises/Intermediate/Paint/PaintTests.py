import unittest
import PaintWizard


class PaintTests(unittest.TestCase):
    def test_waste(self):
        self.assertEqual(PaintWizard.waste(20, 10, 15), 8.666666666666666)

    def test_coverage(self):
        self.assertEqual(PaintWizard.covered(20, 10, 15), 7.5)


if __name__ == '__main__':
    unittest.main()
