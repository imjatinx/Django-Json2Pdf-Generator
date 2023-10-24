from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from weasyprint import HTML


def home(request):
    return render(request, 'home.html')


def generate_pdf(request):
    json_data = {
        "General_Point": {
            "Font": {
                "Font_Style": "Times New Roman",
                "Font_Size": "8",
                "Font_Color": "Black",
                "Background_Color": "None",
                "Bold": "REQUIRED",
                "Italic": "REQUIRED",
                "Underline": "REQUIRED"
            },
            "Page_Layout": {
                "Page_Column": "one",
                "Margin_Top": "1.0",
                "BottomMargin": "1.0",
                "Margin_Left": "1.0",
                "Indent_Left": "1.0",
                "Indent_Right": "1.0",
                "Spacing_Before": "1.0",
                "Spacing_After": "1.0"
            }
        },
        "Technical_Point": {
            "Primary_Parameters": {
                "Total_Words": "150-200",
                "Document_Type": "Docx.file",
                "Accepted_Grammar Mistake": "0%",
                "Problem_discussed": "REQUIRED",
                "Objective": "REQUIRED",
                "Novelty": "REQUIRED",
                "Technique_Used": "REQUIRED"
            },
            "Plagiarism": {
                "Accepted_Plagiarism": "REQUIRED",
                "Plag_Tool": "REQUIRED"
            },
            "Mathematical_result": {
                "Result(Mathematical_Description)": "REQUIRED",
                "Future Scope": "REQUIRED"
            },
            "Dataset": {
                "Dataset_Description": "REQUIRED",
                "Sources": "REQUIRED",
                "Type": "REQUIRED"
            },
            "keyword": {
                "Keywords_headings": "REQUIRED",
                "No_of_Keywords": "REQUIRED"
            }
        }
    }

    context = {
        'data': json_data,
    }
    html_string = render_to_string('pdf.html', context)

    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    return response
