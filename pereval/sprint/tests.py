from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Pereval, User, Coord, Level, PerevalImages
from .serializers import PerevalSerializer
from django.urls import reverse


class PerevalApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Создаем пользователя
        self.user = User.objects.create(
            email="test@example.com",
            fam="Иванов",
            name="Иван",
            otc="Иванович",
            phone="1234567890"
        )

        # Создаем координаты
        self.coord = Coord.objects.create(
            latitude=45.3842,
            longitude=7.1525,
            height=1200
        )

        # Создаем уровень
        self.level = Level.objects.create(
            winter="1A",
            summer="1A",
            autumn="1A",
            spring="1A"
        )

        # Создаем перевал
        self.pereval = Pereval.objects.create(
            beauty_title="пер.",
            title="Пхия",
            other_title="Триев",
            connect="",
            user=self.user,
            coord=self.coord,
            level=self.level
        )

        # Создаем изображения
        self.image1 = PerevalImages.objects.create(
            pereval=self.pereval,
            title="Седловина",
            img="https://example.com/image1.jpg"
        )

        self.image2 = PerevalImages.objects.create(
            pereval=self.pereval,
            title="Подъем",
            img="https://example.com/image2.jpg"
        )

    def test_create_pereval(self):
        url = reverse('Pereval-list')
        data = {
            "beauty_title": "Пример",
            "title": "Пхия",
            "other_title": "Еще пример",
            "connect": "Описание соединения",
            "user": {
                "email": "example@mail.com",
                "fam": "Иванов",
                "name": "Иван",
                "otc": "Иванович",
                "phone": "+79031234567"
            },
            "coord": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1A"
            },
            "images": [
                {"title": "Седловина", "img": "https://example.com/image1.jpg"},
                {"title": "Подъем", "img": "https://example.com/image2.jpg"}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pereval.objects.count(), 2)
        self.assertEqual(response.data['id'], Pereval.objects.last().id)

        created_pereval = Pereval.objects.last()
        print(f"Pereval ID: {created_pereval.id}")
        print(f"Title: {created_pereval.title}")
        print(f"Other Titles: {created_pereval.other_title}")
        print(f"Connect: {created_pereval.connect}")
        print(f"User: {created_pereval.user}")
        print(f"Coordinates: {created_pereval.coord}")
        print(f"Level: {created_pereval.level}")
        print(f"Images: {[str(img) for img in created_pereval.images.all()]}")

    def test_get_pereval(self):
        url = reverse('Pereval-detail', kwargs={'pk': self.pereval.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = PerevalSerializer(self.pereval).data
        self.assertEqual(response.data, serializer_data)

        print(f"Pereval ID: {self.pereval.id}")
        print(f"Title: {self.pereval.title}")
        print(f"Other Titles: {self.pereval.other_title}")
        print(f"Connect: {self.pereval.connect}")
        print(f"User: {self.pereval.user}")
        print(f"Coordinates: {self.pereval.coord}")
        print(f"Level: {self.pereval.level}")
        print(f"Images: {[str(img) for img in self.pereval.images.all()]}")

    def test_update_pereval(self):
        url = reverse('Pereval-detail', kwargs={'pk': self.pereval.pk})
        data = {
            "status": "new",
            "beauty_title": "Пример",
            "title": "Еще раз обновленный перевал",
            "other_title": "Еще пример",
            "connect": "Описание соединения",
            "add_time": "2024-07-10T10:24:31.558345Z",
            "user": {
                "email": "test@example.com",
                "fam": "Иванов",
                "name": "Иван",
                "otc": "Иванович",
                "phone": "1234567890"
            },
            "coord": {
                "latitude": "45.384200",
                "longitude": "7.152500",
                "height": 1200
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1A"
            },
            "images": [
                {
                    "title": "Седловина",
                    "img": "https://example.com/image1.jpg"
                },
                {
                    "title": "Подъем",
                    "img": "https://example.com/image2.jpg"
                }
            ]
        }
        response = self.client.patch(url, data, format='json')
        self.pereval.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.pereval.title, "Еще раз обновленный перевал")

        print(f"Pereval ID: {self.pereval.id}")
        print(f"Title: {self.pereval.title}")
        print(f"Other Titles: {self.pereval.other_title}")
        print(f"Connect: {self.pereval.connect}")
        print(f"User: {self.pereval.user}")
        print(f"Coordinates: {self.pereval.coord}")
        print(f"Level: {self.pereval.level}")
        print(f"Images: {[str(img) for img in self.pereval.images.all()]}")

    def test_check_pereval(self):
        expected_data = {
            "beauty_title": "пер.",
            "title": "Пхия",
            "other_title": "Триев",
            "connect": "",
            "user": {
                "email": "test@example.com",
                "fam": "Иванов",
                "name": "Иван",
                "otc": "Иванович",
                "phone": "1234567890"
            },
            "coord": {
                "latitude": "45.384200",
                "longitude": "7.152500",
                "height": 1200
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1A"
            },
            "images": [
                {"title": "Седловина", "img": "https://example.com/image1.jpg"},
                {"title": "Подъем", "img": "https://example.com/image2.jpg"}
            ]
        }

        url = reverse('Pereval-detail', kwargs={'pk': self.pereval.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actual_data = response.data

        self.assertEqual(actual_data['beauty_title'], expected_data['beauty_title'])
        self.assertEqual(actual_data['title'], expected_data['title'])
        self.assertEqual(actual_data['other_title'], expected_data['other_title'])
        self.assertEqual(actual_data['connect'], expected_data['connect'])

        self.assertEqual(actual_data['user']['email'], expected_data['user']['email'])
        self.assertEqual(actual_data['user']['fam'], expected_data['user']['fam'])
        self.assertEqual(actual_data['user']['name'], expected_data['user']['name'])
        self.assertEqual(actual_data['user']['otc'], expected_data['user']['otc'])
        self.assertEqual(actual_data['user']['phone'], expected_data['user']['phone'])

        self.assertEqual(actual_data['coord']['latitude'], expected_data['coord']['latitude'])
        self.assertEqual(actual_data['coord']['longitude'], expected_data['coord']['longitude'])
        self.assertEqual(actual_data['coord']['height'], expected_data['coord']['height'])

        self.assertEqual(actual_data['level']['winter'], expected_data['level']['winter'])
        self.assertEqual(actual_data['level']['summer'], expected_data['level']['summer'])
        self.assertEqual(actual_data['level']['autumn'], expected_data['level']['autumn'])
        self.assertEqual(actual_data['level']['spring'], expected_data['level']['spring'])

        self.assertEqual(len(actual_data['images']), len(expected_data['images']))
        for i, img in enumerate(expected_data['images']):
            self.assertEqual(actual_data['images'][i]['title'], img['title'])
            self.assertEqual(actual_data['images'][i]['img'], img['img'])
