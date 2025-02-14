import os
from model import CO2Model
from scenario import Scenario
from output import save_to_csv, save_to_png

def main():
    # 初始化模型和情景
    model = CO2Model()
    scenario = Scenario()

    # 获取初始条件和城市名称
    initial_population = model.initial_population
    initial_gdp_per_capita = model.initial_gdp_per_capita
    initial_energy_intensity = model.initial_energy_intensity
    initial_fossil_fuel_ratio = model.initial_fossil_fuel_ratio
    city_name = model.city_name
    font_settings = model.font_settings

    # 获取预测年份范围并生成年份列表
    years = range(model.years_start, model.years_end)

    # 预测结果
    results = {}
    scenario_names = ['base_scenario', 'low_carbon_scenario', 'zero_carbon_scenario']
    for scenario_name in scenario_names:
        population = initial_population
        gdp_per_capita = initial_gdp_per_capita
        energy_intensity = initial_energy_intensity
        fossil_fuel_ratio = initial_fossil_fuel_ratio
        scenario_results = {}
        for year in years:
            scenario_params = scenario.get_scenario_params(scenario_name, year)
            emissions = model.calculate_emissions(population, gdp_per_capita, energy_intensity, fossil_fuel_ratio)
            scenario_results[year] = emissions
            population *= (1 + scenario_params['population_growth_rate'])
            gdp_per_capita *= (1 + scenario_params['gdp_per_capita_growth_rate'])
            energy_intensity *= (1 - scenario_params['energy_intensity_decrease_rate'])
            fossil_fuel_ratio *= (1 - scenario_params['fossil_fuel_ratio_decrease_rate'])
        results[scenario_name] = scenario_results

    # 构建输出目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '../data/output')
    os.makedirs(output_dir, exist_ok=True)

    save_to_csv(results, output_dir, city_name)
    save_to_png(results, output_dir, city_name, font_settings)

if __name__ == "__main__":
    main()
