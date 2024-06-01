# Generated by Django 5.0.4 on 2024-05-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minorproject', '0009_alter_patients_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('substitute0', models.CharField(max_length=1000)),
                ('substitute1', models.CharField(max_length=1000)),
                ('substitute2', models.CharField(max_length=1000)),
                ('substitute3', models.CharField(max_length=1000)),
                ('substitute4', models.CharField(max_length=1000)),
                ('sideEffect0', models.CharField(max_length=1000)),
                ('sideEffect1', models.CharField(max_length=1000)),
                ('sideEffect2', models.CharField(max_length=1000)),
                ('sideEffect3', models.CharField(max_length=1000)),
                ('sideEffect4', models.CharField(max_length=1000)),
                ('sideEffect5', models.CharField(max_length=1000)),
                ('sideEffect6', models.CharField(max_length=1000)),
                ('sideEffect7', models.CharField(max_length=1000)),
                ('sideEffect8', models.CharField(max_length=1000)),
                ('sideEffect9', models.CharField(max_length=1000)),
                ('sideEffect10', models.CharField(max_length=1000)),
                ('sideEffect11', models.CharField(max_length=1000)),
                ('sideEffect12', models.CharField(max_length=1000)),
                ('sideEffect13', models.CharField(max_length=1000)),
                ('sideEffect14', models.CharField(max_length=1000)),
                ('sideEffect15', models.CharField(max_length=1000)),
                ('sideEffect16', models.CharField(max_length=1000)),
                ('sideEffect17', models.CharField(max_length=1000)),
                ('sideEffect18', models.CharField(max_length=1000)),
                ('sideEffect19', models.CharField(max_length=1000)),
                ('sideEffect20', models.CharField(max_length=1000)),
                ('sideEffect21', models.CharField(max_length=1000)),
                ('sideEffect22', models.CharField(max_length=1000)),
                ('sideEffect23', models.CharField(max_length=1000)),
                ('sideEffect24', models.CharField(max_length=1000)),
                ('sideEffect25', models.CharField(max_length=1000)),
                ('sideEffect26', models.CharField(max_length=1000)),
                ('sideEffect27', models.CharField(max_length=1000)),
                ('sideEffect28', models.CharField(max_length=1000)),
                ('sideEffect29', models.CharField(max_length=1000)),
                ('sideEffect30', models.CharField(max_length=1000)),
                ('sideEffect31', models.CharField(max_length=1000)),
                ('sideEffect32', models.CharField(max_length=1000)),
                ('sideEffect33', models.CharField(max_length=1000)),
                ('sideEffect34', models.CharField(max_length=1000)),
                ('sideEffect35', models.CharField(max_length=1000)),
                ('sideEffect36', models.CharField(max_length=1000)),
                ('sideEffect37', models.CharField(max_length=1000)),
                ('sideEffect38', models.CharField(max_length=1000)),
                ('sideEffect39', models.CharField(max_length=1000)),
                ('sideEffect40', models.CharField(max_length=1000)),
                ('sideEffect41', models.CharField(max_length=1000)),
                ('use0', models.CharField(max_length=1000)),
                ('use1', models.CharField(max_length=1000)),
                ('use2', models.CharField(max_length=1000)),
                ('use3', models.CharField(max_length=1000)),
                ('use4', models.CharField(max_length=1000)),
                ('chemicalClass', models.CharField(max_length=1000)),
                ('habitForming', models.BooleanField()),
                ('therapeuticClass', models.CharField(max_length=1000)),
                ('actionClass', models.CharField(max_length=1000)),
            ],
        ),
    ]
