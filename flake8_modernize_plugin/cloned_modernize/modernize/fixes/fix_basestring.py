from __future__ import generator_stop

from flake8_modernize_plugin.cloned_fissix.fissix import fixer_base, fixer_util


class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """'basestring'"""

    def transform(self, node, results):
        fixer_util.touch_import(None, "six", node)
        return fixer_util.Name("six.string_types", prefix=node.prefix)
