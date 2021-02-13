from textwrap import dedent
from reprexlite import reprex


def test_source():
    source = dedent(
        """\
        x = 2+2
        y = [1,2,3]
        [i+x for i in y]
        """
    )

    reprex(source)
