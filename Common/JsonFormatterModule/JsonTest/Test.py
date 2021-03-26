import unittest

from Common.JsonFormatterModule.JsonFormatter import JsonFormatter
from Common.JsonFormatterModule.JsonTest.Entities.Character import Character
from Common.JsonFormatterModule.JsonTest.Entities.DerivedClass import DerivedClass
from Common.JsonFormatterModule.JsonTest.Entities.MyCollection import MyCollection


class TestSerialize(unittest.TestCase):
    def test_simple_entity(self):
        ch = Character(18, 100)
        json_ch = JsonFormatter.serialize(ch)
        ch_val = JsonFormatter.deserialize(json_ch, Character)
        self.assertTrue(ch is not ch_val)
        self.assertTrue(ch == ch_val)

    def test_compound_entity(self):
        d1 = DerivedClass.build()

        json_d1 = JsonFormatter.serialize(d1)
        self.assertTrue(json_d1)

        d2 = JsonFormatter.deserialize(json_d1, DerivedClass)
        self.assertTrue(d2 is not None)
        self.assertFalse(d2 is d1)
        self.assertTrue(d2 == d1)
        self.assertIsInstance(d2, DerivedClass)

        json_d2 = JsonFormatter.serialize(d2)
        self.assertTrue(json_d2)

        d3 = JsonFormatter.deserialize(json_d2, DerivedClass)
        self.assertTrue(d3 is not None)
        self.assertFalse(d3 is d1)
        self.assertFalse(d3 is d2)
        self.assertTrue(d3 == d2)
        self.assertTrue(d3 == d1)

        d1.characters.append(Character(20, 123123))
        self.assertTrue(len(d1.characters) > len(d2.characters) and len(d1.characters) > len(d3.characters))

    # noinspection PyUnusedLocal
    def test_generic_type(self):
        c1: MyCollection[DerivedClass] = MyCollection([DerivedClass.build() for i in range(200)])

        json_c1 = JsonFormatter.serialize(c1)
        self.assertTrue(json_c1)

        c2 = JsonFormatter.deserialize(json_c1, MyCollection[DerivedClass])
        self.assertTrue(c2 == c1)
        self.assertFalse(c1 is c2)


if __name__ == '__main__':
    unittest.main()
