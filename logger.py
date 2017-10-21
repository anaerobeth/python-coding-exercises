import logging

# CRITICAL 50
# ERROR 40
# WARNING 30
# INFO 20
# DEBUG 10

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        logging.debug("Item created: {}({})".format(self.name, self.value))

    def buy(self, quantity=1):
        logging.debug("Bought item: '{}'".format(self.name))

    def sell(self, quantity=1):
        logging.debug("Sold item: '{}'".format(self.name))

item = Item('gold', 100)
item.buy()
item.sell()

