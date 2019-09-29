from .celery import app as celery_app

# Django起動時にcelery.pyからappをインポートしてロードする
__all__ = ('celery_app',)
