# Generated by Django 4.2.5 on 2023-09-23 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0002_menuitem_is_item_of_the_day"),
    ]

    operations = [
        migrations.RemoveField(model_name="menuitem", name="is_item_of_the_day",),
        migrations.RemoveField(model_name="orderitem", name="unit_price",),
        migrations.AlterField(
            model_name="category", name="slug", field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name="order",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="LittleLemonAPI.order",
            ),
        ),
    ]
