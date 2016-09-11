"""
Items
"""


class Item:
    def __init__(self, name, key, skill, description='', equipment=False):
        self.name = name
        self.key = key
        self.skill = skill
        self.description = description
        self.equipment = equipment

    def is_equipment(self):
        return True if self.equipment else False


def the_item(item_key):
    """
    Item caller
    :param item_key: string currently second part of item class name
    :return: the item class
    """
    return globals()['Item_'+item_key]


def create_item(item_key):
    return the_item(item_key)()


class Item_A2(Item):
    def __init__(self, name='大力手套', key='A2', category='weapon', skill='attack2',
                 description='可以强化佩戴者手部力量',
                 equipment=True):
        super(Item_A2, self).__init__(name=name, key=key, skill=skill, description=description,
                                      equipment=equipment)

        self.category = category

