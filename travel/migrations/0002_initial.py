# Generated by Django 4.1.1 on 2023-03-02 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("travel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="tour_guide",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.tourguidemodel"
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="traveler",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.travelermodel"
            ),
        ),
    ]