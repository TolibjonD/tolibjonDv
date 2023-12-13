from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Comments, Posts, PostComments
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import PostForm, PostCommentsForm
from django.conf import settings

# Create your views here.


class HomePageView(View):
    def get(self, request):
        posts = Posts.objects.all().order_by("-created_at")[:10]
        count = Comments.objects.all().count()
        return render(request, "index.html", {"posts": posts, "count": count})

    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        if name and email and message:
            try:
                validate_email(email)
            except ValidationError as e:
                messages.warning(request, f"Janob {name} Xato email kiritildi !...")
            else:
                message_inctance = Comments.objects.create(
                    name=name,
                    email=email,
                    message=message,
                )
                message_inctance.save()
                messages.success(
                    request,
                    f"Janob {message_inctance.name} ma'lumotlaringiz muvaffaqiyatli yuborildi.",
                )

            return redirect("home")
        else:
            messages.warning(
                request,
                f"Janob {name} Ma'lumotlar tashlab ketilgan. Hamma maydonlarni to'ldirilishingiz lozim !...",
            )
            return render(request, "index.html")


class MessagesPage(View):
    def get(self, request):
        messages = Comments.objects.all().order_by("-date_send")
        del_id = request.GET.get("delete")
        if del_id:
            msg = Comments.objects.get(id=del_id)
            msg.delete()
            return redirect("messages")
        count = Comments.objects.all().count()
        return render(request, "messages.html", {"messages": messages, "count": count})


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "create.html", {"form": form})

    def post(self, request):
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(
            #     request,
            #     "Siz yangi postni yaratdingiz !.. Postlar joylab borishda davom eting !...",
            # )
            return redirect("home")
        else:
            return render(request, "create.html", {"form": form})


class PostDetailView(View):
    def get(self, request, slug):
        post = Posts.objects.get(slug=slug)
        dele = request.GET.get("remove")
        if dele:
            post = Posts.objects.get(slug=dele)
            post.delete()
            return redirect("home")
        review_id = request.GET.get("review_id")
        if review_id:
            review = PostComments.objects.get(id=int(review_id))
            review.delete()
            return redirect(reverse("detail", args=[post.slug]))
        form = PostForm(instance=post)
        comment_form = PostCommentsForm()
        reviews = PostComments.objects.all().filter(post=post).order_by("-created_at")
        context = {
            "post": post,
            "form": form,
            "comment_form": comment_form,
            "reviews": reviews,
        }
        return render(request, "detail.html", context)

    def post(self, request, slug):
        comment_form = PostCommentsForm()
        post = Posts.objects.get(slug=slug)
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        comment_form = PostCommentsForm(data=request.POST, files=request.FILES)
        context = {
            "post": post,
            "form": form,
            "comment_form": comment_form,
        }
        if request.method == "POST":
            if "fikringiz" in request.POST:
                print(request.POST.get("ismingiz"))
                if comment_form.is_valid():
                    print(comment_form.cleaned_data["ismingiz"])
                    review = PostComments.objects.create(
                        ismingiz=comment_form.cleaned_data["ismingiz"],
                        fikringiz=comment_form.cleaned_data["fikringiz"],
                        post=post,
                    )
                    review.save()
                    messages.success(
                        request, "Muvaffaqiyatli ravishda izoh qoldirdigiz !..."
                    )
                    return redirect(reverse("detail", args=[post.slug]))
                else:
                    messages.warning(
                        request,
                        "Xatolik yuz berdi izoh qoldirish tugmasini bosib qaytadan urinib ko'ring !...",
                    )
                    return render(request, "detail.html", context)

            if form.is_valid():
                form.save()
                messages.success(
                    request, "Muvaffaqiyatli ravishda postni tahrirladingiz !..."
                )
                return redirect(reverse("detail", args=[post.slug]))
            else:
                messages.success(
                    request, "Xatolik yuz berdi formani ochib ko'ring !..."
                )
                return render(request, "detail.html", context)
