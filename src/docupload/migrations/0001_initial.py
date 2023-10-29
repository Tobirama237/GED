# Generated by Django 4.0.3 on 2022-03-16 05:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('libelleCat', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('libelleDoc', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('typeDoc', models.CharField(choices=[('fichier', 'Fichier'), ('image', 'Image'), ('video', 'Video')], default='fichier', max_length=10)),
                ('docUpload', models.FileField(upload_to='')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docupload.categorie')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]