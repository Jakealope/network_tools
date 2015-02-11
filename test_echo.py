from echo_client import clientmessage
import pytest


def test_ping():
    assert clientmessage("this is a test") == "this is a test"


def test_big():
    assert clientmessage("this is a string that is much longer than the 32 bites that it has to force it to loop") == "this is a string that is much longer than the 32 bites that it has to force it to loop"


def test_empty():
    assert clientmessage("") == ""
