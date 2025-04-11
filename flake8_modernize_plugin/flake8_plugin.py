from flake8_modernize_plugin.cloned_fissix.fissix.refactor import get_fixers_from_package, RefactoringTool
from flake8_modernize_plugin.cloned_modernize.modernize.fixes import fissix_fix_names, opt_in_fix_names, six_fix_names

import logging


class ModernizeCompatibilityPlugin:
    name = "modernize_compatibility_plugin"
    version = "1.0.0"

    def __init__(self, tree, lines, filename):
        self._tree = tree
        self._lines = lines
        self._filename = filename

    def run(self):
        logging.basicConfig(format="%(name)s: %(message)s", level=logging.ERROR)

        options = {
            "print_function": True,
            "exec_function": True,
            "write_unchanged_files": False
        }

        fixer_pkg = "flake8_modernize_plugin.cloned_modernize.modernize.fixes"
        avail_fixes = set(get_fixers_from_package(fixer_pkg))
        avail_fixes.update(fissix_fix_names)
        avail_fixes.update(opt_in_fix_names)
        avail_fixes.update(six_fix_names)
        # avail_fixes.add("flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_unicode")
        # avail_fixes.add("flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_unicode_future")

        rt = RefactoringTool(sorted(avail_fixes), options=options)

        rt.refactor_string(''.join(self._lines), self._filename)

        yield from rt.flake8_errors
