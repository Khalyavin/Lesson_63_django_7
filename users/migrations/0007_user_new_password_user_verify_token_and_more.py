# Generated by Django 4.1.7 on 2023-03-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="new_password",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="новый пароль"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="verify_token",
            field=models.CharField(
                blank=True, max_length=35, null=True, verbose_name="Токен верификации"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="verify_token_expired",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата истечения токена"
            ),
        ),
    ]
