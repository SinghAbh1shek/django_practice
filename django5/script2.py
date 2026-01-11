from django.template.loader import get_template
from django.conf import settings
import pdfkit
from orders.models import *

def generate_order_pdf(instance, data):
    dynamic_directory_name = f"media/pdfs/{instance.order_id}.pdf"
    template_name = 'pdfs/invoice'

    options = {
        'no-outline': None,
        'page-size': 'A4',
        'margin-top': '0.2in',
        'margin-bottom': '0.2in',
        'margin-left': '0.2in',
        'margin-right': '0.2in',
    }

    path_whtmltopdf = '/usr/local/bin/wkhtmltopdf'

    template = get_template(f"{template_name}.html")
    content = template.render(data)
    exact_filepath = f"{settings.BASE_DIR}/{dynamic_directory_name}"
    config = pdfkit.configuration(wkhtmltopdf = path_whtmltopdf)
    pdfkit.from_string(content, exact_filepath, options=options, configuration=config)
    

order = Order.objects.last()

generate_order_pdf(order, order.get_order_data())