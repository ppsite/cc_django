import os
import shutil


class GenericCCHooks(object):
    """
    通用 CookieCutter Hooks
    file_path_list: 定义待删除的文件路径
    dir_path_list: 定义待删除的文件夹路径
    """

    file_path_list = []
    dir_path_list = []

    def __init__(self, removable):
        self.removable = removable

    def __call__(self, *args, **kwargs):
        if self.removable.lower() == 'n':
            for dir_path in self.dir_path_list:
                if os.path.exists(dir_path):
                    shutil.rmtree(dir_path)

            for file_name in self.file_path_list:
                if os.path.exists(file_name):
                    os.remove(file_name)


class DrfCCH(GenericCCHooks):
    file_path_list = [
        'account/serializers.py',
        'account/urls.py',
        'account/utils.py',
        'account/views.py',
        'config/plugins/drf.py'
    ]
    dir_path_list = [
        'utils/drf'
    ]


class CeleryCCH(GenericCCHooks):
    file_path_list = [
        "{{cookiecutter.PROJECT_NAME}}/celery.py",
    ]


class TagCCH(GenericCCHooks):
    dir_path_list = [
        'tag'
    ]


class Boto3CCH(GenericCCHooks):
    file_path_list = [
        "config/plugins/storage.py",
    ]
    dir_path_list = [
        'media'
    ]


class MediaCCH(GenericCCHooks):
    dir_path_list = [
        'media'
    ]


if __name__ == "__main__":
    cch_classes = [
        DrfCCH('{{cookiecutter.DRF}}'),
        CeleryCCH('{{cookiecutter.CELERY}}'),
        Boto3CCH('{{cookiecutter.BOTO3}}'),
        MediaCCH('{{cookiecutter.MEDIA}}'),
        TagCCH('{{cookiecutter.TAG}}')
    ]

    for cch in cch_classes:
        cch()
