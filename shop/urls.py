from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('api/v1/manage_categories', ManageCategoryView.as_view()),  # show and add and delete categories
    path('api/v1/manage_products', ManageProductView.as_view()),
    # show - create - delete - update Product model objects
    path('api/v1/manage_carts', ManageCartsView.as_view()),
    path('api/v1/users_statistic', UsersStatistic.as_view()),
    path('api/v1/product_list', ProductListView.as_view()),
    path('api/v1/product_detail/<int:product_id>', ProductDetailView.as_view()),
    path('api/v1/add_to_cart', AdToCartView.as_view()),
    path('api/v1/show_cart', ShowCartView.as_view()),
    path('api/v1/delete_from_cart', DeleteFromCart.as_view()),
    path('api/v1/show_categories', CategoryListView.as_view()),
    path('api/v1/checkout', CheckoutView.as_view()),
    path('api/v1/filter/', ProductFilterView.as_view())

]
