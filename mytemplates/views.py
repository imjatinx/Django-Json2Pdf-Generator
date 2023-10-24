from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .models import PreviewTemplate
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML


def home(request):
    templates = PreviewTemplate.objects.all()
    return render(request, 'home.html', {'templates': templates})


def generate_pdf(request):
    if request.method == 'POST':
        templatePath = request.POST.get('template')
        if templatePath is not None:
            json_data = {
                "Technical_Point": {
                    "keyword": {
                        "Keywords_headings": "REQUIRED",
                        "No_of_Keywords": "REQUIRED"
                    }
                }
            }

            context = {
                'data': json_data,
            }
            html_string = render_to_string(templatePath, context)

            pdf = HTML(string=html_string).write_pdf()

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
            return response
    
    return HttpResponse('Invalid Request')
