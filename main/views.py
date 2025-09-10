from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app' : 'Snitch Football',
        'name': 'Vidia Qonita Ahmad',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)