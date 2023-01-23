# -*- coding: utf-8 -*-
"""
Python Stockfish

Makefile - Stuff
"""
import os

GIT_DATE: str = os.popen(
    "git show -s --date=format:'%Y%m%d' --format=%cd HEAD 2>/dev/null"
).read()
GIT_SHA: str = os.popen("git rev-parse --short HEAD 2>/dev/null").read()
