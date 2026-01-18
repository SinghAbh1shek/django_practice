from django.shortcuts import render
from core.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult

# Enque tasks using delay()
# def home(request):
#     result1 = add.delay(5, 6)
#     print("Result1: ", result1)
#     result2 = sub.delay(50, 6)
#     print("Result2: ", result2)
#     return render(request, 'home.html')

# # Enque tasks using apply_async()
# def home(request):
#     result1 = add.apply_async(args=[10, 15])
#     print("Result1: ", result1)
#     result2 = sub.apply_async(args=[50, 40])
#     print("Result2: ", result2)
#     return render(request, 'home.html')

def home(request):
    result = add.delay(50, 60)
    return render(request, 'home.html', {'result': result})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def check_result(request, task_id):
    result = AsyncResult(task_id)
    print('Ready: ', result.ready())
    print('Successful: ', result.successful())
    print('Failed: ', result.failed())
    return render(request, 'result.html', {'result': result})