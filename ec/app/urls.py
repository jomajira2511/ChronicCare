from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm , MyPasswordResetForm

urlpatterns = [
    path("", views.home),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name= "category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(), name = 'updateAddress'),  
    path('logout/',auth_view.LogoutView.as_view(next_page='login'), name='logout'),   
    path("search/", views.search, name ="search"),
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login',auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form=LoginForm),  name='login'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)