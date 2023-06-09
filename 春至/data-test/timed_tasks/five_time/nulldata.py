from common.do_mysql import DoMySql


class NullData(object):
    '''
        空数据
    '''
    def series_Required(self, env_flag=0):
        '''
            已入库系列赛某必填项为空
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = 'select s.id, s.game_id,st.series_id,s.`status`,s.league_id,s.bo,s.start_time,st.team_id,st.index from `data-center`.series as s ' \
              'join `data-center`.series_team as st on s.id=st.series_id where s.deleted=1 and s.`status` in (1,2) order by s.`status`, s.game_id;'
        datas = DoMySql().select(cnn, sql, env_flag)
        series_list = []
        for i in datas:
            if i['id'] not in series_list:
                series_list.append(i['id'])
        err_list = []
        for i in series_list:
            team_num = 0
            index = 0
            league_id = 0
            bo = 0
            start_time = 0
            status = 0
            for y in datas:
                if y['status'] == 1:
                    if i == y['id']:
                        team_num += 1
                        index += y['index']
                        league_id = y['league_id']
                        bo = y['bo']
                        start_time = y['start_time']
                        status = y['status']
                elif y['status'] == 2:
                    if i == y['id'] and y['team_id'] != 0:
                        team_num += 1
                        index += y['index']
                        league_id = y['league_id']
                        bo = y['bo']
                        start_time = y['start_time']
                        status = y['status']
            if team_num != 2:
                err_list.append(i)
            if index < 3:
                err_list.append(i)
            if league_id == 0:
                err_list.append(i)
            if bo == 0:
                err_list.append(i)
            if start_time == 0:
                err_list.append(i)
            if status == 0:
                err_list.append(i)
        # print(err_list)
        if len(err_list) != 0:
            msg = '已入库系列赛某必填项为空,存在问题的系列赛ID：' + str(err_list)
            return msg
        else:
            return ""


# if __name__ == '__main__':
#     NullData = NullData()
#     NullData.series_Required()
