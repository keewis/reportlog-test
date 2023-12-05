import pytest
import warnings


class CustomWarning(Warning):
    pass


def warning_func():
    warnings.warn("some warning", CustomWarning, stacklevel=2)


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

def test_warning():
    warnings.warn("warns something", UserWarning)


def test_custom_warning():
    warnings.warn("warns something", CustomWarning)


def test_nested_warning():
    warning_func()


@pytest.fixture
def failing_fixture():
    raise RuntimeError("error")

    yield None


def test_error(failing_fixture):
    pass


@pytest.mark.parametrize("param", range(1000))
def test_parametrized_failure(param):
    raise ValueError(f"invalid value. Try something else.")
