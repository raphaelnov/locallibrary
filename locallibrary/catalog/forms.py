
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import BookInstance
import datetime




class RenewBookForm(forms.Form):
    renew_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(week=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data



# class RenewBookModelForm(ModelForm):
#     def clean_due_back(self):
#         data = self.clean_due_back['due_back']
#
#         # Check if it is not in the past
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         # Check date is in range librarian allowed to change (+4 weeks)
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         return data
#
#     class Meta:
#         model = BookInstance
#         fields=['due_back']
#         labels={'due_back': _('Renewal date'),}
#         help_text={'due_back': _('Enter a date between now and 4 weeks (default 3).'),}
