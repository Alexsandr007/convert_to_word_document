# Generated by Django 4.0.1 on 2022-10-21 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionRisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskAcceptability',
            fields=[
                ('value', models.CharField(choices=[('1', 'Да'), ('2', 'Нет')], max_length=10)),
                ('comments', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('profession_risk', models.ManyToManyField(to='form.ProfessionRisk')),
            ],
        ),
        migrations.CreateModel(
            name='LevelRisk',
            fields=[
                ('value', models.IntegerField()),
                ('risk_acceptability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.riskacceptability')),
            ],
        ),
        migrations.CreateModel(
            name='DegreeProbability',
            fields=[
                ('value', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('level_risk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.levelrisk')),
            ],
        ),
        migrations.CreateModel(
            name='WeightConsequence',
            fields=[
                ('value', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('degree_probability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.degreeprobability')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('title', models.TextField()),
                ('weight_consequences', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.weightconsequence')),
            ],
        ),
        migrations.CreateModel(
            name='EventCondition',
            fields=[
                ('value', models.CharField(choices=[('A', 'Аварийные(A)'), ('HT', 'Нетипичные(HT)'), ('T', 'Типичные(T)')], max_length=30)),
                ('measures', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.measure')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('description', models.TextField()),
                ('event_conditions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.eventcondition')),
            ],
        ),
        migrations.CreateModel(
            name='DangerousEvent',
            fields=[
                ('description', models.TextField()),
                ('effects', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.effect')),
            ],
        ),
        migrations.CreateModel(
            name='Danger',
            fields=[
                ('description', models.TextField()),
                ('dangerous_event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='form.dangerousevent')),
            ],
        ),
        migrations.AddField(
            model_name='professionrisk',
            name='danger',
            field=models.ManyToManyField(to='form.Danger'),
        ),
    ]