from django.db import migrations
from django.contrib.auth.models import User as DjangoUser

from authApp.models import User


def create_users(apps, schema_editor):
    if apps and schema_editor:
        pass

    User.objects.create_user(
        username='admin',
        email="admin@example.com",
        password='admin'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
