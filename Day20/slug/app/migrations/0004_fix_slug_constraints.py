from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
