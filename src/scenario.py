import os
import yaml

class Scenario:
    def __init__(self):
        # 获取当前脚本所在的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建配置文件的绝对路径
        scenario_file = os.path.join(script_dir, '../config/scenario_settings.yaml')
        with open(scenario_file, 'r', encoding='utf-8') as f:
            self.scenarios = yaml.safe_load(f)

    def get_scenario_params(self, scenario_name, year):
        scenario = self.scenarios[scenario_name]
        # 先获取默认参数
        params = scenario.get('default', {}).copy()
        # 提取所有设置了参数的年份
        set_years = sorted([int(y) for y in scenario if y != 'default'])
        # 找到小于等于当前年份的最近设置参数的年份
        last_set_year = None
        for set_year in set_years:
            if set_year <= year:
                last_set_year = set_year
            else:
                break
        # 如果找到了最近设置参数的年份，更新参数
        if last_set_year is not None:
            # 直接使用整数类型的年份作为键
            params.update(scenario[last_set_year])
        return params
