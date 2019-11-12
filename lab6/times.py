import unittest


class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __lt__(self, other):
        return self.s < other.s

    def __ne__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.s > other.s

    def __le__(self, other):
        return self.s <= other.s

    def __ge__(self, other):
        return self.s >= other.s

    def __int__(self):  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual("Time(6)", repr(Time(6)))
        self.assertEqual("Time(11)", repr(Time(11)))
        self.assertEqual("Time(2)", repr(Time(2)))
        self.assertEqual("Time(12)", repr(Time(12)))
        self.assertEqual("00:02:13", str(Time(133)))
        self.assertEqual("00:03:10", str(Time(190)))
        self.assertEqual("02:28:10", str(Time(8890)))
        self.assertEqual("00:00:04", str(Time(4)))

    def test_add(self):
        self.assertEqual(Time(3), Time(1) + Time(2))
        self.assertEqual(Time(4), Time(3) + Time(1))
        self.assertEqual(Time(6), Time(4) + Time(2))
        self.assertEqual(Time(7), Time(6) + Time(1))
        self.assertEqual(Time(1), Time(1) + Time(0))
        self.assertEqual(Time(1), Time(1) + Time(0))
        self.assertEqual(Time(-7), Time(-9) + Time(2))
        self.assertEqual(Time(44), Time(11) + Time(33))
        self.assertEqual(Time(24), Time(12) + Time(12))
        self.assertEqual(Time(120), Time(20) + Time(100))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(Time(1) <= Time(1))
        self.assertTrue(Time(9) >= Time(2))
        self.assertTrue(Time(8) > Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(1) < Time(9))
        self.assertTrue(Time(4) > Time(2))
        self.assertTrue(Time(1) >= Time(1))
        self.assertTrue(Time(9) != Time(2))
        self.assertTrue(Time(9) > Time(2))

    def test_int(self):
        self.assertEqual(int(Time(7)), 7)
        self.assertEqual(int(Time(8)), 8)
        self.assertEqual(int(Time(0)), 0)
        self.assertEqual(int(Time(2222)), 2222)
        self.assertEqual(int(Time(33)), 33)
        self.assertEqual(int(Time(12)), 12)
        self.assertEqual(int(Time(-99)), -99)
        self.assertEqual(int(Time(100)), 100)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
