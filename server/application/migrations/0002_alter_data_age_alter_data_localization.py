# Generated by Django 5.1.3 on 2024-11-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='localization',
            field=models.CharField(choices=[('ear', 'Ear'), ('face', 'Face'), ('neck', 'Neck'), ('scalp', 'Scalp'), ('abdomen', 'Abdomen'), ('back', 'Back'), ('chest', 'Chest'), ('trunk', 'Trunk - Other'), ('acral', 'Acral (Fingers/Toes)'), ('hand', 'Hand'), ('upper_extremity', 'Upper Extremity (Arm)'), ('foot', 'Foot'), ('lower_extremity', 'Lower Extremity (Leg)'), ('genital', 'Genital Area')], max_length=15, null=True),
        ),
    ]
