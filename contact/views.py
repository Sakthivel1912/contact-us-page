from django.shortcuts import render,redirect
from django.core.mail import send_mail
import gspread
from .forms import ContactForm
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            
            # Get form data---------->
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            # Send email to user
            send_mail(
                subject='Thank you for contacting us',
                message=f'Thank you for contacting us, {name}! We will get back to you as soon as possible.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )
            # Write data to Google Sheet
            scope = ['https://spreadsheets.google.com/feeds',
                        'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                'contact\credentials.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open('contact_data').worksheet('Sheet1')
            row = [name, email, subject, message]
            sheet.append_row(row)
            form.save()
            return redirect('/')
    else:
        form = ContactForm()

    return render(request, 'main.html')


