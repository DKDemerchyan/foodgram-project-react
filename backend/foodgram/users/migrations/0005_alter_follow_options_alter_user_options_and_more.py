# Generated by Django 4.1.1 on 2022-09-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_follow_author_follow_unique_follow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['-id'], 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', models.F('following')), _negated=True), name='prevent_self_follow'),
        ),
    ]