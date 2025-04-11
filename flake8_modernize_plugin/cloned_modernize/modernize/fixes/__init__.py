from __future__ import generator_stop

fissix_fix_names = {
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_apply",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_except",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_exec",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_execfile",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_exitfunc",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_funcattrs",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_has_key",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_idioms",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_long",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_methodattrs",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_ne",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_numliterals",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_operator",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_paren",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_reduce",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_renames",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_repr",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_set_literal",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_standarderror",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_sys_exc",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_throw",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_tuple_params",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_types",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_ws_comma",
    "flake8_modernize_plugin.cloned_fissix.fissix.fixes.fix_xreadlines",
}

# fixes that involve using six
six_fix_names = {
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_basestring",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_dict_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_filter",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_imports_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_itertools_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_itertools_imports_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_input_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_int_long_tuple",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_map",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_metaclass",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_raise_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_unicode",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_unicode_type",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_urllib_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_unichr",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_xrange_six",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_zip",
}

# Fixes that are opt-in only.
opt_in_fix_names = {
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_classic_division",
    "flake8_modernize_plugin.cloned_modernize.modernize.fixes.fix_open",
}
