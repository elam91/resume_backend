from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="Elam Buteil - Full-stack Developer - {timezone.now().date().strftime("%B %d, %Y")}.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response

    )
    if pisa_status.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return response
