from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import User
from converge.models import BurrConverge
from project.models import Project
from upgrade.models import ProjectUpgrade


@receiver(post_save, sender=Project)
def handler_project_post_save(sender, instance, **kwargs):
    # 创建默认项目升级规则
    created = kwargs.get('created')
    if created:
        project_upgrade = ProjectUpgrade.objects.create(project=instance, name='%s_默认升级规则' % instance.name)
        project_upgrade.users.add(*instance.users.all())
        project_upgrade.groups.add(*instance.groups.all())
        project_upgrade.save()


@receiver(post_save, sender=Project)
def handler_add_converge(sender, instance, **kwargs):
    # 创建项目默认的收敛规则
    created = kwargs.get('created')
    admin = User.objects.get(username='admin')
    if created:
        BurrConverge.objects.create(name='%s_默认收敛规则' % instance.name, duration=instance.converge_time, count=instance.converge_count,
                                    project=instance, user=admin, alert_type='.*')
