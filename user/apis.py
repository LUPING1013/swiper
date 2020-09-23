from django.core.cache import cache
from django.http import JsonResponse

from user.logics import send_vcode
from user.models import User


def fetch_vcode(request):
    phonenum=request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送失败'})

def submit_vcode(request):
    phonenum=request.POST.get('phonenum')
    vcode=request.POST.get('vcode')
    if vcode and vcode == cache.get('Vcode-%s' % phonenum):
        try:
            user=User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user=User.objects.create(phonenum=phonenum,nickname=phonenum)

        request.session['uid'] = user.id
        return JsonResponse({'code': 0, 'data': user.to_dict()})
    else:
        return JsonResponse({'code': 1001, 'data': '验证码错误'})


def show_profile(request):
    pass
def update_profile(request):
    pass
def qn_token(request):
    pass
def qn_callback(request):
    pass
