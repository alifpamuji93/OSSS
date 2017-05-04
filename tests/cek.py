from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )
str = type('')

import sys
import pytest

from model.camera import VideoCamera

camera = VideoCamera()

camera.rekam()