from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import UserProfile
from .models import Incident
from .forms import IncidentForm


@login_required
def home(request):
    incidents = Incident.objects.all()

    severity_filter = request.GET.get('severity')
    if severity_filter:
        incidents = incidents.filter(severity=severity_filter)

    context = {'incidents': incidents, 'current_filter': severity_filter}
    return render(request, 'incidents/home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reported_by = request.user
            incident.save()
            return redirect('incidents:home')
    else:
        form = IncidentForm()
    return render(request, 'incidents/create.html', {'form': form})


@login_required
def detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'incidents/detail.html', {'incident': incident})


@login_required
def update(request, pk):
    profile = UserProfile.objects.get(user=request.user)
    if not profile.is_admin():
        return HttpResponseForbidden('Only admins can edit incidents.')

    incident = get_object_or_404(Incident, pk=pk)

    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incidents:detail', pk=incident.pk)
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/update.html', {'form': form, 'incident': incident})


@login_required
def delete(request, pk):
    profile = UserProfile.objects.get(user=request.user)
    if not profile.is_admin():
        return HttpResponseForbidden('Only admins can delete incidents.')

    incident = get_object_or_404(Incident, pk=pk)

    if request.method == 'POST':
        incident.delete()
        return redirect('incidents:home')
    return render(request, 'incidents/confirm_delete.html', {'incident': incident})
