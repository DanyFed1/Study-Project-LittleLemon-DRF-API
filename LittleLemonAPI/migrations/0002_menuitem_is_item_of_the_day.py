# Generated by Django 4.2.5 on 2023-09-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="is_item_of_the_day",
            field=models.BooleanField(db_index=True, default=True),
            preserve_default=False,
        ),
    ]
