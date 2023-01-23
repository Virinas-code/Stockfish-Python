# -*- coding: utf-8 -*-
"""
Python Stockfish

misc.cpp - Miscalleneous
"""
import datetime

from .makefile import GIT_DATE, GIT_SHA

version: str = "dev"


def engine_info(to_uci: bool = False) -> str:
    """
    Get engine infos.

    :param bool to_uci: True if from `uci` command.
    :return str: Engine infos.
    """
    string_output: str = ""
    string_output += "Stockfish " + version

    if version == "dev":
        string_output += "-"
        if GIT_DATE:
            string_output += GIT_DATE
        else:
            today: str = datetime.date.today().isoformat().replace("-", "")
            string_output += today
        string_output += "-"
        if GIT_SHA:
            string_output += GIT_SHA
        else:
            string_output += "nogit"

    string_output += "\nid author " if to_uci else " by "
    string_output += "the Stockfish developers (see AUTHORS file)"

    return string_output
