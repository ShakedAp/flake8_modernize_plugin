from __future__ import generator_stop

from flake8_modernize_plugin.cloned_fissix.fissix.fixes import fix_print

from .. import utils


class FixPrint(fix_print.FixPrint):
    def transform(self, node, results):
        result = super().transform(node, results)
        utils.add_future(node, "print_function")
        return result
