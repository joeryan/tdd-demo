Test Driven Development (TDD) Example

Write a function in Python 3 that returns the largest factor of a number
without importing any libraries except pytest.

Installation:

tmux
# divide into multiple panes

# pane 0:
virtualenv env -p `which python3`
source env/bin/activate
pip freeze >requirements.original
pip install pytest
pip install pytest-xdist
pip freeze >requirements.txt
git init
git ci --allow-empty -m 'Start with empty commit.'

# pane 1
# This pane shows results of tests that are run each time a file is changed.
source env/bin/activate
py.test -f .

# pane 2
watch 'git status'

# pane 0:
# Now do a mix of vi, git add, git commit, and git status commands.
