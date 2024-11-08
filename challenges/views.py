from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month, "Challenge not found.")
    return HttpResponse(challenge_text)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month = months[month - 1]
    return HttpResponseRedirect(forward_month)