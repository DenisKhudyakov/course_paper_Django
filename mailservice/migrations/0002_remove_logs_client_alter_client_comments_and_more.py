# Generated by Django 5.0.4 on 2024-05-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailservice", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logs",
            name="client",
        ),
        migrations.AlterField(
            model_name="client",
            name="comments",
            field=models.TextField(blank=True, null=True, verbose_name="комментарий"),
        ),
        migrations.AlterField(
            model_name="message",
            name="body",
            field=models.TextField(
                blank=True, null=True, verbose_name="Текс сообщения"
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Заголовок"),
        ),
    ]
