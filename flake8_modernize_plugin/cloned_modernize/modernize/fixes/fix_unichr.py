from __future__ import generator_stop

from flake8_modernize_plugin.cloned_fissix.fissix import fixer_base, fixer_util
from flake8_modernize_plugin.cloned_fissix.fissix.fixer_util import is_probably_builtin


class FixUnichr(fixer_base.ConditionalFix):
    BM_compatible = True

    skip_on = "six.moves.unichr"
    PATTERN = """'unichr'"""

    def transform(self, node, results):
        if self.should_skip(node):
            return
        if is_probably_builtin(node):
            fixer_util.touch_import("six", "unichr", node)
