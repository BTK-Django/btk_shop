from home.models import Setting
from product.models import Category

def category(request):
    return {'category': Category.objects.all()}

def setting(request):
    return {'setting': Setting.objects.all()}
# contexts_processor ile tüm sayfalarda ortak context tanımlamaları yapılıyor
# sonrasında setting.py içinde tanımlama yapmak gerekiyor