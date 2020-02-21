from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about_us(request):
    return render(request, 'about-us.html', {})

def ad_listing(request):
    return render(request, 'ad-listing.html', {})

def ad_list_view(request):
    return render(request, 'ad-list-view.html', {})


def blog(request):
    return render(request, 'blog.html', {})

def category(request):
    return render(request, 'category.html', {})

def contact_us(request):
    return render(request, 'contact-us.html', {})

def dashboad_archived_ads(request):
    return render(request, 'dashboard-archived-ads.html', {})

def dashboad_favourit_ads(request):
    return render(request, 'dashboard-favourit-ads.html', {})

def dashboad_my_ads(request):
    return render(request, 'dashboard-my-ads.html', {})

def dashboad_pending_ads(request):
    return render(request, 'dashboard-pending-ads.html', {})

def dashboad(request):
    return render(request, 'dashboard.html', {})

def login(request):
    return render(request, 'login.html', {})

def package(request):
    return render(request, 'package.html', {})

def register(request):
    return render(request, 'register.html', {})

def single_blog(request):
    return render(request, 'single-blog.html', {})

def single(request):
    return render(request, 'single.html', {})

def store(request):
    return render(request, 'store.html', {})

def terms_condition(request):
    return render(request, 'terms-condition.html', {})

def user_profile(request):
    return render(request, 'user-profile.html', {})