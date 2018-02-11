# encoding:utf-8

from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail


def hello(request):
    return HttpResponse('Hello World')


def home(request):
    return HttpResponse("Home")


def current_time(request):
    now = datetime.datetime.now()
    c = {"current_time": now}
    # return render(request, 'current_datetime.html', c)python
    return render_to_response('current_datetime.html', c)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        return Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    c = {"hours_offset": offset, "future_time": dt}
    return render_to_response('future_time.html', c)


def display_meta(request):
    print "request.path; %s" % request.path
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % ('\n'.join(html)))


def contact(request):
    errors = []
    if request.method == 'POST':
        # valid method 1
        form = ContactForm(request.POST)
        if form.is_valid():
            # is_valid() autocall clean_message function and other clean_field functions in ContactForm
            # only after valid success, generate cleaned_data
            print('form', form.cleaned_data['subject'])
        else:
            # if valid fail, generate form.errors, return former page with form
            return render(request, 'contact_form.html', {'form': form})

        # valid method 2
        # if not request.POST.get('subject', ''):
        #     errors.append('Enter a subject.')
        # if not request.POST.get('message', ''):
        #     errors.append('Enter a messages.')
        # if request.POST.get('email', '') or '@' not in request.POST['email']:
        #     errors.append('Enter a valid email address.')

        #  from_email = form.cleaned_data['email']
        from_email = request.POST.get('email')
        if not errors:
            send_mail(
                      subject=request.POST['subject'],
                      message=u'您已向管理员发送了邮件，特此通知您，不用回复本邮件。\n\n' + request.POST['message'],
                      from_email=None,
                      recipient_list=['weijihuiall@163.com', from_email],
            )
        # return HttpResponseRedirect('/contact/thanks/')
        return HttpResponse("Send Email OK")
    form = ContactForm()
    # form = form.as_p()
    form.as_ul()
    return render(request, 'contact_form.html', {'form': form})


# Named Groups, positional args
def ng_special_case_2003(request):
    return HttpResponse('ng_special_case_2003')


def ng_month_archive(request):
    # could't to get year arg
    return HttpResponse('ng_month_archive')


def ng_day_archive(request, year, month, day):
    return HttpResponse('ng_day_archive:%s-%s-%s' % (year, month, day))


def ng_page(request, num="1"):
    return HttpResponse('ng_page:%s' % num)



