from django.shortcuts import render, redirect
from .models import Incident


def home(request):

    if request.method == 'POST':

        title = request.POST.get('title', '').strip()

        description = request.POST.get('description', '').strip()

        if title and description:

            Incident.objects.create(
                title=title,
                description=description
            )

            return redirect('/incidents/')

    incidents = Incident.objects.all()

    return render(request, 'incidents/home.html', {
        'incidents': incidents
    })