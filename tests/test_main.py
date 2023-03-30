
import pytest

from demo_workflow_pypi import *


def test_add():
    addition = add(1, 3)
    assert addition == 4, "failed"
