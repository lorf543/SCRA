import django_filters.widgets
from .models import *
from .utility import *

import django_filters

class CustomerFilters(django_filters.FilterSet):

    loan_type = django_filters.ChoiceFilter(
        choices=LOAN_TYPE,
    )
    open_state = django_filters.ChoiceFilter(
        choices=ESTADOS_UNIDOS,
    )
    acc_status = django_filters.ChoiceFilter(
        choices=ACCOUNT_STATUS,
    )
    acc_status = django_filters.ChoiceFilter(
        choices=ACCOUNT_STATUS,
    )
    method_notification = django_filters.ChoiceFilter(
        choices=METHOD_NOTIFICATION,
    )
    date_request = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    date_open_acc = django_filters.DateFromToRangeFilter(
        label = 'Open account date',
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    military_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    qualify = django_filters.BooleanFilter(
        
    )
    date_refund = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    date_mil = django_filters.DateFromToRangeFilter(
        label = 'More Info Date',
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    danial_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date',}
        )
    )
    
    
    class meta:
        model = Account
        fields = '__all__'