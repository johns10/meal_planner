from django.apps import AppConfig


class PuretacodietConfig(AppConfig):
    name = 'puretacodiet'
    
    def ready(self):
        import puretacodiet.signals