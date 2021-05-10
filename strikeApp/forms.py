from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django import forms
from .models import *


class CardsForm(ModelForm):
    # regions = forms.ModelChoiceField(queryset=Regions.objects.all())
    # documents = forms.ModelMultipleChoiceField(queryset=Documents.objects.all())
    class Meta:
        model = Card

        fields = ['card_sources', 'source_url', 'source_content', 'regions',
                  'city_name', 'company', 'company_ownership_type', 'company_country',
                  'company_is_tnk_member', 'company_tnk_name', 'count_workers', 'count_strike_participants',
                  'card_demand_category', 'data_strike_end', 'has_trade_union',
                  'is_active', 'trade_union', 'phone_number_union',
                  'address_union', 'group', 'union_membership', 'first_name', 'last_name', 'gender',
                  'age', 'profession', 'employer', 'phone_number_employer', 'address_employer',
                  'duration', 'meeting_requirements', 'story', 'reasons_for_strike', 'change_number_participants',
                  'initiators_and_participants', 'state_position', 'results_so_far', 'additional_information']

        # fields = '__all__'
        widgets = {
            'card_sources': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'card_sources'}),
            'card_demand_category': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'card_demand_category'}),
            'regions': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-select'}),
            'source_url': forms.TextInput(attrs={'style': 'display: none', 'id': 'source_url'}),
            'source_content': forms.TextInput(attrs={'style': 'display: none', 'id': 'source_con'}),
            'city_name': forms.TextInput(attrs={'class': 'form-select'}),
            'company': forms.TextInput(attrs={'class': 'form-select'}),
            'company_ownership_type': forms.Select(attrs={'class': 'form-control', 'id': 'company_ownership_type'}),
            'company_country': forms.Select(
                attrs={'class': 'form-control', 'style': 'display: none', 'id': 'company_country'}),
            'company_is_tnk_member': forms.CheckboxInput(
                attrs={'class': 'form-check-label', 'style': 'display: none', 'id': 'company_is_tnk_member'}),
            'company_tnk_name': forms.TextInput(attrs={'class': 'form-select'}),
            'count_workers': forms.Select(attrs={'class': 'form-control'}),
            'count_strike_participants': forms.Select(attrs={'class': 'form-control'}),
            'data_strike_end': forms.DateTimeInput(),
            'has_trade_union': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'trade_union': forms.TextInput(attrs={'class': 'form-select'}),
            'phone_number_union': forms.TextInput(attrs={'class': 'form-select'}),
            'address_union': forms.TextInput(attrs={'class': 'form-select'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'union_membership': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-select'}),
            'last_name': forms.TextInput(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-select'}),
            'employer': forms.TextInput(attrs={'class': 'form-select'}),
            'phone_number_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'address_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'meeting_requirements': forms.Select(attrs={'class': 'form-control'}),
        }


class SourceForm(ModelForm):
    name = forms.CharField(label="Название", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(label="Активен", initial=True)

    class Meta:
        model = Source
        fields = ['name', 'is_active']


class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'
# class SourceInfoForm(ModelForm):
#     source = forms.ModelChoiceField(empty_label="Выберите источник",
#     label='Источник', queryset=Source.objects.all(), widget=forms.Select(attrs={
#         'class': 'form-control'
#     }))
#     content = forms.CharField(label='Контент', required=False, widget=forms.TextInput(attrs={'class': 'form-control',
#               'rows': 5}))
#
#     class Meta:
#         model = SourceInfo
#         fields = ['source_url', 'content', 'source']

