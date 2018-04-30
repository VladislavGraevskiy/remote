from datetime import timedelta

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render_to_response, render, redirect
# import requests
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from remote_control.decorators import check_authorization
from remote_control.forms.user import UserprofileForm, LoginUser
from remote_control.fusioncharts import FusionCharts
from remote_control.models.models import Commands, TelemetryFilter, Telemetry, Request, Schedule
from remote_control.models.user import Userprofile
from third_party.bsu_ground.api import send_command_to_api
from third_party.bsu_ground.utils import forming_command_data
from .forms.commands import Modes, CommandsForm, ScheduleForm


def test_ground():
    # response = requests.get('http://0.0.0.0:8001/test_for_remote/').json()
    return JsonResponse('')


@check_authorization
def send_command(request):
    if request.POST:
        form = CommandsForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data.get('command')

            user_id = request.user.id
            command = Commands.objects.get(command=command)
            device = form.cleaned_data.get('device')
            argument = form.cleaned_data.get('argument')
            send_data = forming_command_data(command.command, argument, device)
            request_command = Request.objects.create(
                user_id=user_id,
                command_id=command.id,
                device=device,
                argument=argument
            )
            response_json = send_command_to_api(send_data)
            request_command.cid = response_json.get('cid')
            request_command.save()
        else:
            pass
    info_list = Request.objects.filter(user=request.user).order_by('-send_datetime')
    paginator = Paginator(info_list, 6)
    page = request.GET.get('page')
    info = paginator.get_page(page)

    user_id = request.user.id
    trust_level = Userprofile.objects.get(id=user_id).trust_level
    form = CommandsForm(trust_level=trust_level)

    return render(
        request,
        'send_command.html',
        {
            'form': form,
            'info': info,
        }
    )


def main_page(request):
    return render(
        request,
        'main_page.html',
    )


@check_authorization
def sensors(request):

    f = TelemetryFilter(request.GET, queryset=Telemetry.objects.all())

    # column2d = FusionCharts("column2d", "ex1", "684", "476", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            # )

    return render(request, 'sensors.html',
                  {
                      'filter': f,
                      # 'output': column2d.render()
                  })


def login_user(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/sensors', request)
            else:
                pass
    else:
        form = LoginUser()
    return render(
        request,
        'login.html',
        {'form': form},
    )


def logout_user(request):
    logout(request)
    return redirect('/', request)


def registration(request):
    if request.method == 'POST':
        userprofile = UserprofileForm(request.POST)
        if userprofile.is_valid():
            userprofile.save()
            username = userprofile.cleaned_data.get('username')
            raw_password = userprofile.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('/', request)
    else:
        userprofile = UserprofileForm()

    return render(
            request,
            'registration.html',
            {'userprofile': userprofile},
        )


def personal_account(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user_id = request.user.id
            schedule.end_datetime = form.cleaned_data.get('start_datetime')
            # form.end_datetime = form.start_datetime + timedelta(minutes=29, seconds=59)
            form.save()
        else:
            print(form.errors)
    s = Schedule.objects.all()
    print(s)
    form = ScheduleForm()
    return render(
        request,
        'personal_account.html',
        {'form': form,
         's': s
         },

    )
