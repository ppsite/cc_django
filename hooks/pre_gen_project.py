import re
import sys


class PreGenProjectHooks(object):
    """生成项目前的钩子"""

    @staticmethod
    def check_project_name():
        module_reg = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
        module_name = '{{ cookiecutter.project_name }}'
        if not re.match(module_reg, module_name):
            print('ERROR: The project name(%s) invalid Python module name. use _ instead of -' % module_name)
            sys.exit(1)


if __name__ == '__main__':
    hooks = PreGenProjectHooks()
    hooks.check_project_name()
