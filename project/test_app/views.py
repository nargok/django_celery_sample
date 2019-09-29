from django.shortcuts import render
from celery.result import AsyncResult
from django_celery_results.models import TaskResult

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

def show_status(request, task_id):
  print('task_id is: ', task_id)
  
  # 10秒間はタスクが生成されないので、エラーしないためにfilterを使う
  result_object = TaskResult.objects.filter(task_id=task_id).first()
  
  result = {}
  context = {} 
  if result_object:
    print('result_object is: ', result_object)

    result = {
      'id': result_object.task_id,
      'state': result_object.status,
      'done_at': result_object.date_done
    }
  
    context = { 'result': result }
  
  # result object modelのフィールドを調べる
  q = TaskResult.objects.filter(task_id=task_id)
  print(q.values())

  return render(request, 'test_app/status_show.html', context)