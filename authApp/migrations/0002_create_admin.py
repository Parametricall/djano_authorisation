from django.db import migrations
from django.contrib.auth.models import User as DjangoUser

from authApp.models import Profile


def create_users(apps, schema_editor):
    if apps and schema_editor:
        pass

    DjangoUser.objects.create_user(username='admin', password='admin')


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
