from common.do_mysql import DoMySql
from timed_tasks.sendalarm_li import SendAlarm


class Wrong_Competition(object):
    '''
        赛制错误
    '''

    def MatchSocreBo(self, env_flag=0):
        '''
            已入库系列赛下小局比分数之和超过BO数
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''select s.id, s.game_id,st.series_id,s.bo,st.score,st.team_id from `data-center`.series as s left join `data-center`.series_team as st 
              on s.id=st.series_id where s.deleted=1 and s.start_time >= (unix_timestamp() - 3600*24*7) and s.`status`=3 and s.game_id not in (13,14) order by s.game_id;
              '''
        datas = DoMySql().select(cnn, sql, env_flag)
        series_list = []
        for i in datas:
            if i['id'] not in series_list:
                series_list.append(i['id'])
        new_list = []
        for y in series_list:
            series_id = 0
            score = 0
            bo = 0
            game_id = 0
            map_ = {}
            for i in datas:
                if y == i['id']:
                    series_id = y
                    score += i['score']
                    bo = i['bo']
                    game_id = i['game_id']
            map_['series_id'] = series_id
            map_['score'] = score
            map_['bo'] = bo
            map_['game_id'] = game_id
            new_list.append(map_)
        err_series = []
        for i in new_list:
            if i['score'] > i['bo']:
                err_series.append(i['series_id'])
        err_msg = ''
        if len(err_series) != 0:
            err_msg = err_msg + '已入库系列赛下小局比分数之和超过BO数,存在问题的系列赛ID：' + str(err_series)
        if len(err_msg) != 0:
            print(err_msg)
            return err_msg
        else:
            return ""

#
if __name__ == '__main__':
    w = Wrong_Competition()
    w.MatchSocreBo(1)

