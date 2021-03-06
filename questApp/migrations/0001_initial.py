# Generated by Django 2.1.5 on 2019-06-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Текст опции')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Скрытый')),
                ('is_winning', models.BooleanField(default=False, verbose_name='Победный вариант')),
                ('index', models.PositiveSmallIntegerField(default=1, verbose_name='Индекс отображения')),
                ('changes', models.ManyToManyField(blank=True, to='questApp.Option', verbose_name='Изменяет опции')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='PlayersQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Играет прямо сейчас')),
                ('attempts_num', models.PositiveIntegerField(default=0, verbose_name='Количество попыток в розыгрыше')),
                ('changes', models.ManyToManyField(blank=True, to='questApp.Option', verbose_name='Изменяет опции')),
            ],
            options={
                'verbose_name': 'Активная игра',
                'verbose_name_plural': 'Активные игры',
            },
        ),
        migrations.CreateModel(
            name='PlayersQuestCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_won', models.DateTimeField(auto_now_add=True, verbose_name='Дата окончания квеста')),
                ('is_in_awarding_time', models.BooleanField(default=False, verbose_name='Проходил во время розыгрыша')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_quests_completed', to='player.Player', verbose_name='Игрок')),
            ],
            options={
                'verbose_name': 'Победа игрока',
                'verbose_name_plural': 'Победы игроков',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный квест')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена в рублях')),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Снижение цены за 1 шт. в рублях')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('date_awarding_start', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала розыгрыша')),
                ('date_awarding_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания розыгрыша')),
                ('awarding_descr', models.TextField(blank=True, default='', null=True, verbose_name='Описание розыгрыша')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=4096, verbose_name='Текст:\nтекст;текст~время\n')),
                ('is_first', models.BooleanField(default=False, verbose_name='Первый шаг')),
                ('delay', models.FloatField(default=1, verbose_name='Стандартная задержка (сек)')),
                ('options', models.ManyToManyField(blank=True, to='questApp.Option', verbose_name='Варианты ответов')),
                ('quest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questApp.Quest', verbose_name='Квест')),
            ],
            options={
                'verbose_name': 'Шаг',
                'verbose_name_plural': 'Шаги',
            },
        ),
        migrations.AddField(
            model_name='playersquestcompleted',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_quests_completed', to='questApp.Quest', verbose_name='Квест'),
        ),
        migrations.AddField(
            model_name='playersquest',
            name='current_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='questApp.Step', verbose_name='Текущий шаг'),
        ),
        migrations.AddField(
            model_name='playersquest',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_quests', to='player.Player', verbose_name='Игрок'),
        ),
        migrations.AddField(
            model_name='playersquest',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questApp.Quest', verbose_name='Квест'),
        ),
        migrations.AddField(
            model_name='option',
            name='next_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='questApp.Step', verbose_name='Следующий шаг'),
        ),
        migrations.AddField(
            model_name='option',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questApp.Quest', verbose_name='Квест'),
        ),
        migrations.AlterUniqueTogether(
            name='playersquest',
            unique_together={('player', 'quest')},
        ),
    ]
