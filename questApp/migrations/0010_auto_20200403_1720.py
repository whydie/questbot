# Generated by Django 2.1.5 on 2020-04-03 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questApp', '0009_auto_20200321_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestPermittedPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='quest',
            name='price_per_unit',
        ),
        migrations.AddField(
            model_name='playersquest',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Завершил'),
        ),
        migrations.AddField(
            model_name='quest',
            name='max_attempts',
            field=models.PositiveIntegerField(default=1, verbose_name='Максимальное количество попыток'),
        ),
        migrations.AlterField(
            model_name='playersquest',
            name='attempts_num',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество завершенных игр'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Цена в рублях'),
        ),
        migrations.AddField(
            model_name='questpermittedplayers',
            name='players_quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questApp.PlayersQuest'),
        ),
        migrations.AddField(
            model_name='questpermittedplayers',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questApp.Quest'),
        ),
        migrations.AddField(
            model_name='quest',
            name='players_with_access',
            field=models.ManyToManyField(related_name='permitted_quests', through='questApp.QuestPermittedPlayers', to='questApp.PlayersQuest'),
        ),
        migrations.AlterUniqueTogether(
            name='questpermittedplayers',
            unique_together={('quest', 'players_quest')},
        ),
    ]
