from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Jan activity",
    "febuary": "Feb activity",
    "march": "Mar activity",
    "april": "Apr activity",
    "may": "May activity",
    "june": "June activity",
    "july": "July activity",
    "august": "Aug activity",
    "september": "Sept activity",
    "october": "Oct activity",
    "november": "Nov activity",
    "december": "Dec activity"

}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_number(reuest, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month not found")
    else:
        redirected_month = months[month - 1]
        redirected_path = reverse("month_challenge", args=[redirected_month])
        return HttpResponseRedirect(redirect_to=redirected_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"{month.capitalize()} is not supported, Please enter a valid month")
