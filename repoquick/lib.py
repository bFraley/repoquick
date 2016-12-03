# repoquick_lib.py

import sys, os

from dialogue import license_names, ignore_names, authors, year

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
        command_string = 'cp ../_licenses/{} ./LICENSE'.format(license_filename)
        os.call(command_string)


    def touch_ignore_file(self, ignore_filename):
        command_string = 'cp ../_ignore/{} ./.gitignore'.format(ignore_filename)
        os.call(command_string)



def start():
    rq = RepoQuick()
    rq.check_posix()

    if not len(sys.argv) > 1:
        print(dialogue.version_text)
        print(dialogue.help_text)
        exit(0)
    else:
        command_text = sys.argv[1]
        print('got argv1 = {}'.format(command_text))
    
