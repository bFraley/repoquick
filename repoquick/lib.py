# repoquick_lib.py

import sys, os
from . dialogue import *

class RepoQuick():
    def __init__(self):
        self.osname = os.name

    # Execute shell commands.
    def call(self, shell_string):
        if os.system(shell_string):
            return True
        else:
            return False

    # Check for compatible POSIX OS.
    def check_posix(self):
        if not self.osname == 'posix':
            print('repoquick: posix OS required.\n')
            exit(1)

    def touch_license_file(self, license_filename):
        command_string = 'cp _licenses/{} ./LICENSE'.format(license_filename)
        self.call(command_string)


    def touch_ignore_file(self, ignore_filename):
        command_string = 'cp _ignore/{} ./.gitignore'.format(ignore_filename)
        self.call(command_string)


def start():
    arg_length = len(sys.argv)
    rq = RepoQuick()
    rq.check_posix()

    if not arg_length > 1:
        print('\nrepoquick:\nNo arguments provided. Get help by typing: repoquick help\n')
        exit(0)

    command_text = sys.argv[1]
    
    if not command_text in commands:
        error_str ='\nrepoquick:\nUnrecognized command "{}"'.format(command_text)
        print(error_str)
        exit(0)

    if not arg_length > 2:
        error_str = '\nrepoquick:\nCommand: {} requires an option'.format(command_text)
        print(error_str)
        exit(0)

    command_option = sys.argv[2]


    if command_text == 'license':
        rq.touch_license_file(command_option)

    elif command_text == 'ignore':
        rq.touch_ignore_file(command_option)  
    
