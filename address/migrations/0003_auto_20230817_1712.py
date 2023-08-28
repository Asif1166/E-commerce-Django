# Generated by Django 3.2.16 on 2023-08-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_alter_address_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Bogra', 'Bogra'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chapainawabganj', 'Chapainawabganj'), ('Chattogram', 'Chattogram'), ('Chuadanga', 'Chuadanga'), ('Comilla', 'Comilla'), ('Cox’s Bazar', "Cox's Bazar"), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jashore', 'Jashore'), ('Jhalokathi', 'Jhalokathi'), ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Meherpur', 'Meherpur'), ('Moulvibazar', 'Moulvibazar'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Natore', 'Natore'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon')], default='Dhaka', max_length=100, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(choices=[('Bangladesh', 'Bangladesh')], default='Bangladesh', max_length=100, verbose_name='Country'),
        ),
    ]