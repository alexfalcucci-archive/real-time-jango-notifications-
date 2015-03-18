from notifications.models import Notification
from notifications import notify
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    notifications = request.user.notifications.unread().order_by('-timestamp')
    return render(request, 'index.html', {'notifications': notifications})


@login_required
def send_notification(request):
    recipient_username = request.POST.get('recipient_username', None)

    if recipient_username:
        recipients = User.objects.filter(username=recipient_username)
    else:
        recipients = User.objects.all()

    for recipient in recipients:
        notify.send(
            request.user,
            recipient=recipient,
            verb=request.POST.get('verb', '')
        )

    return HttpResponseRedirect(reverse('home'))


@login_required
def mark_as_read(request):
    request.user.notifications.unread().mark_all_as_read()

    return HttpResponseRedirect(reverse('home'))
