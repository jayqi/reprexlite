import platform

from reprexlite.session_info import SessionInfo


def test_session_info():
    session_info = str(SessionInfo())
    assert session_info
    assert platform.python_version() in session_info
    assert "pytest" in session_info
