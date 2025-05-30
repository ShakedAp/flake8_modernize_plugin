#!/usr/bin/env python3
import abc
from typing import Iterable

from flake8_modernize_plugin.flake8_errors_info import MDNErrorInfo


def _should_update_error_counter(bases: Iterable[type]) -> bool:
    """
    Args:
        bases (Iterable[type]): the classes to check.

    Returns:
        bool: True if error counter should be updated, False otherwise.
    """
    if not bases:
        return False
    if abc.ABC in bases:
        return False
    return True


class MdnCheckerMeta(abc.ABCMeta):
    """
    The metclass for MDN Checkers.
    This metaclass gives each checker that inherits it a unique error_number
    The given error_number will shown when an error occured.

    Any class that will be the first to use this metaclass will not get an error_number.
    Any class that inherits abc.ABC will not get an error_number.
    """

    _error_number_counter = 1

    def __new__(cls, name, bases, dct):
        if _should_update_error_counter(bases):
            error_number = cls._error_number_counter
            cls._error_number_counter += 1
        else:
            error_number = 0

        self = type.__new__(cls, name, bases, dct)
        self.error_number = error_number
        return self


def _get_error_representation(node):
    node_str = str(node).strip()
    str_arr = [elem for elem in node_str.split('\n') if not elem.strip().startswith('#')]
    error_represenation = str_arr[0]
    return error_represenation

class MdnFixer(metaclass=MdnCheckerMeta):
    """
    The base class for each mdn checker.


    Make sure *not* to override error_number, unless a specific error number is wanted.
    """

    @classmethod
    def _create_mdn_error(cls, node, new_node) -> MDNErrorInfo:
        """create the given error info based on the given node.
        This uses the defined error_message, and the automatically given error_number.
        If this method is not used, make sure to use those class member.

        Args:
            node: fissix Node or fissix Leaf
            new_node: fissix Node or fissix Leaf

        Returns:
            MDNErrorInfo: The created error info.
        """
        try:
            fixer_name = cls.__module__.split("cloned_")[1]
        except Exception:
            fixer_name = cls.__module__

        return MDNErrorInfo(
            node.lineno,
            node.column,
            cls.error_number,
            f"Fixer {fixer_name}: Use {_get_error_representation(new_node)} instead of {_get_error_representation(node)}. See modernize for futher details",
            cls,
        )

    @classmethod
    def _create_unknown_mdn_error(cls, node) -> MDNErrorInfo:
        """create the given error info based on the given node.
        This uses the defined error_message, and the automatically given error_number.
        If this method is not used, make sure to use those class member.

        Args:
            node: fissix Node or fissix Leaf

        Returns:
            MDNErrorInfo: The created error info.
        """
        try:
            fixer_name = cls.__module__.split("cloned_")[1]
        except Exception:
            fixer_name = cls.__module__

        return MDNErrorInfo(
            node.lineno,
            node.column,
            cls.error_number,
            f"Fixer {fixer_name} error that couldn't be shown (other lines changed). See modernize for futher details",
            cls,
        )


    @classmethod
    def _create_added_mdn_error(cls, node, added_node) -> MDNErrorInfo:
        """create the given error info based on the given node.
        This uses the defined error_message, and the automatically given error_number.
        If this method is not used, make sure to use those class member.

        Args:
            node: fissix Node or fissix Leaf
            added_node: fissix Node or fissix Leaf

        Returns:
            MDNErrorInfo: The created error info.
        """
        try:
            fixer_name = cls.__module__.split("cloned_")[1]
        except Exception:
            fixer_name = cls.__module__

        return MDNErrorInfo(
            node.lineno,
            node.column,
            cls.error_number,
            f"Fixer {fixer_name}: Add {_get_error_representation(added_node)}. See modernize for futher details",
            cls,
        )
