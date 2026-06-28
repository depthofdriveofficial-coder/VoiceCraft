# VoiceCraft - Flutter TTS + Voice Clone App

## Features
- Text to Speech (Android native, offline, free)
- Voice Clone (apni awaaz record karo, pitch/speed analyze hogi)
- Multi-language: English, Urdu, Hindi, Arabic, French, German, Spanish
- Audio save karna
- Saved files manager

---

## Setup Steps

### Step 1: Flutter Install karo
1. https://flutter.dev/docs/get-started/install par jao
2. Windows ke liye: Flutter SDK download karo, PATH mein add karo
3. Android Studio install karo (free)
4. Terminal mein chalao: `flutter doctor`
5. Sab green ho jaye to ready ho

### Step 2: Project Setup
```bash
# Ye folder apne PC par copy karo, phir:
cd voicecraft_app
flutter pub get
```

### Step 3: Android Phone Connect karo
1. Phone mein Developer Options on karo
2. USB Debugging on karo
3. Phone connect karo PC se
4. Terminal mein: `flutter devices` (phone dikhna chahiye)

### Step 4: APK Build karo
```bash
# Release APK banao
flutter build apk --release

# APK yahan milegi:
# build/app/outputs/flutter-apk/app-release.apk
```

### Step 5: Install karo
```bash
# Direct install via USB
flutter install

# Ya APK file phone par copy karo aur manually install karo
```

---

## Voice Clone ke baare mein important note
Is app mein "voice clone" matlab hai:
- Tumhari awaaz record hoti hai
- Uski pitch aur speed analyze hoti hai
- Android TTS engine us pitch/speed se bolti hai

100% perfect voice clone ke liye deep learning model chahiye (Coqui RVC etc.)
jo 2GB+ ka hota hai aur phone par chalana mushkil hai.
Yeh app best possible free approach use karta hai.

---

## Troubleshooting
- `flutter pub get` fail ho to: internet check karo
- APK install na ho to: Phone settings > Unknown sources > Allow
- Microphone kaam na kare to: App permissions check karo
