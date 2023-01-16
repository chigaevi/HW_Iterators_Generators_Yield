class FlatIterator:

    def __init__(self, list_of_list):
        self.raw_list = list_of_list

    def __iter__(self):
        self.irl = 0
        self.iil = 0
        return self

    def __next__(self):
        if len(self.raw_list) == self.irl:
            raise StopIteration
        item_list = self.raw_list[self.irl]
        item = item_list[self.iil]
        if len(item_list) > self.iil+1:
            self.iil += 1
        else:
            self.irl += 1
            self.iil = 0
        return item


def flat_generator(raw_list):
    i = 0
    while True:
        if len(raw_list) == i:
            break
        item_list = raw_list[i]
        if len(item_list) != 0:
            item = item_list.pop(0)
            yield item
        else:
            i += 1

