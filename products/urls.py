from django.urls import path
from .views import ProductList, ProductDetail, CategoryList

from .views import precio_final

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('categories/', CategoryList.as_view()),
]

# AGREGAR esto en products/urls.py, junto a tus rutas existentes
# (debajo del router.register(...) o de tu lista urlpatterns actual)

urlpatterns += [
    path('products/<int:pk>/precio-final/', precio_final),
]

# ============================================================
# IMPORTANTE sobre la URL final:
# El documento de la tarea prueba esto en /api/v1/products/<id>/precio-final/
# PERO en nuestro proyecto (desde la Práctica 2) usamos el prefijo 'api/'
# (sin v1) en tienda_online/urls.py, para que coincidiera con lo que esa
# práctica pedía.
#
# Si NO cambiaste ese prefijo después, tu endpoint real va a quedar en:
#   http://127.0.0.1:8000/api/products/<id>/precio-final/
#
# Si en cambio en alguna práctica posterior SÍ cambiaste tienda_online/urls.py
# para usar 'api/v1/', entonces sí sería con /api/v1/.
# Revisa tu tienda_online/urls.py y usa el prefijo que realmente tengas ahí.
# ============================================================