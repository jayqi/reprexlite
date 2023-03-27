import pytest

# Requires invoking with pytest

## SKIP DECORATORS

requires_ipython = pytest.mark.skipif(
    not pytest.IPYTHON_IS_AVAILABLE, reason="ipython is not available"
)
requires_no_ipython = pytest.mark.skipif(
    pytest.IPYTHON_IS_AVAILABLE, reason="ipython is available"
)
requires_black = pytest.mark.skipif(not pytest.BLACK_IS_AVAILABLE, reason="black is not available")
requires_no_black = pytest.mark.skipif(pytest.BLACK_IS_AVAILABLE, reason="black is available")
requires_pygments = pytest.mark.skipif(
    not pytest.PYGMENTS_IS_AVAILABLE, reason="pygments is not available"
)
requires_no_pygments = pytest.mark.skipif(
    pytest.PYGMENTS_IS_AVAILABLE, reason="pygments is available"
)
requires_rich = pytest.mark.skipif(not pytest.RICH_IS_AVAILABLE, reason="rich is not available")
requires_no_rich = pytest.mark.skipif(pytest.RICH_IS_AVAILABLE, reason="rich is available")
