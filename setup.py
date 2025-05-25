import os
import sys
from pathlib import Path

from setuptools import find_packages, setup

ROOT_FOLDER = Path(__file__).parent.absolute()

sys.path.insert(0, str(ROOT_FOLDER))

setup(
    name='discord_bot',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)