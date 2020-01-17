app_notification = '''Привет, это Stepik VideoGames, портал видео про видеоигры.
Введите 1 чтобы посмотреть видео и 2 чтобы посмотреть плейлист, exit или 0, чтобы выйти.
'''

VIDEO_REQUEST = '1'
PLAYLIST_REQUEST = '2'
EXIT_REQUESTS = ['exit', '0']
NOT_FOUND_INFO = 'Ничего не найдено\n'


# videos ------------------

videos = {
    0: {'id': 0, 'title': 'ИгроСториз: Mafia 4, GTA 6 и BioShock Online – Take-Two дает бой конкурентам на '
       'PS5 и Xbox Series X', 'videoid': 'https://youtu.be/05GPNjBtF48'},
    1: {'id': 1, 'title': 'Поиграли в Sekiro: Shadows Die Twice. Свежо, но знакомо',
        'videoid': 'https://youtu.be/nwPs5f4WLN8'},
    2: {'id': 2, 'title': 'Gothic Remake - Актуально ли в 2021 году ? [Мнение после Демки]',
        'videoid': 'https://youtu.be/eVtx5Y6lFjk'},
    3: {'id': 3, 'title': 'Начало прохождения - Anno 1800 #01', 'videoid': 'https://youtu.be/J3Wk2CecrUg'},
    4: {'id': 4, 'title': 'ИгроСториз: Итоги 2019 года. ПК победит PS5 и Xbox, сюжетные игры оживают, '
                          'крупные студии вымрут?', 'videoid': 'https://youtu.be/pxsJsFjCcgU'},
    5: {'id': 5, 'title': 'Подробности игры по «Властелину колец», глобальный мод для Mafia II, '
                          'падение популярности Dota 2...', 'videoid': 'https://youtu.be/UdsrgZk5lVA'},
    6: {'id': 6, 'title': 'ИГРОВЫЕ НОВОСТИ STALKER 2, про The Elder Scrolls 6, Medal of Honor, '
                          'PlayStation 5, Final Fantasy 7', 'videoid': 'https://youtu.be/VYAk05t6Q'},
    7: {'id': 7, 'title': 'Эпидерсия: Невероятный случай на Кикстартер. Игра о драконах собрала кучу денег '
                          'из-за Гарри Поттера', 'videoid': 'https://youtu.be/fvTZTx6tlAU'},
    8: {'id': 8, 'title': 'Поиграли в Borderlands 3. Вооружённая жертва Epic Games Store',
        'videoid': 'https://youtu.be/NXlosGTO3'},
    9: {'id': 9, 'title': '10 лучших хорроров десятилетия. От Amnesia: The Dark Descent до Resident Evil 2 Remake',
        'videoid': 'https://youtu.be/83r7CffMmS8'},
    10: {'id': 10, 'title': 'АААА-новости #135. Новогодний эфир. Вопросы, ответы, рефлексия',
         'videoid': 'https://youtu.be/ksWZfVsxTN4'},
    11: {'id': 11, 'title': 'Экранизация GTA, новинки Star Citizen, мультиплеер Cyberpunk 2077, боссы '
                            'Final Fantasy VII Remake...', 'videoid': 'https://youtu.be/TkVUnyEAk0M'},
    12: {'id': 12, 'title': 'АААА-новости #135. Новогодний эфир. Вопросы, ответы, рефлексия',
         'videoid': 'https://youtu.be/ksWZfVsxTN4'},
    13: {'id': 13, 'title': 'Игромания! ИГРОВЫЕ НОВОСТИ, 16 декабря (The Game Awards 2019, '
                            'Resident Evil 3, Half-Life: Alyx)', 'videoid': 'https://youtu.be/xn6URedv4LQ'},
}


def handle_videos(videos, not_found_info=NOT_FOUND_INFO):
    print('Выберите, какое видео, вы хотите посмотреть:\n')

    for index, video in enumerate(videos):
        print(f'''{index + 1}. {videos[video]['title']}''')

    print('\n')

    request = int(input()) - 1
    if request in videos:
        print(f'''Ваше видео:
{videos[request]['title']}
{videos[request]['videoid']}
Приятного просмотра!\n''')
    else:
        print(not_found_info)


# playlists ------------------

playlists = {
  "igrostories": {
    "title": "ИгроСториз",
    "videos" : [0, 4, 7]
  },
  "programs": {
    "title": "Репортажи",
    "videos" : [8, 9]
  },
  "reviews": {
    "title": "Обзоры",
    "videos" : [1, 2]
  },
  "letsplays": {
     "title": "Летсплеи",
     "videos": [3]
  },
  "news": {
     "title": "Новости",
     "videos": [5, 6, 10, 11, 12, 13]
  },
}


def handle_playlists(playlists, not_found_info=NOT_FOUND_INFO):
    print('Выберите, какой плейлист, вы хотите посмотреть:\n')

    for index, playlist in enumerate(playlists):
        print(f'''{index + 1}. {playlists[playlist]['title']} ({len(playlists[playlist]['videos'])} видео)''')

    print('\n')

    request = int(input())
    playlist_keys = list(playlists.keys())
    playlist_name = playlist_keys[request - 1] if len(playlist_keys) >= request > 0 else False

    if playlist_name:
        print(f'''{playlists[playlist_name]['title']}:\n''')
        for index, video in enumerate(playlists[playlist_name]['videos']):
            print(f'''{index + 1}. {videos[video]['title']}\n{videos[video]['videoid']}\n''')
        print('Приятного просмотра\n')
    else:
        print(not_found_info)


# main part ------------------

def start_app():
    print(app_notification)

    while True:
        command = input()

        if command in EXIT_REQUESTS:
            break
        elif command == VIDEO_REQUEST:
            handle_videos(videos, 'Такого видео у нас нет, всего хорошего!\n')
        elif command == PLAYLIST_REQUEST:
            handle_playlists(playlists, 'Такого плейлиста у нас нет, всего хорошего!\n')
        else:
            print(NOT_FOUND_INFO)


start_app()