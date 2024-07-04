from .models import *
from rest_framework import serializers

from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class PerevalImagesSerializer(serializers.ModelSerializer):
    img = serializers.URLField()

    class Meta:
        model = PerevalImages
        fields = ['title', 'img']


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()
    images = PerevalImagesSerializer(many=True)

    class Meta:
        model = Pereval
        depth = 1
        fields = ['status','beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coord', 'level',
                  'images']

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coord = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        # Проверяем user, если точно такой же существует в БД, нового не создаем
        user, created = User.objects.get_or_create(**user)

        coord = Coord.objects.create(**coord)
        level = Level.objects.create(**level)

        pereval = Pereval.objects.create(**validated_data, user=user, coord=coord, level=level)

        for image in images:
            data = image.pop('img')
            title = image.pop('title')
            PerevalImages.objects.create(img=data, pereval=pereval, title=title)

        return pereval
