#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Stockfish

main.cpp - Launch
"""
from .misc import engine_info


def main(argc: int, argv: list[str]) -> int:
    """
    Start Stockfish.

    :param int argc: Amount of arguments.
    :param list[str] argv: Arguments.
    :return int: Exit code.
    """
    print(engine_info())
