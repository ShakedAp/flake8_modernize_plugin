from __future__ import generator_stop

fissix_fix_names = {
    "cloned_fissix.fissix.fixes.fix_apply",
    "cloned_fissix.fissix.fixes.fix_except",
    "cloned_fissix.fissix.fixes.fix_exec",
    "cloned_fissix.fissix.fixes.fix_execfile",
    "cloned_fissix.fissix.fixes.fix_exitfunc",
    "cloned_fissix.fissix.fixes.fix_funcattrs",
    "cloned_fissix.fissix.fixes.fix_has_key",
    "cloned_fissix.fissix.fixes.fix_idioms",
    "cloned_fissix.fissix.fixes.fix_long",
    "cloned_fissix.fissix.fixes.fix_methodattrs",
    "cloned_fissix.fissix.fixes.fix_ne",
    "cloned_fissix.fissix.fixes.fix_numliterals",
    "cloned_fissix.fissix.fixes.fix_operator",
    "cloned_fissix.fissix.fixes.fix_paren",
    "cloned_fissix.fissix.fixes.fix_reduce",
    "cloned_fissix.fissix.fixes.fix_renames",
    "cloned_fissix.fissix.fixes.fix_repr",
    "cloned_fissix.fissix.fixes.fix_set_literal",
    "cloned_fissix.fissix.fixes.fix_standarderror",
    "cloned_fissix.fissix.fixes.fix_sys_exc",
    "cloned_fissix.fissix.fixes.fix_throw",
    "cloned_fissix.fissix.fixes.fix_tuple_params",
    "cloned_fissix.fissix.fixes.fix_types",
    "cloned_fissix.fissix.fixes.fix_ws_comma",
    "cloned_fissix.fissix.fixes.fix_xreadlines",
}

# fixes that involve using six
six_fix_names = {
    "cloned_modernize.modernize.fixes.fix_basestring",
    "cloned_modernize.modernize.fixes.fix_dict_six",
    "cloned_modernize.modernize.fixes.fix_filter",
    "cloned_modernize.modernize.fixes.fix_imports_six",
    "cloned_modernize.modernize.fixes.fix_itertools_six",
    "cloned_modernize.modernize.fixes.fix_itertools_imports_six",
    "cloned_modernize.modernize.fixes.fix_input_six",
    "cloned_modernize.modernize.fixes.fix_int_long_tuple",
    "cloned_modernize.modernize.fixes.fix_map",
    "cloned_modernize.modernize.fixes.fix_metaclass",
    "cloned_modernize.modernize.fixes.fix_raise_six",
    "cloned_modernize.modernize.fixes.fix_unicode",
    "cloned_modernize.modernize.fixes.fix_unicode_type",
    "cloned_modernize.modernize.fixes.fix_urllib_six",
    "cloned_modernize.modernize.fixes.fix_unichr",
    "cloned_modernize.modernize.fixes.fix_xrange_six",
    "cloned_modernize.modernize.fixes.fix_zip",
}

# Fixes that are opt-in only.
opt_in_fix_names = {
    "cloned_modernize.modernize.fixes.fix_classic_division",
    "cloned_modernize.modernize.fixes.fix_open",
}
