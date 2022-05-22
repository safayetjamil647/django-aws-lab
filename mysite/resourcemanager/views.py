from django.shortcuts import render



def index(request):
    return render(request, 'resourcemanager/index.html')


def ec2_index(request):
    return render(request, 'resourcemanager/ec2_index.html')
