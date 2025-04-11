from cloned_fissix.fissix.refactor import get_fixers_from_package, RefactoringTool
from cloned_modernize.modernize.fixes import fissix_fix_names, opt_in_fix_names, six_fix_names

import logging


if __name__ == '__main__':

    logging.basicConfig(format="%(name)s: %(message)s", level=logging.ERROR)

    options = {
        "print_function": False,
        "exec_function": True,
        "write_unchanged_files": False
    }

    fixer_pkg = "cloned_modernize.modernize.fixes"
    avail_fixes = set(get_fixers_from_package(fixer_pkg))
    avail_fixes.update(fissix_fix_names)
    avail_fixes.update(opt_in_fix_names)
    avail_fixes.update(six_fix_names)
    # avail_fixes.add("cloned_modernize.modernize.fixes.fix_unicode")
    # avail_fixes.add("cloned_modernize.modernize.fixes.fix_unicode_future")

    rt = RefactoringTool(sorted(avail_fixes), options=options)

    rt.refactor(['.'])
    print(rt.flake8_errors)

    return_code = int(bool(rt.errors))
