from django.apps import AppConfig


class DemoConfig(AppConfig):
    name = 'demo'
    verbose_name = '示例代码'

    def ready(self):
        import demo.signals
