from home.models import Setting
from product.models import Category


def category(request):
    return {'category': Category.objects.all()}


def setting(request):
    return {'setting': Setting.objects.all()}
