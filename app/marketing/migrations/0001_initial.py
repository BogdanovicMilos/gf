# Generated by Django 3.2.9 on 2021-11-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("full_name", models.CharField(max_length=254)),
                ("phone_number", models.CharField(max_length=30)),
                ("email_address", models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ("website", models.URLField(blank=True)),
                (
                    "monthly_ad_budget",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("less_than_10_thousand", "Less than $10,000/month"),
                            ("between_10_and_25_thousand", "$10,000-$25,000/month"),
                            ("between_25_and_50_thousand", "$25,001-$50,000/month"),
                            ("between_50_and_100_thousand", "$50,001-$100,000/month"),
                            ("more_than_100_thousand", "$100,000+/month"),
                        ],
                        max_length=30,
                    ),
                ),
                ("message", models.TextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
