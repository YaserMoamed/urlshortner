
from django.shortcuts import redirect, render
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner


# Create your views here.
def home(token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url, )


def make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            a = shortner().issue_token()
            new_url.short_url = a
            print(a)
            new_url.save()
        else:
            form = UrlForm()
            a = "Invalid Url"
    return render(request, 'home.html', {'form': form, 'a': a})
