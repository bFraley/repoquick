from distutils.core import setup
setup(
  name = 'repoquick',
  packages = ['repoquick'],
  version = '1.0',
  description = 'git repo starter utility for gitignore and license files',
  author = 'Brett Fraley',
  author_email = 'brettfraley@gmail.com',
  url = 'https://github.com/bfraley/repoquick',
  download_url = 'https://github.com/bfraley/repoquick/tarball/1.0',
  keywords = ['repoquick ignore', 'repoquick license', 'repo starter tool'],
  classifiers = [],
  scripts=['bin/repoquick'],
)
