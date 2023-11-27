from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challengs={
 "january": "ocak",
 "february": "Şubat",
 "march": "Mart"

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challengs.keys())

    for month  in months:
        capitalized_month = month.capitalize()
        list_items += f"<li><a href="">{capitalized_month}</a></li>"
        month_path = reverse("month_challenge", args=[month])
    response_data = """"
    <ul> 
        <li><a href="/challengs/january">January</a></li>
    </ul>
 """
    return HttpResponse()

def monthly_challengs_by_number(request, month):
    months = list(monthly_challengs.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
     
    return HttpResponseRedirect(redirect_path)

def monthly_challengs(request, month):
     try:
       challengs_text == monthly_challengs[month]
       response_data = f"<h1>{response_data}</h1>"
     except:
         return HttpResponseNotFound("Not found")
     return HttpResponse(challengs_text)
   