# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from __future__ import generator_stop

from flake8_modernize_plugin.cloned_fissix.fissix import fixer_util
from flake8_modernize_plugin.cloned_fissix.fissix.fixes import fix_map

from .. import utils


class FixMap(fix_map.FixMap):

    skip_on = "six.moves.map"

    def transform(self, node, results):
        result = super().transform(node, results)
        if not utils.is_listcomp(result):
            # Always use the import even if no change is required so as to have
            # improved performance in iterator contexts even on Python 2.7.
            fixer_util.touch_import("six.moves", "map", node)
        return result
