from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class UserManager(models.Manager):
    #Check name
    def nm_validate(self, name):
        if len(name) > 1:
            return True
        else:
            return False
    #Check alias
    def alias_validate(self, alias):
        if len(alias) > 1:
            return True
        else:
            return False
    #Check email length
    def email_validate(self, email):
        if not EMAIL_REGEX.match(email):
            return False
        else:
            return True
    #Check if email already exists
    def email_exists(self, email):
        check = User.objects.filter(email = email).exists()
        if check:
            return False
        else:
            return True
    #Check password
    def password_validate(self, password):
        if len(password) > 8:
            return True
        else:
            return False
    #Check password
    def password_match(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False
    #Create User
    def createUser(self, name, alias, email, password):
        user = self.create(name = name, alias = alias, email = email, password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
        return user
    #Check if passwords match
    def passwordsMatchCheck(self, entered_pw, db_pw):
        if bcrypt.hashpw(entered_pw.encode(), db_pw.encode()) != db_pw:
            return False
        else:
            return True

class User(models.Model):
    name = models.TextField(max_length = 50)
    alias = models.TextField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
