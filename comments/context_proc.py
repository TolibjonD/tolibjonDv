from .models import Comments



def comments_counter(request):
    counter = Comments.objects.all().count()
    context = {"count": counter}
    return context
