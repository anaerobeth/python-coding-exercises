class C():
    """Manually define getter, setter and deleter methods"""
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property")


c = C()
c.x = 2
print(c.x)


class Parrot():
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage"""
        return self._voltage


class Cprime():
    """Use decorators to define getter, setter and deleter"""
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property"""
        # also has the attributes fget, fset, and fdel
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


