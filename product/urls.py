from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Home.as_view(),name='home'),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('pcreate/', ProductCreate.as_view(), name='product_create'),
    path('plist/', ProductList.as_view(), name='product_list'),
    path('pupdate/<int:id>/', ProductUpdate.as_view(), name='product_update'),
    path('pdelete/<int:id>/', ProductDelete.as_view(), name='product_delete'),
    path('export/', ExportProducts.as_view(), name='export'),
    path('import/', ImportProducts.as_view(), name='import'),
    path('orders/', OrderListView.as_view(), name='order_list'),  # List orders
    path('ordercreate/', OrderCreateView.as_view(), name='order_create'),  # Create order
     path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details'),  # Detail order
    path('orderupdate/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),  # Update order
    path('orderdelete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),  # D
]