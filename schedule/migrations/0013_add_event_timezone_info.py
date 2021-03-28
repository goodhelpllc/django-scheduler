from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("schedule", "0012_auto_20191025_1852")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="origin_timezone",
            field=models.CharField(
                verbose_name="source timezone", max_length=140, default="UTC",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="origin_isdst",
            field=models.BooleanField(
                verbose_name="source is dst active", null=True, blank=True,
            ),
        ),
    ]
