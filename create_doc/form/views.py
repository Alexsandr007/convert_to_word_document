from django.shortcuts import render, get_object_or_404, redirect
from . import doc


def index(request):
    return render(request, 'form/index.html')


def create_document(request):
    """ Create docx """
    if request.method == 'POST':
        form = request.POST
        print(form['profession_director_IM'])
        context = {
            'name_organization': form['name'],
            'address_organization': form['address'],
            'job_title': form['profession_director_IM'],
            'director_fio': form['fio_director'],
            'IIN_code': form['INN'],
            'OKPO_code': form['OKPO'],
            'OKOGU_code': form['OKOGU'],
            'OKVD_code': form['OKVED'],
            'OKTMO': form['OKTMO'],
            'profession': form['profession'],
            'job_title_chairman': form['job_title_chairman'],
            'chairman_fio': form['chairman_fio'],
            'commission': [
                {'job_title': 'Заместитель директора по библиотечной работе ', 'fio': 'Барбоза А.В. '},
                {'job_title': 'Ведущий юрисконсульт ', 'fio': 'Данакари Р.Р. '},
                {'job_title': 'Заведующая библиотекой-филиалом № 24 ', 'fio': 'Копанева В.П. '},
            ],
            'table': [
                {
                    'profession_risks': [
                        {'danger': 'Опасность недостаточной освещенности в рабочей зоне',
                         'name': 'Обеспечение учебно-воспитательного процесса и самообразования населения путём обслуживания читателей и предоставление библиотечного фонда',
                         'dangerous event': 'Снижение остроты зрения',
                         'effects': 'Потеря трудоспособности, инвалидность, профзаболевание',
                         'terms_effect': 'Т',
                         'measures': 'Проведение регулярных замеров освещенности на рабочих местах (производственный контроль). Использование переносных светильников для освещения рабочей зоны. ',
                         'severity': '3',
                         'probability': '2',
                         'level_risk': '6',
                         'admissibility': 'Нет',
                         'comments': ' '
                         },
                        {'danger': 'Опасность недостаточной освещенности в рабочей зоне',
                         'name': 'Обеспечение учебно-воспитательного процесса и самообразования населения путём обслуживания читателей и предоставление библиотечного фонда',
                         'dangerous event': 'Снижение остроты зрения',
                         'effects': 'Потеря трудоспособности, инвалидность, профзаболевание',
                         'terms_effect': 'Т',
                         'measures': 'Проведение регулярных замеров освещенности на рабочих местах (производственный контроль). Использование переносных светильников для освещения рабочей зоны. ',
                         'severity': '3',
                         'probability': '2',
                         'level_risk': '6',
                         'admissibility': 'Нет',
                         'comments': ' '
                         },
                        {'danger': 'Опасность недостаточной освещенности в рабочей зоне',
                         'name': 'Обеспечение учебно-воспитательного процесса и самообразования населения путём обслуживания читателей и предоставление библиотечного фонда',
                         'dangerous event': 'Снижение остроты зрения',
                         'effects': 'Потеря трудоспособности, инвалидность, профзаболевание',
                         'terms_effect': 'Т',
                         'measures': 'Проведение регулярных замеров освещенности на рабочих местах (производственный контроль). Использование переносных светильников для освещения рабочей зоны. ',
                         'severity': '3',
                         'probability': '2',
                         'level_risk': '6',
                         'admissibility': 'Нет',
                         'comments': ' '
                         },
                        {'danger': 'Опасность недостаточной освещенности в рабочей зоне',
                         'name': 'Обеспечение учебно-воспитательного процесса и самообразования населения путём обслуживания читателей и предоставление библиотечного фонда',
                         'dangerous event': 'Снижение остроты зрения',
                         'effects': 'Потеря трудоспособности, инвалидность, профзаболевание',
                         'terms_effect': 'Т',
                         'measures': 'Проведение регулярных замеров освещенности на рабочих местах (производственный контроль). Использование переносных светильников для освещения рабочей зоны. ',
                         'severity': '3',
                         'probability': '2',
                         'level_risk': '6',
                         'admissibility': 'Нет',
                         'comments': ' '
                         },

                    ]
                }
            ],
        }
        doc.generate_docx(context)
    return render(request, 'form/file.html')
