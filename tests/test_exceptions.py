from reprexlite.exceptions import UnexpectedError


def test_unexpected_error_messsage():
    """Test that UnexpectedError adds message to report an issue."""
    e = UnexpectedError("Boo!")
    assert str(e).startswith("Boo! "), str(e)
    assert "report" in str(e), str(e)
    assert "github.com/jayqi/reprexlite/issues" in str(e), str(e)
