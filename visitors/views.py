from django.shortcuts import render
from .models import VisitorsInformation
import pygame
import pygame.camera
from django.views.decorators.csrf import csrf_exempt


def visitor_ip_address(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


# Create your views here.
@csrf_exempt
def record_visitors(request):
    mobile = request.user_agent.is_mobile
    tablet = request.user_agent.is_tablet
    touch_capable = request.user_agent.is_touch_capable
    pc = request.user_agent.is_pc
    bot = request.user_agent.is_bot
    # find device name by bool and get device information
    if mobile:
        device = "Mobile"
    if tablet:
        device = "Tablet"
    if touch_capable:
        device = "Touchpad capable"
    if pc:
        device = "PC"
    if bot:
        device = "BOT"

    browser = f"{request.user_agent.browser.family} , version: {request.user_agent.browser.version_string}"
    os_info = f"{request.user_agent.os.family} , version: {request.user_agent.os.version_string}"
    device_pr = request.user_agent.device.family

    # get device location
    ip = visitor_ip_address(request)
    check_ip = VisitorsInformation.objects.all().filter(ip=ip)
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0])
        cam.start()
        image = cam.get_image()

        # saving the image
        pygame.image.save(image, f"media/visitors/user-{ip}.jpg")

    # if camera is not detected the moving to else part
    else:
        print("No camera on current device")

    if check_ip:
        # do something
        msg = "user exists"
    else:
        visitor = VisitorsInformation.objects.create(
            device=device,
            browser=browser,
            os_info=os_info,
            device_pr=device_pr,
            ip=ip,
            image=f"visitors/user-{ip}.jpg",
        )
        visitor.save()


def all_visitors(request):
    visitors_list = VisitorsInformation.objects.all().order_by("-created_at")
    return render(request, "visitors/visitors-list.html", {"visitors": visitors_list})
