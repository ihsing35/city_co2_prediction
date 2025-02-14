import os
import pandas as pd
import matplotlib.pyplot as plt


def save_to_csv(results, output_dir, city_name):
    data = []
    for scenario, emissions in results.items():
        for year, sector_emissions in emissions.items():
            row = {'scenario': scenario, 'year': year}
            row.update(sector_emissions)
            data.append(row)
    df = pd.DataFrame(data)
    # 构建 CSV 文件的绝对路径
    csv_file = os.path.join(output_dir, f'{city_name}_co2_emissions.csv')
    df.to_csv(csv_file, index=False)


def save_to_png(results, output_dir, city_name, font_settings):
    # 设置全局字体大小
    plt.rcParams.update({
        'font.size': font_settings['font_size'],
        'axes.titlesize': font_settings['axes_titlesize'],
        'axes.labelsize': font_settings['axes_labelsize'],
        'legend.fontsize': font_settings['legend_fontsize']
    })

    sectors = ['energy', 'industry', 'transport', 'building', 'agriculture', 'service']
    # 绘制各领域单独的折线图
    for sector in sectors:
        # 调整图形尺寸为原来的 2 倍
        plt.figure(figsize=(plt.rcParams['figure.figsize'][0] * 2, plt.rcParams['figure.figsize'][1] * 2))
        for scenario, emissions in results.items():
            years = sorted(emissions.keys())
            # 将排放数据转换为千吨
            sector_emissions = [emissions[year][sector] / 1000 for year in years]
            plt.plot(years, sector_emissions, label=scenario)
        plt.xlabel('Year')
        # 标注纵坐标单位为 Kilotons
        plt.ylabel(f'{sector.capitalize()} CO2 Emissions (Kilotons)')
        # 优化标题描述
        plt.title(f'{city_name} {sector.capitalize()} Sector CO2 Emissions Projection under Different Scenarios')
        # 将图例放置在图表区左上角
        plt.legend(loc='upper left')
        # 使用 tight_layout 自动调整布局，设置 pad 参数保证标题与图表区间隔
        plt.tight_layout(pad=2)
        # 构建折线图的绝对路径
        line_chart_file = os.path.join(output_dir, f'{city_name}_{sector}_emissions.png')
        plt.savefig(line_chart_file)
        plt.close()

    # 绘制不同情景下各领域排放的堆积图
    scenario_names = list(results.keys())
    for scenario in scenario_names:
        # 调整图形尺寸为原来的 2 倍
        plt.figure(figsize=(plt.rcParams['figure.figsize'][0] * 2, plt.rcParams['figure.figsize'][1] * 2))
        emissions = results[scenario]
        years = sorted(emissions.keys())
        sector_emissions_list = []
        for sector in sectors:
            # 将排放数据转换为千吨
            sector_emissions = [emissions[year][sector] / 1000 for year in years]
            sector_emissions_list.append(sector_emissions)

        bottom = [0] * len(years)
        for i, sector in enumerate(sectors):
            plt.bar(years, sector_emissions_list[i], bottom=bottom, label=sector)
            bottom = [bottom[j] + sector_emissions_list[i][j] for j in range(len(years))]

        plt.xlabel('Year')
        # 标注纵坐标单位为 Kilotons
        plt.ylabel('Total CO2 Emissions (Kilotons)')
        # 优化标题描述
        scenario_title = scenario.replace("_", " ").title()
        plt.title(f'{city_name} CO2 Emissions by Sector under {scenario_title} Scenario')
        # 将堆积图的图例放置在图表区右上角
        plt.legend(loc='upper right')
        # 使用 tight_layout 自动调整布局，设置 pad 参数保证标题与图表区间隔
        plt.tight_layout(pad=2)
        # 构建堆积图的绝对路径
        stacked_chart_file = os.path.join(output_dir, f'{city_name}_{scenario}_sector_emissions_stacked.png')
        plt.savefig(stacked_chart_file)
        plt.close()

    # 绘制城市二氧化碳排放的预测图
    plt.figure(figsize=(plt.rcParams['figure.figsize'][0] * 2, plt.rcParams['figure.figsize'][1] * 2))
    for scenario, emissions in results.items():
        years = sorted(emissions.keys())
        total_emissions = [emissions[year]['total'] / 1000 for year in years]
        plt.plot(years, total_emissions, label=scenario)
    plt.xlabel('Year')
    plt.ylabel('Total City CO2 Emissions (Kilotons)')
    # 优化标题描述
    plt.title(f'{city_name} Total City CO2 Emissions Projection under Different Scenarios')
    # 将图例放置在图表区左上角
    plt.legend(loc='upper left')
    # 使用 tight_layout 自动调整布局，设置 pad 参数保证标题与图表区间隔
    plt.tight_layout(pad=2)
    total_emissions_chart_file = os.path.join(output_dir, f'{city_name}_total_co2_emissions_projection.png')
    plt.savefig(total_emissions_chart_file)
    plt.close()
