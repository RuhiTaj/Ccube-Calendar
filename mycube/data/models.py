# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Competitions(models.Model):
    codingLink = models.CharField(primary_key=True, max_length=800)
    compName = models.CharField(max_length=300)
    websiteName = models.CharField(max_length=300)
    startDate = models.CharField(max_length=300)
    endDate = models.CharField(max_length=300)
    startTime = models.CharField(max_length=300)
    endTime = models.CharField(max_length=300)
    duration = models.CharField(max_length=300)

    def __str__(self):
        return self.compName + '-' + self.websiteName

#b = Users(nameOfUser = "Usha" , password = 2345 , emailId = "ushae@gmail.com" , firstName = "Usha" , lastNmae = "Sree" , profilePic ="https://i.ytimg.com/vi/6SlgpOzWuFU/maxresdefault.jpg" , birthdate = "22_12_1997" , language = "Ruby")


class Calendar(models.Model):
    year = models.CharField(max_length=5)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    date = models.CharField(default="1998-01-06", max_length=300)

    def __str__(self):
        return self.day + '-' + self.month + '-' + self.year


class Users(models.Model):
    nameOfUser = models.CharField(primary_key=True, max_length=300)
    password = models.IntegerField(default=0)
    emailId = models.CharField(max_length=300)
    firstName = models.CharField(max_length=300)
    lastNmae = models.CharField(max_length=300)
    profilePic = models.CharField(max_length=500)
    birthdate = models.CharField(max_length=12)
    language = models.CharField(max_length=300)

    def __str__(self):
        return self.firstName + ' ' + self.lastNmae

class Ratings(models.Model):
    User = models.ForeignKey(Users,primary_key=True,  on_delete=models.CASCADE)
    spoj = models.IntegerField(default=0)
    leet = models.IntegerField(default=0)
    hackerRank = models.IntegerField(default=0)
    codeChef = models.IntegerField(default=0)

    def __str__(self):
        return self.User