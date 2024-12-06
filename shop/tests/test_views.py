from django.test import TestCase, Client

class WebpageAccessibilityTestCase(TestCase):
    def setUp(self):
        # Создаем клиент для имитации запросов
        self.client = Client()

    def test_webpage_accessibility(self):
        # Проверяем, что главная страница доступна
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
