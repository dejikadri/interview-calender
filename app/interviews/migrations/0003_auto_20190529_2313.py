# Generated by Django 2.2.1 on 2019-05-29 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0002_auto_20190528_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skype_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='OtherInterviewers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviews.InterviewSlot')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviews.Interviewer')),
            ],
        ),
    ]