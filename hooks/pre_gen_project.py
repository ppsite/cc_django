import re
import sys
from subprocess import check_call


class PreGenProjectHooks(object):
    """生成项目前的钩子"""
    ENV_COMMANDS = [
        'pyenv virtualenv 3.7.5 {{cookiecutter.project_name}}',
        'pyenv local {{cookiecutter.project_name}}'
    ]

    @staticmethod
    def check_project_name():
        module_reg = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
        module_name = '{{ cookiecutter.project_name }}'
        if not re.match(module_reg, module_name):
            print('ERROR: The project name(%s) invalid Python module name. use _ instead of -' % module_name)
            sys.exit(1)

    def pyenv_virtualenv(self):
        for cmd in self.ENV_COMMANDS:
            check_call(cmd.split())


if __name__ == '__main__':
    hooks = PreGenProjectHooks()
    hooks.check_project_name()
    hooks.pyenv_virtualenv()
