class Report:
    
    def increase_plain(self, data, indicator_key, date_key, date=2019, measure='万亿'):
        # 读取数据
        indi_list = data[indicator_key]
        date_list = data[date_key]
        # 确定日期的索引
        date_index = date_list.index(date)
        # 计算增量增速
        indi_now = indi_list[date_index] # 当前指标的数据
        indi_inc = indi_now - indi_list[date_index+1] # 增量
        indi_rate = indi_inc / indi_list[date_index+1] # 增速
        indi_judge = ""
        if indi_inc > 0:
            indi_judge = "增长"
        elif indi_inc < 0:
            indi_judge = "下降"
        else:
            indi_judge = "变化"
        output_text = f"{indicator_key}在{date}年为{indi_now}{measure}，\
比上年{indi_judge}{abs(indi_inc)}{measure}，\
比上年{indi_judge}{'%.2f' % (abs(indi_rate)*100)}%"
        return output_text
    
    def cross_plain(self, data, parent_key, date_key, date=2019):
        # 读取数据
        parent_list = data[parent_key]
        date_list = data[date_key]
        # 确定日期的索引
        date_index = date_list.index(date)
        # 计算占比
        output_text = ""
        for child_key in data:
            if child_key in [parent_key, date_key]:
                continue
            tmp_rate = data[child_key][date_index] / data[parent_key][date_index] * 100
            tmp_text = f"{child_key}占{parent_key}{'%.2f' % tmp_rate}%"
            if output_text: # 如果有值
                output_text = output_text + "，" + tmp_text
            else: # 如果没有值
                output_text = f'{date}年，' + tmp_text
        return output_text   