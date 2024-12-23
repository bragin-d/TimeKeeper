from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from calendarapp.models import Event
from .forms import WorkerEditForm, EventForm
from datetime import datetime

@login_required
def dashboard(request):
    return render(request, 'dashboard.html') 

@login_required
def home(request):
    return render(request, 'dashboard.html')

@login_required
def calendar(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

@login_required
def workers(request):
    users = CustomUser.objects.all()  # Fetch all users
    return render(request, 'workers.html', {'users': users})

@login_required
def worker_detail(request, id):
    worker = get_object_or_404(CustomUser, id=id)
    return render(request, 'worker_detail.html', {'worker': worker})

@login_required
def edit_worker(request, id):
    worker = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = WorkerEditForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_detail', id=worker.id)  # Redirect to worker details page
    else:
        form = WorkerEditForm(instance=worker)
    return render(request, 'edit_worker.html', {'form': form, 'worker': worker})

@login_required
def create_event(request, date):
    # Parse the date to a Python datetime object
    event_date = datetime.strptime(date, '%Y-%m-%d').date()
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_date = event_date
            event.created_by = request.user
            event.save()
            return redirect('calendar')  # Redirect to the calendar page after creating the event
    else:
        form = EventForm(initial={'event_date': event_date})

    return render(request, 'create_event.html', {'form': form, 'event_date': event_date})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

# Create your views here.
