from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Jan activity",
    "febuary": "Feb activity",
    "march": "Mar activity",
    "april": None,
    "may": "May activity",
    "june": "June activity",
    "july": "July activity",
    "august": "Aug activity (If you have a background in programming, or if you\’re used to languages which mix programming code directly into HTML, you’ll want to bear in mind that the Django template system is not simply Python embedded into HTML. This is by design: the template system is meant to express presentation, not program logic.)",
    "september": "Sept activity",
    "october": "Oct activity",
    "november": "Nov activity",
    "december": None

}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound(f"{month.capitalize()} is not supported, Please enter a valid month")
