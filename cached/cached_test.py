import math

from cached import cached, auto_cached


class Number:
    def __init__(self, x, counters):
        self._x = x
        self._counters = counters

    def value(self):
        return self._x

    @cached("_sqrd_x")
    def value_squared(self):
        # Keep track of the amount of times this method has been called
        self._counters["value_squared"] += 1
        return self._x ** 2

    @cached("_sqrt_x")
    def square_root_value(self):
        # Keep track of the amount of times this method has been called
        self._counters["square_root_value"] += 1
        return math.sqrt(self._x)

    @auto_cached
    def value_cubed(self):
        # Keep track of the amount of times this method has been called
        self._counters["value_cubed"] += 1
        return self._x ** 3


if __name__ == "__main__":
    x = 25
    counters = {"value_squared": 0, "square_root_value": 0, "value_cubed": 0}
    number = Number(x=x, counters=counters)

    assert number.value() == x

    assert number.value_squared() == x ** 2
    assert counters["value_squared"] == 1

    assert number.square_root_value() == math.sqrt(x)
    assert counters["square_root_value"] == 1

    assert number.value_cubed() == x ** 3
    assert counters["value_cubed"] == 1

    # Show that x ^ 2 is now cached
    number.value_squared()
    number.value_squared()
    assert counters["value_squared"] == 1

    # Show that sqrt(x) is now cached
    number.square_root_value()
    number.square_root_value()
    assert counters["square_root_value"] == 1

    # Show that x ^ 3 is now cached
    number.value_cubed()
    number.value_cubed()
    assert counters["value_cubed"] == 1

    print("All tests passed successfully.")
