from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories_per_serving', models.IntegerField()),
                ('image', models.ImageField(default='/home/adi/Pictures/Mahavatar-Babaji-Maharaj.jpg', upload_to='food_images')),
            ],
        ),
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_servings', models.IntegerField()),
                ('time_ate', models.DateTimeField(default=django.utils.timezone.now)),
                ('calories_consumed', models.PositiveIntegerField(blank=True, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
