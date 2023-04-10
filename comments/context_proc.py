from .models import Comments
import cv2


def comments_counter(request):
    counter = Comments.objects.all().count()
    context = {"count": counter}
    return context
