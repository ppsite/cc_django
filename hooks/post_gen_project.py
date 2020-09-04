import os
import shutil


class GenericCCHooks(object):
    file_path_list = []
    dir_path_list = []

    def __init__(self, removable):
        self.removable = removable

    def remove(self):
        if self.removable.lower() == 'n':
            for dir_path in self.dir_path_list:
                if os.path.exists(dir_path):
                    shutil.rmtree(dir_path)
            for file_name in self.file_path_list:
                if os.path.exists(file_name):
                    os.remove(file_name)


class GrappelliCCH(GenericCCHooks):
    dir_path_list = ["config/common/grappelli/"]
    file_path_list = [os.path.join('config/common/', 'filebrowser.py')]


class DrfCCH(GenericCCHooks):
    file_path_list = [os.path.join('config/common/', 'drf.py')]


class CeleryCCH(GenericCCHooks):
    file_path_list = [
        os.path.join("{{cookiecutter.project_name}}", "celery.py"),
        os.path.join("config/common/", "celery.py"),
    ]


class MDEditorCCH(GenericCCHooks):
    file_path_list = [os.path.join('config/common/', 'mdeditor.py')]


class AccountCCH(GenericCCHooks):
    dir_path_list = ["account"]


class DemoCCH(GrappelliCCH):
    dir_path_list = ["demo"]


if __name__ == "__main__":
    cch_classes = [
        GrappelliCCH('{{cookiecutter.use_grappelli}}'),
        DrfCCH('{{cookiecutter.use_drf}}'),
        CeleryCCH('{{cookiecutter.use_celery}}'),
        AccountCCH('{{cookiecutter.use_account}}'),
        DemoCCH('{{cookiecutter.use_demo}}'),
        MDEditorCCH('{{cookiecutter.use_mdeditor}}'),
    ]

    for cch in cch_classes:
        cch.remove()
