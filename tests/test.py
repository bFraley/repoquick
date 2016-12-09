# repoquick test file

from nose.tools import *

from repoquick.lib import RepoQuick, start
from repoquick.dialogue import *

rq = RepoQuick()

def test_repoquick_dialogue():
    print(author)
    print(year)

def test_rq_check_posix():
    rq.check_posix()
