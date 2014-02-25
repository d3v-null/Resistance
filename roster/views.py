from django.shortcuts import render
from django.http import HttpResponse
from roster.models import Occupation, Member, MemberOccupation

# Create your views here.
def index(request):
    output = '<h1>Roster</h1>'
    occupation_list = Occupation.objects.all()
    # output += str(len(occupation_list))
    for occupation in occupation_list:
        output += '<h2>' + occupation.name + '</h2>'
        output += '<ul>'
        memberoccupation_list = MemberOccupation.objects.filter(occupation = occupation.id)
        for memberoccupation in memberoccupation_list:
            output += '<li>' + memberoccupation.member.name + '</li>'
        output += '</ul>'
    return HttpResponse(output)
    