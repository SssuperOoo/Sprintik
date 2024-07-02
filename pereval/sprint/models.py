from django.db import models


class Pereval(models.Model):
    CHOICE_STATUS = (
        ("new", 'новый'),
        ("pending", 'в работе'),
        ("accepted", 'принятно'),
        ("rejected", 'отклонено'),
    )
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default="new")

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')
    coord = models.ForeignKey('Coord', on_delete=models.CASCADE,
                              related_name='coord')  # Или все же OnetoOneField т.к. у одного перевала могут быть одни координаты? Или разные входы на перевал с разными координатами?
    level = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='level')

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.EmailField(max_length=255)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fam} {self.name} {self.otc}"


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    height = models.IntegerField()

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Height: {self.height}"


class Level(models.Model):
    CHOICE_LEVEL = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A'),
    )
    winter = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    summer = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    autumn = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    spring = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")

    def __str__(self):
        return f"Winter: {self.winter}, Summer: {self.summer}, Autumn: {self.autumn}, Spring: {self.spring}"


class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title
