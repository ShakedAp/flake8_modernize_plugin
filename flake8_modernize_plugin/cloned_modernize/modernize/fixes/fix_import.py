from __future__ import generator_stop

from flake8_modernize_plugin.cloned_fissix.fissix.fixer_util import syms
from flake8_modernize_plugin.cloned_fissix.fissix.fixes import fix_import

from .. import utils


class FixImport(fix_import.FixImport):

    # Make sure this runs before any other fixer to guarantee that any other
    # added absolute_import doesn't block this fixer's execution.
    run_order = 1

    def transform(self, node, results):
        if self.skip:
            return
        # We're not interested in __future__ imports here
        if (
            node.type == syms.import_from
            and getattr(results["imp"], "value", None) == "__future__"
        ):
            return

        # If there are any non-future imports, add absolute_import
        utils.add_future(node, "absolute_import")
        return super().transform(node, results)
