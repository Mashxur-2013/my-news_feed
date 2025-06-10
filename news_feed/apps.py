from django.apps import AppConfig


class NewsFeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_feed'

    def ready(self):
        import news_feed.translation
