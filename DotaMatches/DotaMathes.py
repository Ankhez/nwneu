# -*- coding:utf-8 -*-
from Weather.BasicParse import MyParse
from pyparsing import *


class Matches(MyParse):

    global l
    l = []


    @staticmethod
    def except_for_empty_values(path, error):
        try:
            name = path[0]
        except error:
            name = ''
        return name

    @staticmethod
    def nowgames():
        results = []
        the_main_box = Matches.parse_user_datafile_bs('dotamatches.html', './/*[@class="matches table table-striped table-hover"]//tr')
        for item in the_main_box:

            commands_vs = item.xpath('.//*[@class = "mlink"]/@title')[0]
            bet_for_first_command = Matches.except_for_empty_values(item.xpath('.//*[@class="bet-percentage bet1"]/text()'), IndexError)
            bet_for_second_command = Matches.except_for_empty_values(item.xpath('.//*[@class="bet-percentage bet2"]/text()'), IndexError)
            the_data_time = Matches.except_for_empty_values(item.xpath('.//td[3]/span[2]/span/text()'), IndexError)
            name_of_tournament = item.xpath('.//*[@class="ta odtip"]/@title')[0]

            results.append({

                'commands': commands_vs,
                'bet': bet_for_first_command+bet_for_second_command,
                'data_time': the_data_time,
                'tour_name': name_of_tournament
            })


        for element in results:
            l.append(element.get('commands') + u'    /Ставки на команды: ' + element.get('bet') + u'  / Время: '+ element.get('data_time')\
                  + u' /Название турнира: ' + element.get('tour_name'))
        return l

    @staticmethod
    def parsewithpagination():

        count = int(Matches.get_count_of_pagination())
        for i in range(1, count.__add__(1)):

            dct = {

                'rid': 'dota2',
                'ajax': 'block_matches_current',
                'data[s]': i,
                'data[type]': 'gg'

            }

            MyParse.checkthepagination('dotamatches.html','http://game-tournaments.com/dota-2', **dct)
            Matches.nowgames()
        return l

    @staticmethod
    def get_count_of_pagination():

        s = Matches.parse_user_datafile_bs('dotamatches.html', './/*[@class="pager-count"]/text()')
        s = u' '.join(s).encode('utf-8').strip()
        c = 'Пйцукенгшщзхъёфывапролджэячсмитьбю'
        module_word = ZeroOrMore(Suppress(Word(c)) | Word(nums))
        result = module_word.parseString(s)

        count = int(result[result.__len__().__sub__(1)])
        return round(count.__float__().__div__(20) + 0.45)


if __name__ == '__main__':
    pass




