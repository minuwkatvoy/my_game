[app]
# Имя приложения
title = MyGame

# Название пакета (замени "com.example.mygame" на своё)
package.name = mygame
package.domain = com.example

# Версия
version = 1.0.0

# Путь к исходникам (по умолчанию корень проекта)
source.dir = .

# Главный файл (замени на имя своего основного скрипта)
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# Значок и разрешения
permissions = INTERNET

[buildozer]
# Поддержка только Android
log_level = 2
warn_on_root = 0

[python]
# Требуемые зависимости (Pygame и др.)
requirements = python3,kivy,pygame

[android]
# Целевая платформа
android.api = 31
android.ndk = 23b
android.ndk_api = 21
android.minapi = 21
android.sdk = 31

# Архитектура
android.archs = arm64-v8a,armeabi-v7a

# Указываем, что это игра (ускоряет графику)
android.presplash_color = #000000
android.entrypoint = main.py
android.add_jars =

# Флаг для поддержки pygame
android.p4a_whitelist = pygame

# Поддержка современных Android API
p4a.branch = master
p4a.fork = kivy/python-for-android
android.gradle_dependencies =

# Включение Java 8 (если нужно)
android.gradle_arguments = "-Dorg.gradle.jvmargs=-Xmx4g"

[build]
# Опции сборки
ignore_setup_py = 1
