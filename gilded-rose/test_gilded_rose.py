# -*- coding: utf-8 -*-
import unittest

from gilded_rose_refactored import GildedRose, Item

INPUT_ITEMS = [
    Item("Backstage passes to a TAFKAL80ETC concert", 10, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 5, 42),
    Item("Backstage passes to a TAFKAL80ETC concert", 0, 10),
    Item("Foo Item", 1, 1),
    Item("Foo Item", 0, 0),
    Item("Aged Brie", 10, 10),
    Item("Aged Brie", 1, 10),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Sulfuras, Hand of Ragnaros", 1, 80),
]

EXPECTED_ITEMS = [
    Item("Backstage passes to a TAFKAL80ETC concert", 9, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", 4, 45),
    Item("Backstage passes to a TAFKAL80ETC concert", -1, 0),
    Item("Foo Item", 0, 0),
    Item("Foo Item", -1, 0),
    Item("Aged Brie", 9, 11),
    Item("Aged Brie", 0, 11),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Sulfuras, Hand of Ragnaros", 1, 80),
]


class GildedRoseTest(unittest.TestCase):

    def test_update_quality(self):
        gilded_rose = GildedRose(INPUT_ITEMS)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items, EXPECTED_ITEMS)


if __name__ == '__main__':
    unittest.main()
