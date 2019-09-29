from django.shortcuts import render
from celery.result import AsyncResult

from project.tasks import add

def celery_test(request):
  """
  APIでresultを呼べば、ステータスチェック処理を実装できる

  return例
  タスクのID, 状態、終了済か否か？
  result: 00000000-0000-0000-0000-000000000000  :  PENDING  :  False
  """

  task_id = add.delay(5, 5)

  result = AsyncResult(task_id)
  print('result:', result, ' : ', result.state, ' : ', result.ready())

  context = { 'result': result }

  return render(request, 'test_app/celery_test.html', context)