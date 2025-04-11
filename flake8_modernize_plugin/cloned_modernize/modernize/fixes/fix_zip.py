# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from __future__ import generator_stop

from cloned_fissix.fissix import fixer_util
from cloned_fissix.fissix.fixes import fix_zip


class FixZip(fix_zip.FixZip):

    skip_on = "six.moves.zip"

    def transform(self, node, results):
        result = super().transform(node, results)
        # Always use six.moves.zip so that even Python 2.7 gets performance
        # boost from using itertools in iterator contexts.
        fixer_util.touch_import("six.moves", "zip", node)
        return result
