#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
import os

# External imports

# Bokeh imports

# Module under test
import bokeh.ext as ext

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def test_ext_commands(tmpdir):
    assert _names(tmpdir) == []

    assert ext.init(tmpdir, development=True) is True
    assert _names(tmpdir) == [
        "bokeh.ext.json",
        "index.ts",
        "package.json",
        "tsconfig.json",
    ]

    assert ext.build(tmpdir) is True
    assert _names(tmpdir) == [
        ".bokeh",
        "bokeh.ext.json",
        "dist",
        "index.ts",
        "node_modules",
        "package-lock.json",
        "package.json",
        "tsconfig.json",
    ]

    assert ext.init(tmpdir) is False

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

def _entries(path):
    return sorted(os.scandir(path), key=lambda entry: entry.name)

def _names(path):
    return [ entry.name for entry in _entries(path) ]

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
