# Generated by Django 5.0.7 on 2024-07-27 09:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0002_userdetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="FineRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fine_image", models.ImageField(upload_to="fine_images/")),
                ("fine_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("issued_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("user_response", models.CharField(default="Pending", max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fines",
                        to="adminapp.userdetails",
                    ),
                ),
            ],
        ),
    ]