import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arsenal.forensics.decode import desfa

def test_base64():
    strat, b = desfa("U2FsdXQ=")

    assert strat == "base64"

    assert b == b"Salut"