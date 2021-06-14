from django.apps import AppConfig


class CustomUiTutorialAppConfig(AppConfig):
    name = 'custom_ui_tutorial_app'
    label = name
    verbose_name = "Custom UI Tutorial App"
    fa_icon_class = "fa-comment"
    url_home = "custom_ui_tutorial_app:hello_world"
