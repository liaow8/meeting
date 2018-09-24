# Create your views here.
from common.mymako import render_mako_context
from iwork.models import WorkRecord
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    theme = request.POST.get("theme", "")
    content = request.POST.get("content", "")
    operator = "liaowei"
    if theme:
        record = WorkRecord(theme=theme, content=content, operator=operator)
        record.save()
    records = WorkRecord.objects.all()
    return render_mako_context(request, '/iwork/meeting.html', {"operator": "liaowei", "records": records})

