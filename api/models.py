# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField
from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'


class Note(Model):
    title = CharField(max_length=150)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now_add=True, blank=True)
    user = ForeignKey(to=User, on_delete=CASCADE)
