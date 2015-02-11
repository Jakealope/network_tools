from echo_client import clientmessage
import pytest


def test_unicode():
    assert clientmessage("this is a test") == "this is a test"
