[app]
title = Perfect English Test
package.name = perfectenglishtest
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

# Важно: добавляем jnius явно
requirements = python3,kivy,jnius>=1.4.0

orientation = portrait
fullscreen = 0

# Используем проверенные версии API и NDK
android.api = 33
android.ndk = 25b