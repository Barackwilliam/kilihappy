# from django import forms
# from .models import Booking_Report

# class Booking_ReportForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['name', 'email', 'datetime', 'destination', 'message']
#         widgets = {
#             'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }

# from django import forms
# from .models import Contact_Message

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact_Message
#         fields = ['name', 'email', 'subject', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email'}),
#             'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'subject', 'placeholder': 'Subject'}),
#             'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Leave a message here', 'style': 'height: 100px'}),
#         }
