import unittest

from .rover import Rover, DirectedPosition


class Test_Position(unittest.TestCase):

    def test_printPosition(self):
        """
        Stampa della posizione
        """
        x = Rover(1, 2, 'N')
        self.assertEqual(str(x), "1 2 N")


class Test_Forward(unittest.TestCase):

    def test_f1_N(self):
        x = Rover(1, 2, 'N')
        s = x.command('F')
        self.assertEqual(s, "1 3 N")
        # self.assertEqual(s, DirectedPosition(1, 3, 'N'))

    def test_2f1_N(self):
        x = Rover(1, 2, 'N')
        s = x.command('FF')
        self.assertEqual(s, "1 4 N")

    def test_f1_W(self):
        x = Rover(1, 2, 'W')
        s = x.command('F')
        self.assertEqual(s, "0 2 W")

    def test_f1_E(self):
        x = Rover(1, 2, 'E')
        s = x.command('F')
        self.assertEqual(s, "2 2 E")

    def test_f1_S(self):
        x = Rover(1, 2, 'S')
        s = x.command('F')
        self.assertEqual(s, "1 1 S")

    #
    # def test_f1_S(self):
    #     x = Rover(1, 2, 'S')
    #     s = x.command('F')
    #     self.assertEqual(s, "1 1 S")
