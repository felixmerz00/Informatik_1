# Variables can either be defined and directly used...
# or provided during script invocation like in this task. You
# MUST use the REPO_URL variable that points to a repository.
# But you should NOT define REPO_URL in this script. When
# testing your solution locally, you must define it before
# calling script.sh (as shown in the task descption):
# REPO_URL="some-url" ./script.sh

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.

git clone $REPO_URL repo
cd repo

git checkout -b feature_x
printf 'print("Hello World!")' > hello.py
git add hello.py
git commit -m 'Add "Hello World" example'
git push origin feature_x
git checkout master
printf '# good bye' > bye.py
git add bye.py
git commit -m 'Add "Good Bye" comment'
git merge feature_x -m 'Merge "feature_x"'

git push origin master