from django.shortcuts import render
from .models import Award


def award_list(request):
    awards  = Award.objects.all()
    context = {
        'award_list': awards
    }
    return render(request, 'awards/award_list.html', context)
