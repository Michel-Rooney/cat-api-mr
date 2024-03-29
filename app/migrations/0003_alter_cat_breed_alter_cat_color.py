# Generated by Django 5.0.2 on 2024-02-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('si', 'Siamês'), ('pe', 'Persa'), ('mc', 'Maine Coon'), ('ra', 'Ragdoll'), ('be', 'Bengal'), ('ab', 'Abyssinian'), ('sf', 'Scottish Fold'), ('sp', 'Sphynx'), ('bs', 'British Shorthair')], max_length=2),
        ),
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('pr', 'preto'), ('br', 'branco'), ('ci', 'cinza'), ('ma', 'marrom'), ('gr', 'gengibre'), ('li', 'listrado'), ('am', 'amarelo'), ('ve', 'vermelho'), ('az', 'azul'), ('lar', 'laranja'), ('ro', 'rosa'), ('ro', 'roxo'), ('ver', 'verde'), ('ma', 'malhado')], max_length=3),
        ),
    ]
