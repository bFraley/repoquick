# repoquick test file

from nose.tools import *

from repoquick.lib import RepoQuick, start
from repoquick.dialogue import *

rq = RepoQuick()

def test_repoquick_dialogue():
    print(author)
    print(year)

    for (k,v) in license_names.items():
        print(k, v)

    for (k,v) in ignore_names.items():
        print(k,v)

def test_rq_check_posix():
    rq.check_posix()
