from paver.easy import consume_args, needs, sh, task


@task
@needs(['deps', 'migrate'])
def setup():
    """Setups the project."""
    sh('bower install')
    sh('npm install --save-dev')
    sh('gulp')

@task
@needs(['clean'])
def build():
    sh('rm -rf build/')
    sh('mkdir -p build/static/')
    sh('rsync -av rotina/static/ build/static/')
    sh('cp rotina/templates/index.html build/')

@task
def clean():
    """Removes files generated by build or runtime."""
    sh("find . -name '*.pyc' -print0 | xargs -0 rm")

@task
@consume_args
def deps(args):
    """Installs the required dependencies for an environment: dev, test, or prod."""
    sh('pip install -q -r requirements/%s.txt' % get_env(args))

@task
def migrate():
    """Synchronizes the database according to migrations."""
    sh_manage("migrate")

@task
def shell():
    sh_manage('shell_plus --ipython')

@task
@needs(['deps'])
@consume_args
def run(args):
    """Runs the development web server on port 8000."""
    sh_manage('runserver_plus 0.0.0.0:8000 --settings=rotina.settings.%s' % get_env(args))

def sh_manage(command, capture=False):
    """Runs a shell command through Django's manage.py."""
    return sh("python manage.py %s" % command, capture=capture)

def get_env(args):
    return args[0] if args else 'dev'
