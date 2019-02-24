from fabric.api import env, local, cd, run
import config

env.hosts = [config.PRODUCTION_HOST]


def deploy():
    local('git push')
    with cd('~/karl'):
        run('git pull')
        run('pipenv install')
        run('supervisorctl restart karl')
