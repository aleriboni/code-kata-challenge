# -*- coding: utf-8 -*-
from gilded_handler import GildedRoseFactoryHandler


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            provider = GildedRoseFactoryHandler(item).create_handler()
            item.quality = provider.update_quality()
            item.sell_in = provider.update_sell_in()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.name == other.name and self.quality == other.quality and self.sell_in == other.sell_in



