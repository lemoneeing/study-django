from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'mail/index.html')

def send_mail(request):
    if request.method == 'POST':
        to = request.POST.get('email')
        title = request.POST['title']
        msg = request.POST['message']

        context = {'to': to, 'title': title, 'message': msg}

        mail_html = render_to_string('mail/mail_form.html', context)

        mail = EmailMessage(subject=title, body=mail_html, to=[to])
        mail.content_subtype = 'html'
        mail.send()

    return HttpResponseRedirect(reverse('mail:end'))

def mail_end(request):
    return render(request, 'mail/mail_sent.html')
