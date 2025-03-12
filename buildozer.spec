[app]
source.dir = lazigame
title = lazigame
package.name = lazigame
package.domain = org.lazigame
source.include_exts = py,png,jpg,kv,atlas,ogg,wav,mp3
version = 1.0
requirements = python3, pygame
orientation = landscape
fullscreen = 1
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 0

[app.android]
android.ndk = 23b
android.api = 33
android.minapi = 21
android.gradle_dependencies = com.android.support:support-v4:28.0.0
android.meta-data = android.max_aspect=2.1, android.notch_support=true
android.arch = arm64-v8a, armeabi-v7a
android.allow_backup = 0
android.compile_options = -O2