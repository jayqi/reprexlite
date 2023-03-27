import pytest


def pytest_configure(config):
    try:
        import IPython

        print(IPython.__version__)
        pytest.IPYTHON_IS_AVAILABLE = True
    except ModuleNotFoundError as e:
        if e.name == "IPython":
            pytest.IPYTHON_IS_AVAILABLE = False
        else:
            raise

    try:
        import black

        print(black.__version__)
        pytest.BLACK_IS_AVAILABLE = True
    except ModuleNotFoundError as e:
        if e.name == "black":
            pytest.BLACK_IS_AVAILABLE = False
        else:
            raise

    try:
        import pygments

        print(pygments.__version__)
        pytest.PYGMENTS_IS_AVAILABLE = True
    except ModuleNotFoundError as e:
        if e.name == "pygments":
            pytest.PYGMENTS_IS_AVAILABLE = False
        else:
            raise

    try:
        import rich

        pytest.RICH_IS_AVAILABLE = True
    except ModuleNotFoundError as e:
        if e.name == "rich":
            pytest.RICH_IS_AVAILABLE = False
        else:
            raise
