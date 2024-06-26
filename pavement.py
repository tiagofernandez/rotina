import os, sys

from paver.easy import consume_args, needs, sh, task

# Add the current folder to the system path
sys.path.append(os.path.dirname(__file__))

@task
def setup():
    """Setups the project."""
    sh('bower install')
    sh('npm install --save-dev')
    sh('gulp setup')

@task
def deps():
    """Installs the required dependencies for the development environment."""
    for env in ['dev', 'test']:
        sh('pip install --quiet --upgrade -r requirements/%s.txt' % env)

@task
def migrate():
    """Synchronizes the database according to migrations."""
    sh_manage('migrate --noinput')

@task
def makemigrations():
    """Generates migrations for the installed apps."""
    sh_manage('makemigrations')

@task
def shell():
    """Opens a Python shell in the development environment."""
    sh_manage('shell_plus --ipython')

@task
@consume_args
def test(args):
    """Executes the unit tests."""
    for target in args if len(args) > 0 else list_apps():
        sh_manage('test --settings=rotina.settings.test %s' % target)

@task
@needs(['migrate'])
def run():
    """Runs the development web server."""
    sh_manage('runserver_plus 0.0.0.0:8000 --settings=rotina.settings.dev')

def sh_manage(command, capture=False):
    """Runs a shell command through Django's manage.py."""
    return sh('python manage.py %s' % command, capture=capture)

def list_apps():
    """Lists apps within the application module."""
    from rotina.settings.common import INSTALLED_APPS
    return [app for app in INSTALLED_APPS if app.startswith('rotina')]
