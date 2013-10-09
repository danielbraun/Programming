import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .utils import bubble_sort, num
from .forms import SortingForm


@login_required
def index(request):
        return render(request, "ex2/index.html", {
            'form': SortingForm()
        })


@login_required
def sort_view(request):
    result = []
    try:
        result = bubble_sort(
            [num(i) for i in request.POST['input'].split(',')]
        )
    except ValueError:
        pass
    return HttpResponse(json.dumps({'result': result}),
                        content_type="application/json")
