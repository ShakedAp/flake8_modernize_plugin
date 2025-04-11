from __future__ import generator_stop

from cloned_fissix.fissix import fixer_base
from cloned_fissix.fissix.fixer_util import Name


class FixFile(fixer_base.BaseFix):

    BM_compatible = True
    order = "pre"

    PATTERN = """
    power< name='file'
        trailer<
            '(' any ')'
        > any*
    >
    """

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name("open", prefix=name.prefix))
