# Copyright 2006 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer that turns 'long' into 'int' everywhere.
"""

# Local imports
from flake8_modernize_plugin.cloned_fissix.fissix import fixer_base
from flake8_modernize_plugin.cloned_fissix.fissix.fixer_util import is_probably_builtin


class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def transform(self, node, results):
        if is_probably_builtin(node):
            node.value = "int"
            node.changed()
