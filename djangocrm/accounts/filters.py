import django_filters
from django_filters import DateFilter

from .models import  *


class formFilters(django_filters.FilterSet):




	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']