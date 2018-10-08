#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


def execute(cmd):
    process = os.popen(cmd)
    output = process.read()
    process.close()
    return output