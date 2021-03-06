# Generated by Django 3.1.2 on 2020-10-24 14:30

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="A unique identification name for the client.",
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "token_ttl",
                    models.DurationField(
                        default=datetime.timedelta(days=1),
                        help_text="\n            Token Time To Live (TTL) in timedelta. Format: <em>DAYS HH:MM:SS</em>.\n            ",
                        verbose_name="Token Time To Live (TTL)",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuthToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        db_index=True,
                        help_text="Token is auto-generated on save.",
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expiry", models.DateTimeField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_token_set",
                        to="durin.client",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_token_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="authtoken",
            constraint=models.UniqueConstraint(
                fields=("user", "client"), name="unique token for user per client"
            ),
        ),
    ]
