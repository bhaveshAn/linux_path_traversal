#!/usr/bin/env python

import sys

from file_structure import FileStructure

CMDS = ["cd", "mkdir", "pwd", "rm", "ls"]

sys.stdout.write("Application started...\n")
trie = FileStructure()

while True:
    cmd = input("$ ")
    if cmd == "session clear":
        trie = FileStructure()
        print("SUCC: CLEARED: RESET TO ROOT")
        continue
    print(trie.process(cmd))
