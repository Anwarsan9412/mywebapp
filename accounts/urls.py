from django.urls import path
from django.contrib.auth import views as auth_views
from .decorators import unauthenticated_user
from .views import UserRegisterView,AccountSetting,PasswordChangeView,LoginFormView

from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import reverse_lazy
from django.contrib import messages

urlpatterns = [
    # path('login/', unauthenticated_user(auth_views.LoginView.as_view(template_name='registration/login.html')), name='login',success_message = "Updated successfully"),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('account_setting/', AccountSetting.as_view(), name='account-setting'),
    path('password/', PasswordChangeView.as_view(),name='password_change'),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('login')),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)