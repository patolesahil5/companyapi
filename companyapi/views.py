from django.http import HttpResponse, JsonResponse

def homepage(request):
    friends=[
        'Ankit',
        'Ravi',
        'Uttam'
    ]
    return JsonResponse(friends, safe=False)