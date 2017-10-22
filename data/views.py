# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader

from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from .models import Competitions
from .models import Calendar
from .models import Users
from .models import Ratings


def index(request):
    all_dates = Calendar.objects.all()
    all_users = Users.objects.all()
    all_ratings = Ratings.objects.all()
    all_competitions = Competitions.objects.all()
    template = loader.get_template('calendardata/index.html')
    context_data = {
        'all_dates': all_dates,
        'all_users': all_users,
        'all_ratings': all_ratings,
        'all_competitions': all_competitions
    }
    return HttpResponse(template.render(context_data, request))
    # html = ''
    # url = ''
    # for the_date in alldates:
    #     url = '/data/' + str(the_date.year) + str(the_date.month) + str(the_date.day) + '/'
    #     html += "Go to the competitions on: " + '<a href="' + url + '">' + the_date.day + "-" + the_date.month + "-" + the_date.year + '</a><br>'
    #
    # return HttpResponse(html)


def detail(request, date):
    all_competitions = Competitions.objects.all()
    p = 0
    for the_competition in all_competitions:
        time = date[0:4]+'-'+date[4:6]+'-'+date[6:8]
        html = 'Ruhi'  +'-----' + time +'-----' + the_competition.startDate
        if time >= the_competition.startDate:
            if time <= the_competition.endDate:
                html += the_competition.websiteName +  "  :  Go to the competition on: " + '<a href="' + the_competition.codingLink + '">' + the_competition.compName  + '</a><br>'
                #html += date
                p = p+1
            elif time == the_competition.startDate:
                #html += date
                p = p+1
                html += the_competition.websiteName +  "  :  Go to the competition on: " + '<a href="' + the_competition.codingLink + '">' + the_competition.compName  + '</a><br>'
        return HttpResponse(html)
    if p == 0:
        html = "Oops!"
        return HttpResponse(html)




# Create your views here.
#
#
# n = 7305
#
# dayno=1
# monthno=1
# yearnoo=2004
#
# for i in range(0, n):
#     if dayno>9 :
#         d = str(dayno)
#     else :
#         d = '0'+ str(dayno)
#     if monthno>9 :
#         m = str(monthno)
#     else :
#         m = '0' + str(monthno)
#     y = str(yearnoo)
#     b = Calendar()
#     b.year = y
#     b.month = m
#     b.day = d
#     b.date = y + '-' + m + '-' + d
#     b.save()
#
#     #year = int(input("Input a year: "))
#
#     if yearnoo % 400 == 0 :
#         leap_year = True
#     elif yearnoo % 100 == 0:
#         leap_year = False
#     elif yearnoo % 4 == 0 :
#         leap_year = True
#     else:
#         leap_year = False
#
#
#     if monthno in (1, 3, 5, 7, 8, 10, 12):
#         month_length = 31
#     elif monthno == 2:
#         if leap_year:
#             month_length = 29
#         else:
#             month_length = 28
#     else:
#         month_length = 30
#
#     if dayno < month_length:
#         dayno += 1
#     else:
#         dayno = 1
#         if monthno == 12:
#             monthno = 1
#             yearnoo += 1
#         else:
#             monthno += 1
#
# i=86
# h = 9
# g = 2017
#
# while i<=87:
#     c = Competitions()
#
#     if i < 10:
#         f = "0" + str(i)
#     else :
#         f = str(i)
#
#     if h == 1:
#         moni = "January-Cook-Off"
#     elif h ==2 :
#         moni = "February-Cook-Off"
#     elif h==3 :
#         moni = "March-Cook-Off"
#     elif h==4 :
#         moni = "April-Cook-Off"
#     elif h==5 :
#         moni = "May-Cook-Off"
#     elif h ==6 :
#         moni = "June-Cook-Off"
#     elif h==7:
#         moni = "July-Cook-Off"
#     elif h==8:
#         moni = "August-Cook-Off"
#     elif h==9:
#         moni = "September-Cook-Off"
#     elif h==10 :
#         moni = "October-Cook-Off"
#     elif h==11 :
#         moni = "November-Cook-Off"
#     elif h==12 :
#         moni = "December-Cook-Off"
#
#     if h<10 :
#         kl = "0" + str(h)
#     else:
#         kl = str(h)
#
#     c.codingLink = "https://www.codechef.com/COOK" + f
#     c.websiteName = "CodeChef"
#     c.compName = moni + "-" + str(g)
#     c.startDate = str(g) + "-" + kl + "-" + "22"
#     c.endDate = str(g) + "-" + kl + "-" + "23"
#     c.startTime = "09:30 PM"
#     c.endTime = "00:00 AM"
#     c.duration = "2 hours 30 minutes"
#     c.save()
#
#     if h<12:
#         h = h+1
#     elif h==12:
#         h=1
#
#     if h==1:
#         g = g+1
#     i= i+1
#
#





   # print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
#
# i = 2
#
# y = 2016
# d = 28
# m = 8
#
# while i<52 :
#
#     de = str(y) + "-"
#     if(m<10):
#         de = de + "0"
#     de = de + str(m) + "-"
#     if(d<10):
#         de = de + "0"
#     de = de + str(d)
#
#
#     a = Competitions()
#     a.codingLink = "https://leetcode.com/contest/leetcode-weekly-contest-" + str(i)
#     a.websiteName = "LeetCode"
#     a.compName = "LeetCode Weekly Contest " + str(i)
#     a.startTime = "07:00 PM"
#     a.endTime = "08:30 PM"
#     a.duration = "1 hour 30 minutes"
#     a.startDate = de
#     a.endDate = de
#     a.save()
#
#     k = 1
#
#     if d<21 :
#         d = d+7
#     else:
#         d = 1
#         k = 2
#
#     if k==2 :
#         if m==12:
#             m = 1
#         else :
#             m = m+1
#     if m == 1:
#         if d == 1:
#             y = y+1
#
#     i=i+1
#
#
# y = 9
# m = 3
#
# i = 0
#
# while i<110:
#     if m==3:
#         mon = "MARCH"
#     elif m==1:
#         mon = "JAN"
#     elif m==2:
#         mon = "FEB"
#     elif m==4:
#         mon = "APRIL"
#     elif m==5:
#         mon = "MAY"
#     elif m==6:
#         mon = "JUN"
#     elif m==7:
#         mon = "JULY"
#     elif m==8:
#         mon = "AUG"
#     elif m==9:
#         mon = "SEP"
#     elif m==10:
#         mon = "OCT"
#     elif m==11:
#         mon = "NOV"
#     elif m==12:
#         mon = "DEC"
#
#     r = Competitions()
#     if y==9 :
#         l = "09"
#     else:
#         l = str(y)
#     if m<10:
#         f = "0" + str(m)
#     else :
#         f = str(m)
#
#     r.codingLink = "https://www.codechef.com/" + mon + l
#     r.compName = mon + " - " + "Long Challenge" + "20" + l
#     r.websiteName = "CodeChef"
#     r.startDate = "20" + l + "-" + f + "-" + "04"
#     r.endDate = "20" + l + "-" + f + "-" + "14"
#     r.startTime = "03:30 PM"
#     r.endTime = "03:30 PM"
#     r.duration = "10 days"
#     r.save()
#
#     if m==12:
#         m = 1
#     else:
#         m = m + 1
#
#     if m==1:
#         y = y+1
#
#     i = i+1



