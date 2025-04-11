from flake8_modernize_plugin.cloned_fissix.fissix.fixer_base import BaseFix
from flake8_modernize_plugin.cloned_fissix.fissix.fixer_util import Name


class FixParrot(BaseFix):
    """
    Change functions named 'parrot' to 'cheese'.
    """

    PATTERN = """funcdef < 'def' name='parrot' any* >"""

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name("cheese", name.prefix))
