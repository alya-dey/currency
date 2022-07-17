from django.http import HttpResponse
from currency.models import ContactUs


def contacts_responses(request):

    contacts_responses_list = []
    for contact in ContactUs.objects.all():
        html_string = f'ID: {contact.id}, email_from: {contact.email_from}, email_to: {contact.email_to}, ' \
                      f'subject: {contact.subject}, message: {contact.subject}, created: {contact.created} <br>'
        contacts_responses_list.append(html_string)

    return HttpResponse(str(contacts_responses_list))
