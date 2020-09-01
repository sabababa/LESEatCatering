from django.shortcuts import render
from .forms import SimpleForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def book(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimpleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            number = form.cleaned_data.get('phone_number')
            date = form.cleaned_data.get('date')
            str_date = str(date)
            time = form.cleaned_data.get('time')
            str_time = str(time)
            notes = form.cleaned_data.get('appointment_notes')
            service = form.cleaned_data.get('Services')
            email_from = settings.EMAIL_HOST_USER
            to_email = email
            mail_subject = 'LES Eat Appointment Confirmation'
            message = render_to_string('clientemail.html', {
                'name': name,
                'number': number,
                'service': service,
                'str_date': str_date,
                'str_time': str_time,
                'notes': notes
            })
            adminMessage = render_to_string('email.html', {
                'name': name,
                'number': number,
                'service': service,
                'str_date': str_date,
                'str_time': str_time,
                'notes': notes
            })
            send_mail(mail_subject, message, email_from, [to_email], fail_silently=False)
            send_mail(mail_subject, adminMessage, email_from, [email_from], fail_silently=False)
            return render(request, 'confirmation.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimpleForm()
    return render(request, 'book.html', {'form': form})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def services(request):
    context = {}
    return render(request, 'service.html', context)

def menus(request):
    context = {}
    return render(request, 'menus.html', context)

def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)

def confirm(request):
    context = {}
    return render(request, 'confirmation.html', context)




