import wikipedia
import re


wikipedia.set_lang('ru')


def get_wiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000] # получаем первую тысячу символов
        wikimas = wikitext.split('.') # разделяем по точкам
        wikimas = wikimas[:-1] # отбрасываем все после последней точки
        wikitext_2 = ''
        for x in wikimas:       # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
            if not ('==' in x):
                if (len((x.strip())) > 3):  # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                    wikitext_2 = wikitext_2 + x + '.'
                else:
                    break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
        wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
        wikitext_2 = re.sub('\{[^\{\}]*\}', '', wikitext_2)
        return wikitext_2

    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'