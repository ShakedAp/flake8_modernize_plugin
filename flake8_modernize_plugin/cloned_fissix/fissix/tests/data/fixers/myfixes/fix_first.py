from flake8_modernize_plugin.cloned_fissix.fissix.fixer_base import BaseFix


class FixFirst(BaseFix):
    run_order = 1

    def match(self, node):
        return False
