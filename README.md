tdd-demo
========

Test Driven Development (TDD) Example

Write a function in Python 3 that returns the largest factor of a number
without importing any libraries except pytest.

The following is how I did a beginning TDD demo in Python from scratch.

The order of the TDD stuff was roughly:
- (930e0c5) Started by creating many separate tests.
- (a3edc9d) Created a stub function to make tests fail.
- (610a0c5) Put meat in the function to make all the tests pass.
- (bae7a0b) Refactored the function.

In adca93f, the tests were refactored to use @pytest.mark.parametrize() to
consolidate the many small tests into a test data dictionaries and a few test
functions. 

## Dependencies

```
tmux
git
Python 3 with the following packages
- execnet==1.2.0
- py==1.4.26
- pytest==2.6.4
- pytest-xdist==1.11
```

## Setup

```
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
```
