# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:08:28 2020

@author: lucifelex
"""


"""
import aiml
kernel = aiml.Kernel()
kernel.learn("01-AIML-hello.xml")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))
"""


"""
import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("04-AIML-all.xml")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))
"""


import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("05-AIML-load.xml")
kernel.respond("load aiml b")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))



