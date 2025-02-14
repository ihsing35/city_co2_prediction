import os
import yaml

class CO2Model:
    def __init__(self):
        # 获取当前脚本所在的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建配置文件的绝对路径
        params_file = os.path.join(script_dir, '../config/model_params.yaml')
        with open(params_file, 'r', encoding='utf-8') as f:
            self.params = yaml.safe_load(f)
        self.initial_population = self.params['initial_population']
        self.initial_gdp_per_capita = self.params['initial_gdp_per_capita']
        self.initial_energy_intensity = self.params['initial_energy_intensity']
        self.initial_fossil_fuel_ratio = self.params['initial_fossil_fuel_ratio']
        self.city_name = self.params['city_name']
        self.font_settings = self.params['font_settings']
        # 读取预测年份范围
        self.years_start = self.params['years']['start']
        self.years_end = self.params['years']['end']

    def calculate_emissions(self, population, gdp_per_capita, energy_intensity, fossil_fuel_ratio):
        # 计算各领域碳排放
        energy_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['energy_emission_factor']
        industry_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['industry_emission_factor']
        transport_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['transport_emission_factor']
        building_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['building_emission_factor']
        agriculture_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['agriculture_emission_factor']
        service_emissions = population * gdp_per_capita * energy_intensity * fossil_fuel_ratio * self.params['service_emission_factor']

        total_emissions = energy_emissions + industry_emissions + transport_emissions + building_emissions + agriculture_emissions + service_emissions
        return {
            'energy': energy_emissions,
            'industry': industry_emissions,
            'transport': transport_emissions,
            'building': building_emissions,
            'agriculture': agriculture_emissions,
            'service': service_emissions,
            'total': total_emissions
        }
