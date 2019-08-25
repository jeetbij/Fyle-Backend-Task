from django.conf.urls import url
from .views import GetBankView

app_name = 'bank'

urlpatterns = [
	url(r'^bank/$', GetBankView.as_view(), name='bank'),
	]