#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: getTables.py                                                      #
# File Path: /getTables.py                                                     #
# Created Date: 2020-10-19                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-10-19 1:52:08 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

"""
Description: This program working in MacOS will grab all of the Access DB's tables in a specificed working directory, and export to file has the same name as Access DB.

OS: MacOS
Prerequisite:
- Homebrew:  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
- mdbtools: brew install mdbtools
"""

DBPath=input("")