from home.models import Setting
from product.models import Category, Product


def category(request):
    all_categories = Category.objects.all()

    # Her bir kategori için gerekli bilgileri hesapla
    category_info = []
    for category in all_categories:
        product_count = category.products_count
        total_subcategory_products = category.products_cumulative_count

        category_info.append({
            'category': category,
            'product_count': product_count,
            'total_subcategory_products': total_subcategory_products,
        })

    context = {
        'category_info': category_info,
    }


    return {'category_info': category_info}

def setting(request):
    return {'setting': Setting.objects.all()}
# contexts_processor ile tüm sayfalarda ortak context tanımlamaları yapılıyor
# sonrasında setting.py içinde tanımlama yapmak gerekiyor