from django.urls import path

from .views import SignupView, LoginViews


app_name = 'account'

urlpatterns = [
    path('sign', SignupView.as_view(), name='sign-in'),
    path('', LoginViews.as_view(), name='log-in')
]