# Generated by Django 5.0.6 on 2024-07-07 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(help_text='Уникальный идентификатор пользователя в Telegram.', unique=True, verbose_name='ID пользователя')),
                ('username', models.CharField(blank=True, help_text='Имя пользователя в Telegram.', max_length=120, null=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, help_text='Имя пользователя в Telegram.', max_length=120, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Фамилия пользователя в Telegram.', max_length=120, null=True, verbose_name='Фамилия')),
                ('language_code', models.CharField(blank=True, help_text='Код языка, используемый пользователем в Telegram.', max_length=10, null=True, verbose_name='Код языка')),
                ('is_bot', models.BooleanField(default=False, help_text='Указывает, является ли пользователь ботом.', verbose_name='Бот')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Временная метка, указывающая, когда был создан пользователь.', verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Пользователь Telegram',
                'verbose_name_plural': 'Пользователи Telegram',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст заметки.', verbose_name='Текст заметки')),
                ('order', models.IntegerField(default=0, help_text='Порядок сортировки заметок пользователя.', verbose_name='Порядок сортировки')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Временная метка, указывающая, когда была создана заметка.', verbose_name='Создан')),
                ('user', models.ForeignKey(help_text='Пользователь, которому принадлежит заметка.', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='main.telegramuser', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
