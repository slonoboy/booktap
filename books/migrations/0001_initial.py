
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('id_number', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('genres', models.CharField(blank=True, max_length=150)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BookOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('call_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.account')),
            ],
        ),
        migrations.CreateModel(
            name='SocialRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_borrows', models.IntegerField(default=0)),
                ('late_returns', models.IntegerField(default=0)),
                ('total_requests', models.IntegerField(default=0)),
                ('cancelled_requests', models.IntegerField(default=0)),
                ('total_reviews', models.IntegerField(default=0)),
                ('compliants_received', models.IntegerField(default=0)),
                ('final_rating', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.account')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000)),
                ('rating', models.BooleanField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.account')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('deliver_date', models.DateField(blank=True, default=None, null=True, verbose_name='deliver date')),
                ('isDelivering', models.BooleanField(default=True)),
                ('isCancelled', models.BooleanField(default=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookowned')),
                ('from_lib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.library')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.account')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('return_date', models.DateField(blank=True, default=None, null=True, verbose_name='return date')),
                ('isActive', models.BooleanField(default=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookowned')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.account')),
            ],
        ),
        migrations.AddField(
            model_name='bookowned',
            name='original_library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.library'),
        ),
        migrations.AddField(
            model_name='account',
            name='library_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.library'),
        ),
    ]
