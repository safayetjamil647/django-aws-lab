from django.shortcuts import render
import boto3
import mimetypes
import os
from django.http.response import HttpResponse


def index(request):
    return render(request, 'resourcemanager/index.html')


def ec2_index(request):
    return render(request, 'resourcemanager/ec2_index.html')


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'ec2-keypair.pem'
    # Define the full file path
    filepath = BASE_DIR + '/filedownload/Files/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


def launch_instances(self):
    # create a new EC2 instance
    ec2 = boto3.resource('ec2', region_name="us-east-1")
    instances = ec2.create_instances(
        ImageId='ami-0b0ea68c435eb488d',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='ec2-keypair'
    )
    return launch_instances()


def get_running_instances(self):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
    return get_running_instances(self)


def linux_index(request):
    return render(request, 'resourcemanager/linux_index.html')


def aws_playground(request):
    return render(request, 'resourcemanager/aws_playground.html')
