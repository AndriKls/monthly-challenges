from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django every day for at least 20 minutes!",
    "april": "Read for 30 minutes every day!",
    "may": "Meditate for 10 minutes every day!",
    "june": "Drink 8 glasses of water every day!",
    "july": "Try a new workout routine twice a week!",
    "august": "Journal every day for at least 10 minutes!",
    "september": "Cook a new recipe once a week!",
    "october": "Reduce screen time to 2 hours a day!",
    "november": "Practice gratitude by writing 3 things you're thankful for daily!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge(request, month):
    try:
        challenge_text =  monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month = months[month - 1]
    return HttpResponseRedirect(forward_month)