# -*- coding:utf-8 -*-
from BasicParse import MyParse
from lxml import html


class Weather(MyParse):

#today's weather. Update the parse file if we need to do it, after this parse by one day - today
    @staticmethod
    def todayweather():
        Weather.updateparse('zest.html', 'https://www.yandex.ru', 2)
        date = MyParse.parse_user_datafile_bs('zest.html', './/*[@class="home-link home-link_black_yes"]/text()')
        date[0] = u'Сейчас: '+date[0]
        return ', '.join(date)

#Take the main blocks of yandex weather
    @staticmethod
    def weatherbyweek():
        results = []
        count = 1
        text = MyParse.read_file('zest1.html')
        tree = html.fromstring(text)

        #Declare the one main block
        weather_list_lxml = tree.xpath('.//*[@class="forecast-brief forecast-brief_cols_10 i-bem"]')[0]
        items_lxml = weather_list_lxml.xpath('.//*[@class="forecast-brief__item day-anchor i-bem"]')

        #Working with child of main block and append it to dictionary
        for element in items_lxml:
            weather_day = element.xpath('.//*[@class="forecast-brief__item-day-name"]/text()')[0]
            data_day = element.xpath('.//*[@class="forecast-brief__item-day"]/text()')[0]
            forecast_brief = element.xpath('.//*[@class="forecast-brief__item-comment"]/text()')[0]
            temp_day = element.xpath('.//*[@class="forecast-brief__item-temp-day"]//text()')[0]
            temp_night = element.xpath('//div[3]/text()')[count]
            count = count.__add__(1)

            results.append({

                'day': weather_day,
                'date': data_day,
                'forecast_brief': forecast_brief,
                'temp_day': temp_day,
                'temp_night': temp_night
            })

        return results

#Return from massive of weather date info. Value can be integer or string. If we have string some as
# 'sho po pogode'- return weather by week, if we have integer - return weather by this day
    @staticmethod
    def weathebydayintheweek(value):
        mass = []
        Weather.updateparse('zest1.html', 'https://yandex.ru/pogoda/moscow', 2)

        for element in Weather.weatherbyweek():

            if value == u'что по погоде на неделю':
                day = element['date'] + ' ' + element['day'] + ', ' + element['forecast_brief'] + \
                       unicode(', днём: ', 'utf-8') + element['temp_day'] + unicode(', ночью: ', 'utf-8') \
                       + element['temp_night']
                mass.append(day)


            if element['date'].__contains__(value):
                mass = element['date'] +' '+ element['day'] + ', ' + element['forecast_brief'] + \
                    unicode(', днём: ','utf-8') + element['temp_day'] + unicode(', ночью: ','utf-8') \
                    + element['temp_night']

        return mass

if __name__ == "__main__":
    pass
    #print Weather.todayweather()
    a = Weather.weathebydayintheweek(u'что по погоде на неделю')
    print a.__len__()

