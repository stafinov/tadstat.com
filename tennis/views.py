from django.shortcuts import render, redirect
from .models import Statistic
from .forms import StatisticForm
from django.views.generic import DetailView


def tennis_home(request):
    tennis = Statistic.objects.order_by('-date')
    return render(request, 'tennis/tennis_home.html', {'tennis': tennis})

class tennisDetailView(DetailView):
    model = Statistic
    template_name = 'tennis/details_view.html'
    context_object_name = 'statistic'




def create(request):
    error = ''
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StatisticForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tennis/create.html', data)
