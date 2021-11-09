"""
                _ _
               | (_)
   ___ ___   __| |_  __ _ _ __   __ _  ___
  / __/ __| / _` | |/ _` | '_ \ / _` |/ _ \\
 | (_| (__ | (_| | | (_| | | | | (_| | (_) |
  \___\___| \__,_| |\__,_|_| |_|\__, |\___/
        ______  _/ |             __/ |
       |______||__/             |___/
"""

import re
import subprocess


class ColorSchema(object):
    """
    基于 shell 的配色方案
    """
    TERMINATOR = "\033[0m"  # 统一终止符

    FONT_RED = "\033[31m"
    FONT_GREEN = "\033[32m"
    FONT_YELLOW = "\033[33m"
    FONT_BLUE = "\033[34m"
    FONT_VIOLET = "\033[35m"
    FONT_SKY_BLUE = "\033[36m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_VIOLET = "\033[45m"
    BG_SKY_BLUE = "\033[46m"

    def end(self, message):
        print(self.BG_VIOLET + message + self.TERMINATOR)

    def info(self, message):
        message = "[Info] " + message
        print(self.FONT_SKY_BLUE + message + self.TERMINATOR)

    def warning(self, message):
        message = "[🔔️] " + message
        print(self.FONT_YELLOW + message + self.TERMINATOR)

    def error(self, message):
        message = "[🆘] " + message
        print(self.FONT_RED + message + self.TERMINATOR)

    def success(self, message):
        message = "[✅] " + message
        print(self.FONT_GREEN + message + self.TERMINATOR)

    def title(self, message):
        message = "[🚀] " + message
        print(self.BG_GREEN + message + self.TERMINATOR)


class MessageBlock(ColorSchema):
    """
    屏幕输出的信息块，封装统一样式
    """
    TITLE = None
    START = None
    END = None

    def __init__(self):
        if self.TITLE:
            self.title(message=self.TITLE)
        if self.START:
            self.info(message=self.START)
        self.action()
        if self.END:
            self.end(message=self.END)

    def action(self):
        pass

    @staticmethod
    def decode_output(output):
        """
        decode check_output from byte to utf-8
        @param output: subprocess check_output result
        """
        return output.decode('utf-8').strip().strip('\n')


class Welcome(MessageBlock):
    TITLE = "Hi Man, Glad to see you here, Welcome to Star!"
    START = ">>> https://github.com/pyfs/cc_django.git <<<"
    END = "----------------------------------------------------------"

    def action(self):
        print(__doc__)


class WellDone(MessageBlock):
    END = "Congratulations, Well Done Once Again ⛽️⛽️⛽️ \nlast operation execute: make install."


class PreGenError(Exception):
    pass


class CheckProjectName(MessageBlock):
    TITLE = "检测项目名称是否合规"
    reg = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
    project_name = '{{ cookiecutter.PROJECT_NAME }}'

    def action(self):
        result = re.match(self.reg, self.project_name)
        if not result:
            raise PreGenError(f'check {self.project_name} error')


class PipInstallRequirements(MessageBlock):
    TITLE = "安装项目 python 依赖包"
    REQUIREMENTS = {
        'DEFAULT': {
            'input': 'Y',
            'pkg': [
                'django>3,<4',
                'wrapt',
                'Pillow',
                'django-model-utils',
                'psycopg2-binary',
                'uWSGI',

            ],
        },
        'DRF': {
            'input': '{{cookiecutter.DRF}}',
            'pkg': [
                'django-filter',
                'django-extensions',
                'drf-extensions',
                'djangorestframework',
                'djangorestframework-jwt'
            ]
        },
        'GRAPPELLI': {
            'input': '{{cookiecutter.CELERY}}',
            'pkg': [
                'django-grappelli',
                'django-filebrowser',
                'feedparser'
            ]
        },
        'CELERY': {
            'input': '{{cookiecutter.CELERY}}',
            'pkg': [
                'django-celery-beat',
                'celery',
                'amqp',
            ],
        }
    }

    def action(self):
        requirements = []
        for key, item in self.REQUIREMENTS.items():
            if item['input'].strip().lower() == 'y':
                requirements += item['pkg']
                self.warning('[!] installing ...')
                error = subprocess.call(['pip', 'install'] + requirements)
                if error:
                    raise PreGenError('install pkg error')


class PipFreezeRequirements(MessageBlock):
    TITLE = "更新项目依赖到 requirements.txt 文件"

    def action(self):
        file_name = 'requirements.txt'
        with open(file_name, "w") as f:
            error = subprocess.call(["pip", "freeze"], stdout=f)
            if error:
                raise PreGenError(f'create {file_name} error')


class PreGenProjectHooks(object):
    PIPELINE = [
        'Welcome',
        'CheckProjectName',
        'PipInstallRequirements',
        'PipFreezeRequirements',
        'WellDone'
    ]

    def __call__(self):
        for cls_name in self.PIPELINE:
            try:
                eval(cls_name)()
            except PreGenError as e:
                print(e)
                break


if __name__ == '__main__':
    PreGenProjectHooks()()
