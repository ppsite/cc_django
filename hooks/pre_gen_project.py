import re
import sys
from subprocess import check_call


class GenericHooks(object):
    TERMINATOR = "\x1b[0m"
    WARNING = "\x1b[1;33m [WARNING]: "
    INFO = "\x1b[1;33m [INFO]: "
    HINT = "\x1b[3;33m"
    SUCCESS = "\x1b[1;32m [SUCCESS]: "

    def __init__(self):
        self.hint('[^_^] Hi Man, Welcome to STAR: https://github.com/pyfs/cc_django')

    def info(self, content):
        print(self.INFO + content + self.TERMINATOR)

    def warning(self, content):
        print(self.WARNING + content + self.TERMINATOR)

    def hint(self, content):
        print(self.HINT + content + self.TERMINATOR)

    def success(self, content):
        print(self.SUCCESS + content + self.TERMINATOR)

    def __del__(self):
        self.hint('[!] Well Done, enjoy coding now !')


class PreGenProjectHooks(GenericHooks):
    """生成项目前的钩子"""
    ENV_COMMANDS = [
        'pyenv virtualenv 3.7.5 {{cookiecutter.project_name}}',
        'pyenv local {{cookiecutter.project_name}}',
        'pip install --upgrade pip'
    ]

    # 依赖关系
    REQUIREMENTS = {
        'default': {
            'input': 'Y',
            'pkg': [
                'Django==2.2.14',
                'wrapt',
                'Pillow',
                'django-model-utils',
                'psycopg2-binary',
                'uWSGI'
            ],
        },
        'celery': {
            'input': '{{cookiecutter.use_celery}}',
            'pkg': [
                'django-celery-beat',
                'celery'
            ],
        },
        'grappelli': {
            'input': '{{cookiecutter.use_grappelli}}',
            'pkg': [
                'django-grappelli',
                'django-filebrowser',
                'feedparser'
            ],
        },
        'mdeditor': {
            'input': '{{cookiecutter.use_mdeditor}}',
            'pkg': [
                'django-mdeditor'
            ],
        },
        'taggit': {
            'input': '{{cookiecutter.use_taggit}}',
            'pkg': [
                'django-taggit',
                'django-taggit-serializer'
            ]
        },
        'drf': {
            'input': '{{cookiecutter.use_drf}}',
            'pkg': [
                'djangorestframework',
                'djangorestframework-jwt',
                'django-filter',
                'markdown',
            ]
        },
        'demo': {
            'input': '{{cookiecutter.use_demo}}',
            'pkg': [
                'django-mptt',
                'djangorestframework-recursive',
                'django-taggit',
                'django-taggit-serializer'
            ]
        }
    }

    @staticmethod
    def check_project_name():
        """检查项目名称是否合规"""
        module_reg = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
        module_name = '{{ cookiecutter.project_name }}'
        if not re.match(module_reg, module_name):
            print('ERROR: The project name(%s) invalid Python module name. use _ instead of -' % module_name)
            sys.exit(1)

    def pyenv_create_virtualenv(self):
        """使用 pyenv 创建虚拟环境"""
        self.info('[!] pyenv 创建虚拟环境')
        for cmd in self.ENV_COMMANDS:
            self.success('[!] %s' % cmd)
            check_call(cmd.split())

    def pip_install_requirements(self):
        """按需安装依赖包"""
        self.warning('[!] requirements check list')
        requirements = []
        for key, item in self.REQUIREMENTS.items():
            if item['input'].strip().lower() == 'y':
                requirements += item['pkg']
                self.success('[!] %s requires: %s' % (key, ', '.join(item['pkg'])))
        self.warning('[!] installing ...')
        cmd = ['pip', 'install'] + requirements
        check_call(cmd)


if __name__ == '__main__':
    hooks = PreGenProjectHooks()
    hooks.check_project_name()
    hooks.pyenv_create_virtualenv()
    hooks.pip_install_requirements()
