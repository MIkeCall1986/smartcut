<p align="center">
  <img src="images/logo_small.png" alt="Logo" width="250">
</p>

<h1 align="center">Video Smartcut</h1>

[![PyPI - Version](https://img.shields.io/pypi/v/smartcut?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/smartcut) [![Discord](https://img.shields.io/discord/1257684604941504623?logo=discord&logoColor=blue&label=Join%20Discord)](https://discord.gg/uYGkyfzU4c)

**UPDATE Feb 2026:**
- **This repo is no longer being updated.**
- The code is no longer integrated with SMC and maintaining a separate open source repo got too difficult.
- New performance & correctness fixes are only in [SMC](https://smartmediacutter.com).
- The SMC executable has the same CLI syntax, e.g. `.\smart-media-cutter.exe input.mp4 output.mp4 --keep 10,20`
- I still read the repo issues, so feel free to open them.

---

This tool is an open-source CLI companion to [Smart Media Cutter](https://smartmediacutter.com).

`smartcut` can cut video files in many different formats and codecs with only minimal recoding around the cutpoints (a.k.a. "smart cut").

This means that you can cut even long video files in seconds!

In contrast, [Smart Media Cutter](https://smartmediacutter.com) is fully-featured linear video editor with a lot more features like: Easy to use GUI, Transcript based editing (edit videos like text documents), Automatic silence cutting, Export timeline to editors like Resolve & Premiere and a generous free tier.

## Demo
<p align="center">
  <a href=https://youtu.be/_OBDNVxydB4><img src="images/yt_thumbnail.png" alt="Logo" width="400"></a>
</p>

## Open Sourced Features

- **Efficient Cutting**: `smartcut` only recodes around the cutpoints, preserving the majority of the original video quality.
- **Flexible Input**: Supports a wide range of video/audio formats and codecs.
- **Flexible cutting**: Allows for both "keep" and "cut" operations based on specified input times.
- **Audio Export**: Includes all audio tracks by default with nearly lossless passthrough.

## Installation

Get built binaries for Windows and Linux from [releases](https://github.com/skeskinen/smartcut/releases).

### Install from PyPI

```bash
# Install directly with pip
pip install smartcut

# Or use pipx for isolated installation
pipx install smartcut

# Then run from anywhere
smartcut input.mp4 output.mp4 --keep 10,20,40,50
```

### Install from source
```
# Clone this repository:
git clone https://github.com/skeskinen/smartcut.git
cd smartcut
# Create python virtual environment:
python -m venv venv
source venv/bin/activate
# Install the project to venv along with required dependencies:
pip install .
# Run:
python ./smartcut input.mp4 output.mp4 --keep 10,20,40,50
```

## Usage

The CLI requires the input and output file paths as positional arguments. You can specify the segments to keep or cut using the `--keep` or `--cut` options.

### Basic Commands

- **Keep specific segments**:

  `smartcut.exe input.mp4 output.mp4 --keep 10,20,40,50`

  This keeps the segments from 10s to 20s and from 40s to 50s.

- **Cut specific segments**:

  `smartcut.exe input.mp4 output.mp4 --cut 30,40,01:00,01:10`

  This cuts out the segments from 30s to 40s and from 1m to 1m10s, keeping the rest.

- **Various shorthands**:
```bash
  smartcut input.mp4 output.mp4 -k 10,20,40,50 # -k for --keep
  smartcut input.mp4 output.mp4 -c 30,35 # -c for --cut

  # Video start end keywords: s/start and e/end
  smartcut input.mp4 output.mp4 -k start,30,01:00,end
  smartcut input.mp4 output.mp4 -k s,30,60,e

  # Negative timestamps for counting from end of file
  smartcut input.mp4 output.mp4 -c "-5,end"          # Cut last 5 seconds
  smartcut input.mp4 output.mp4 -k 10,-10          # Keep 10s to 10s from end
  smartcut input.mp4 output.mp4 -k 0,-1:30         # Keep all but last 1m30s
```

- **Specify log level**:

  `smartcut.exe input.mp4 output.mp4 --keep 10,20 --log-level info`

### Audio Export

By default, all audio tracks are included with passthrough codec settings. This can be adjusted by modifying the `AudioExportInfo` in the script if needed.

## Contributing

Contributions are welcome! All the code will be licensed under MIT license.

Any changes have to work with the closed-source GUI app as well, so please coordinate with me if you want to make significant changes. You can find me on [discord](https://discord.gg/uYGkyfzU4c) most of the time.

## Testing

We have ok test coverage for various video and audio formats. Video tests check that pixel values are ~unchanged. In audio testing it's harder to check if the output is the same as input, but we try our best by checking the correlation of input&output as well as absolute diff.

Some of the tests depend on components in the GUI app that are not open-source. These tests are disabled.

Some commands to run different subsets of tests:
```bash
  # Test synthetic H.264 tests only
  python smartcut_tests.py --category h264

  # Test only real-world H.264 videos
  python smartcut_tests.py --category real_world_h264

  # Test all real-world videos (all codecs)
  python smartcut_tests.py --category real_world

  # See all available categories
  python smartcut_tests.py --list-categories
```


Normal test run looks like this:
```
Skipping smc tests
test_h264_cut_on_keyframes: PASS
test_h264_smart_cut: PASS
test_h264_24_fps_long: PASS
test_h264_1080p: PASS
test_h264_multiple_cuts: PASS
test_h264_profile_baseline: PASS
test_h264_profile_main: PASS
test_h264_profile_high: PASS
test_h264_profile_high10: PASS
test_h264_profile_high422: PASS
test_h264_profile_high444: PASS
test_mp4_cut_on_keyframe: PASS
test_mp4_smart_cut: PASS
test_mp4_to_mkv_smart_cut: PASS
test_mkv_to_mp4_smart_cut: PASS
test_vp9_smart_cut: PASS
test_vp9_profile_1: PASS
test_av1_smart_cut: PASS
test_avi_smart_cut: PASS
test_flv_smart_cut: PASS
test_mov_smart_cut: PASS
test_wmv_smart_cut: PASS
test_mpg_cut_on_keyframes: PASS
test_mpg_smart_cut: PASS
test_m2ts_mpeg2_smart_cut: PASS
test_m2ts_h264_smart_cut: PASS
test_ts_smart_cut: PASS
test_night_sky: PASS
test_night_sky_to_mkv: PASS
test_sunset: PASS
test_h265_cut_on_keyframes: PASS
test_h265_smart_cut: PASS
test_h265_smart_cut_large: PASS
test_mp4_h265_smart_cut: PASS
test_vertical_transform: PASS
x265 [warning]: Source height < 720p; disabling lookahead-slices
x265 [warning]: Source height < 720p; disabling lookahead-slices
test_video_recode_codec_override: PASS
test_vorbis_passthru: PASS
test_mkv_with_video_and_audio_passthru: PASS
test_mp3_passthru: PASS
test_seeking: PASS
Tests ran in 153.6s
```

## Acknowledgements

* This project is part of [Smart Media Cutter](https://smartmediacutter.com)
* We use [PyAV](https://github.com/PyAV-Org/PyAV) to interface with [ffmpeg](https://www.ffmpeg.org/) internals in a pythonic way
* [avcut](https://github.com/anyc/avcut) is one of better smartcut implementations and their code was useful in understanding some of the nuances


## Other projects

* [lossless-cut](https://github.com/mifi/lossless-cut) has an experimental smartcut mode. Being an experimental feature, it's not really supported. [Link to discussion](https://github.com/mifi/lossless-cut/issues/126)
* [VidCutter](https://github.com/ozmartian/vidcutter) also has an experimental smartcut mode.
* [This shell script github gist](https://gist.github.com/fernandoherreradelasheras/5eca67f4200f1a7cc8281747da08496e) inspired the lossless-cut implementation of smartcutting.
* [VideoReDo](https://www.videohelp.com/software/VideoReDo) was a popular closed source frame accurate video trimming tool. It is no longer supported.
* [SolveigMM Video Splitter](https://www.solveigmm.com/en/products/video-splitter/) and [TMPGEnc MPEG Smart Renderer](https://tmpgenc.pegasys-inc.com/en/product/tmsr6.html) are 2 other commercial smartcutting tools. I have no experience with these. [Here's one review](https://github.com/mifi/lossless-cut/issues/126#issuecomment-2035823788)
* [mp3splt](https://mp3splt.sourceforge.net/mp3splt_page/home.php) does lossless cutting of mp3, vorbis and other audio formats
* [mp3DirectCut](https://mpesch3.de/) is a proprietary audio lossless cutting tool. This one supports mp3 and aac.
* [Avidemux](https://avidemux.sourceforge.net/) used to have a mode called [SmartCopy](https://www.avidemux.org/admWiki/doku.php?id=using:cutting#intra_frames_and_smartcopy) but according to [this forum post](https://avidemux.org/smif/index.php?topic=16372.0) it was removed in avidemux 2.6 and current version only supports cutting on keyframes (at least I think so).
* [Machete](https://www.machetesoft.com/) Quick and light lossless video cutting tool. Not free, but has a 14-day trial version.

## Version History

### 1.7
* Set hev1 encoder tag for h265 in mp4 and mov. Improves compatibility in some cases.
* Improved test suite to catch more encoding issues.

### 1.6
* Proper handling of HEVC CRA and RASL frames.
* Other small compatibility changes.
* Set encoded by program name to 'smartcut'.

### 1.5
* Better handling of inputs where DTS is missing.
* Code cleanups to get clean pyright output

### 1.4
* Support converting from .ts to .mp4/.mkv.
* Add support for .mkv attachments. They are copied to output when cutting a file with attachments.
* Various small fixes to cutting correctness and corner cases.
* Added --flaky to test suite to catch even more corner cases.
* All tests pass with 10 different random seeds.
* Update to PyAV 16.

### 1.3.3
* Another h264 NAL detection fix

### 1.3.2
* Fix memory usage issues for good with better handling of large GoPs
* Fix an issue with certain types of h264 streams

### 1.3.1
* Fix a critical issue in h265 smartcutting that caused a lot of memory usage when cutting specific types of h265 streams
* Better h265 gop detection
* Added h265 CRA to BLA conversion

### 1.3
* Update to PyAV 15.0
* Fixed some critical issues in h264 and h265 smartcutting
* A lot more tests with real world videos
* Improve command line time parameter handling
* Preserve disposition data when cutting (forced subtitles, etc.) #14

### 1.2
* [#11](https://github.com/skeskinen/smartcut/pull/11) Allow frame number input instead of time input, by snelg

Starting from this version the Windows binaries are unsigned. This means that you'll probably get a security warning about running unsigned code. If this bothers you, you can either use older versions or run the software from source code.

### 1.1
* Cut subtitle tracks
* Add support for MPEG-2 cutting and more container formats (.flv, .mov, .wmv, .avi)
* Add timecode format hh:mm:ss to the command line interface

### 1.0
* Initial opensource release
* Frame accurate smart cutting of most modern video codecs (h264, h265, vp9, av1)

20.02.26 Sync fork
Ось результати аналізу та стратегія трансформації для проекту **Smartcut**, підготовлені у форматі для копіювання в Notion.

---

# 📑 Звіт AI-консультанта: Проект "Smartcut"

**Smartcut** — це спеціалізований CLI-інструмент для обрізки відеофайлів різних форматів і кодеків із мінімальним перекодуванням лише в точках розрізу.

---

## 🧬 Частина 1: "ДНК" Проекту

Логіку коду проекту можна розбити на такі **атомарні функції**:

*   **Парсинг команд та часових міток:** Обробка вхідних аргументів `--keep` та `--cut`, підтримка форматів часу (секунди, hh:mm:ss), номерів кадрів та від'ємних значень для відліку з кінця файлу.
*   **Інтерфейс до нутрощів FFmpeg:** Використання бібліотеки **PyAV** для взаємодії з медіа-потоками на низькому рівні у "пітонічному" стилі.
*   **Інтелектуальна обрізка (Smart Cutting):** Логіка перекодування відео лише навколо точок розрізу (cutpoints), що дозволяє зберегти оригінальну якість основної частини матеріалу.
*   **Управління потоками (Stream Passthrough):** Автоматичне копіювання всіх аудіодоріжок, субтитрів та метаданих (disposition data) без втрати якості.
*   **Обробка контейнерів та вкладень:** Підтримка конвертації між форматами (.ts в .mp4/.mkv) та копіювання вкладень (attachments) для MKV.

### 💎 Головна технічна цінність
Головна цінність проекту — **поєднання швидкості та збереження якості**. Завдяки "розумній" обрізці навіть довгі відео обробляються за лічені секунди, оскільки більша частина даних просто копіюється, а не рендериться заново.

---

## 🚀 Частина 2: "Трансформація" (Інтеграція з Gemini LLM)

Додавання мультимодальної моделі **Gemini** (через **GitHub Models**) перетворює Smartcut із технічної утиліти на **автоматизовану студію монтажу**.

### Як зміниться функціонал?
1.  **Семантичний монтаж:** Замість ручного введення секунд, ви кажете Gemini: *"Залиш тільки моменти, де спікер говорить про інвестиції"*. Gemini аналізує аудіо/відео і генерує точні мітки для `--keep`.
2.  **Автоматичне видалення невдалих дублів:** LLM може ідентифікувати повторювані сцени або візуальний шум і автоматично формувати команду `--cut` для очищення відео.
3.  **Розумне тегування:** Gemini аналізує вміст розрізаних фрагментів і автоматично прописує метадані для вихідного файлу.

### Сценарій сервісу "Video Highlight Bot" (Smartcut + Gemini + ID_{$})

Сценарій створення сервісу автоматичної генерації хайлайтів на вашому сайті:
1.  **Завантаження (ID_{$}):** Ваш скрипт приймає відео від користувача та витягує з нього аудіодоріжку або ключові кадри.
2.  **Аналіз (Gemini):** Gemini (через **GitHub Models**) аналізує контент і повертає список "цікавих" часових проміжків у форматі JSON.
3.  **Обробка (ID_{$}):** Скрипт-оркестратор перетворює JSON у команду для `smartcut.exe` (наприклад: `smartcut input.mp4 output.mp4 -k 10,60,120,180`).
4.  **Миттєвий монтаж:** Проект Smartcut виконує фізичну обрізку без втрати якості за частки секунди.
5.  **Доставка:** Готовий ролик публікується на сайті, а вихідні дані зберігаються.
6.  **Деплой:** Використовуючи **GitHub Spark**, ви розгортаєте цей інтелектуальний інтерфейс як веб-застосунок.

---

## 📋 План дій для Notion
| Крок | Дія | Результат |
| :--- | :--- | :--- |
| **1** | Встановлення `smartcut` через `pip` або `pipx` | Робоче ядро для маніпуляцій відео |
| **2** | Підключення Gemini API для аналізу відео/аудіо | Автоматичне визначення точок розрізу |
| **3** | Створення Python-обгортки `ID_{$}` для CLI | Зв'язок ШІ-логіки з фізичною обрізкою |
| **4** | Розгортання через **GitHub Spark** | Готовий інтелектуальний сервіс монтажу |

---

### 💡 Резюме

**Суть:** **Швидка обрізка відео без втрати якості**.

**AI-Роль:** **Створення інтелектуальних відео-сервісів через Spark**.
