from .ExecutionCounter import count


def test_one():
    @count
    def f(a, b):
        return a + b
    assert f(2, 5) == 7
    assert f.exec_count == 1


def test_two():
    @count
    def g(a):
        return a + 1
    assert g(1) == 2
    assert g(2) == 3
    assert g(5) == 6
    assert g.exec_count == 3


def test_three():
    @count
    def f():
        pass
    for i in range(999):
        f()
    assert f.exec_count == 999


def test_four():
    @count
    def f(a, b="text"):
        return a + b
    assert f("aa") == "aatext"
    assert f("c", b="a") == "ca"
    assert f.exec_count == 2


def test_five():
    @count
    def f():
        pass
    f()
    assert f.exec_count == 1
