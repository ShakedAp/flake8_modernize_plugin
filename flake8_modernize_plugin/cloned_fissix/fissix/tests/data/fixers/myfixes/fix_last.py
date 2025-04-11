from flake8_modernize_plugin.cloned_fissix.fissix.fixer_base import BaseFix


class FixLast(BaseFix):

    run_order = 10

    def match(self, node):
        return False
