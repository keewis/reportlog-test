import pytest


def test_pass():
    pass


def test_fail():
    assert False


@pytest.mark.skip(reason="skipped")
def test_skip():
    pass


@pytest.mark.xfail(reason="xfailed")
def test_xfail():
    assert False


@pytest.mark.xfail(reason="xpassed")
def test_xpass():
    pass


@pytest.fixture
def failing_fixture():
    raise RuntimeError("error")

    yield None


def test_error(failing_fixture):
    pass
