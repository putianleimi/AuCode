from django.shortcuts import render, get_object_or_404


from .models import AuCode


def index(request):

    return render(request, 'querycode/index.html')


def detail(request):
    # ac = get_object_or_404(AuCode, code=request.GET.get('name'))
    ac = request.GET.get('name')
    error_msg = ''
    if not ac:
        error_msg = "You didn't input anything, try again!"
        return render(request, 'querycode/detail.html', {
            'error_msg': error_msg,
        })
    aucode = AuCode.objects.filter(code=ac)

    if not aucode:
        error_msg = "Don't match any report,please note the case"
        return render(request, 'querycode/detail.html', {
            'error_msg': error_msg,

        })


    return render(request, 'querycode/detail.html', {
        'aucode': aucode,


    })
