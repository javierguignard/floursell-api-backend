from django.shortcuts import render

def test_reder_template(request):
    return render(request, 'base.html')