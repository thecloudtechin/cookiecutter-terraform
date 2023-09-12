import os
import shutil
from subprocess import Popen

print(os.getcwd()) 

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

def init_terraform():
    """
    Initialises terraform on the new project folder
    """
    TERRAFORM_COMMANDS = [
        ["terraform", "init"],
        ["terraform", "validate"],
        ["terraform", "plan"],
#        ["terraform", "plan", "-a", "-m", ":cookie: Initial Commit :rocket:"],
#        ["git", "branch", "-m", "master", "main"]
    ]

    for command in TERRAFORM_COMMANDS:
        terraform = Popen(command, cwd=PROJECT_DIRECTORY)
        terraform.wait()

#####################

# Remove unused files
# create_pytest = '{{cookiecutter.use_pytest}}' == 'y'
# create_pylint = '{{cookiecutter.use_pylint}}' == 'y'
# create_github_actions = '{{cookiecutter.use_github_actions}}' == 'y'

# if not create_pytest:
#     remove('{{cookiecutter.project_slug}}/test_main.py')

# if not create_pylint:
#     remove('{{cookiecutter.project_slug}}/.pylintrc')

# if not create_github_actions:
#     remove('.github')

# # Initialize Git (should be run after all file have been modified or deleted)
# if '{{ cookiecutter.use_git }}'.lower() == 'y':
#     init_git()
# else:
#     remove(".gitignore")
#     remove('.github')
