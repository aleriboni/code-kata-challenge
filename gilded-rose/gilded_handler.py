from gilded_rose import Item


class GildedRoseFactoryHandler:

    def __init__(self, item: Item):
        self.item = item

    def create_handler(self):

        if self.item.name == "Aged Brie":
            return AgeBrieHandler(self.item)
        if self.item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasHandler(self.item)
        if self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesProvider(self.item)
        if self.item.name == "Conjured":
            return ConjuredHandler(self.item)
        else:
            return ItemHandler(self.item)


class ItemHandler:

    def __init__(self, item: Item):
        self.item = item
        self.min_quality = 0
        self.max_quality = 50

    def update_quality(self):

        if self.item.sell_in > 0:
            quality = self.item.quality - 1
        else:
            quality = self.item.quality - 2

        return max(quality, self.min_quality)

    def update_sell_in(self):

        return self.item.sell_in - 1


class AgeBrieHandler(ItemHandler):

    def update_quality(self):

        if self.item.sell_in > 0:
            quality = self.item.quality + 1
        else:
            quality = self.item.quality + 2

        return min(quality, self.max_quality)


class SulfurasHandler(ItemHandler):

    def __init__(self, item: Item):
        super().__init__(item)
        self.max_quality = 80

    def update_quality(self):
        return self.item.quality

    def update_sell_in(self):
        return self.item.sell_in


class BackstagePassesProvider(ItemHandler):

    def update_quality(self):

        if self.item.sell_in <= 0:
            quality = 0
        elif self.item.sell_in <= 5:
            quality = self.item.quality + 3
        elif self.item.sell_in <= 10:
            quality = self.item.quality + 2
        else:
            quality = self.item.quality + 1

        return min(quality, self.max_quality)


class ConjuredHandler(ItemHandler):

    def update_quality(self):

        if self.item.sell_in > 0:
            quality = self.item.quality - 2
        else:
            quality = self.item.quality - 4

        return max(quality, self.min_quality)
