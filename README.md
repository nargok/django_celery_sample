# REDME

## 参考ドキュメント
https://dot-blog.jp/news/django-async-celery-redis-mac/

## 非同期処理の起動

### Redisの起動
```
redis-server
```

### celery beatの起動
manage.pyのあるディレクトリに移動する
```
DJANGO_SETTINGS_MODULE=project.settings celery -A project beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile /tmp/celerybeat.pid
```

### ワーカープロセスの起動
manage.pyのあるディレクトリに移動する
```
bash -c "DJANGO_SETTINGS_MODULE=project.settings celery -A project worker"
```
