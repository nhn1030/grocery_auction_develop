from django.template.response import TemplateResponse
from django.shortcuts import render

def combined_template_view(request):
    context = {
        'variable1': '값1',
        'variable2': '값2',
    }
    
    # TemplateResponse를 사용하여 두 개의 템플릿을 함께 렌더링
    response = TemplateResponse(request, ['estimate.html', 'estimate_sidebar.html'], context)
    
    return response
