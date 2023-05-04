# -*- coding: utf-8 -*-
import unittest

from gilded_rose_refactored import Item
from gilded_handler import GildedRoseFactoryHandler, ItemHandler, SulfurasHandler, \
    BackstagePassesProvider, ConjuredHandler, AgeBrieHandler


class GildedRoseFactoryHandlerTest(unittest.TestCase):

    def test_create_handler(self):

        foo_item = Item("foo", 0, 0)
        handler = GildedRoseFactoryHandler(foo_item).create_handler()
        self.assertIsInstance(handler, ItemHandler)

        sulfuras_item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
        handler = GildedRoseFactoryHandler(sulfuras_item).create_handler()
        self.assertIsInstance(handler, SulfurasHandler)

        backstage_item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        handler = GildedRoseFactoryHandler(backstage_item).create_handler()
        self.assertIsInstance(handler, BackstagePassesProvider)

        conjured_item = Item("Conjured", 0, 0)
        handler = GildedRoseFactoryHandler(conjured_item).create_handler()
        self.assertIsInstance(handler, ConjuredHandler)

        age_brie_item = Item("Aged Brie", 0, 0)
        handler = GildedRoseFactoryHandler(age_brie_item).create_handler()
        self.assertIsInstance(handler, AgeBrieHandler)


if __name__ == '__main__':
    unittest.main()
