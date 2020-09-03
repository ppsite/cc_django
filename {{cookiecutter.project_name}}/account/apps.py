from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = '用户管理'

    def ready(self):
        import account.signals
