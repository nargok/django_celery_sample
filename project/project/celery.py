from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# settings.pyをデフォルト設定として使用する
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# すべてのCelery関係の設定に接頭辞CELERYを設定する
app.config_from_object('django.conf:settings', namespace='CELERY')

# Djangoに登録しているすべてのタスクモジュールをロードする
app.autodiscover_tasks()
