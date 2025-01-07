# Generated by Django 5.0.7 on 2024-07-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("student_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "full_name",
                    models.CharField(
                        help_text="Enter full Name", max_length=100, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Enter Email Address", max_length=100, null=True
                    ),
                ),
                ("phone_number", models.BigIntegerField()),
                (
                    "photo",
                    models.ImageField(default="image", null=True, upload_to="images/"),
                ),
                (
                    "password",
                    models.CharField(
                        help_text="Enter Password", max_length=10, null=True
                    ),
                ),
                ("reg_date", models.DateField(auto_now_add=True, null=True)),
                ("address", models.CharField(max_length=255)),
                ("otp", models.CharField(default=0, max_length=6)),
                ("otp_status", models.CharField(default="Not Verified", max_length=15)),
            ],
            options={
                "db_table": "User_Details",
            },
        ),
    ]