import numpy as np
import pytest

from demo_workflow_package import *


def test_add():
    addition = add(1, 3)
    assert addition == 3, "failed"

    sub = sub(2, 1)
    assert sub == 1, "failed"
