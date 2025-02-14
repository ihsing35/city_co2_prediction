# 城市二氧化碳排放预测模型

## 一、项目概述
本项目旨在对城市的二氧化碳排放进行预测，通过设置不同的情景参数，模拟在不同发展情况下城市各领域（能源、工业、交通、建筑、农业、服务业）的二氧化碳排放情况。项目使用 Python 语言编写，利用系统动力学模型进行预测，并将结果以 CSV 文件和 PNG 图片的形式输出。

## 二、安装部署

### 2.1 环境要求
- Python 3.x
- 所需 Python 库：`pandas`、`matplotlib`、`PyYAML`

### 2.2 安装步骤
1. **克隆项目代码**：
   如果你使用的是 Git，可以通过以下命令克隆项目到本地：
   ```bash
   git clone https://github.com/ihsing35/city_co2_prediction
   cd city_co2_prediction
   ```
2. **创建虚拟环境（可选但推荐）**：
   在项目目录下创建并激活虚拟环境，以避免不同项目之间的依赖冲突。
   - **Windows**：
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/MacOS**：
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **安装依赖库**：
   使用 `pip` 安装项目所需的依赖库：
   ```bash
   pip install pandas matplotlib PyYAML
   ```

### 2.3 运行项目
在项目根目录下运行 `run_prediction.py` 脚本：
```bash
python run_prediction.py
```
运行成功后，预测结果将保存到 `data/output` 目录下，包括 CSV 文件和 PNG 图片。

## 三、文件结构
```plaintext
city_co2_prediction/
│
├── .git/              # Git 仓库目录
├── .gitignore         # 忽略文件配置
├── config/
│   ├── model_params.yaml  # 模型参数配置文件
│   └── scenario_settings.yaml  # 情景设置配置文件
├── data/
│   └── output/        # 输出结果目录
├── src/
│   ├── model.py       # 二氧化碳排放计算模型
│   ├── scenario.py    # 情景参数获取模块
│   ├── output.py      # 结果输出模块，生成 CSV 和 PNG 文件
│   └── main.py        # 主程序入口
├── run_prediction.py  # 根目录运行脚本
└── README.md          # 项目说明文档
```

## 四、配置文件说明

### 4.1 `config/model_params.yaml`
该文件包含了系统动力学模型的参数、初始条件、城市名称、图片全局文字设置以及预测年份范围等信息。示例内容如下：
```yaml
# 系统动力学模型参数
population_growth_rate: 0.01
gdp_per_capita_growth_rate: 0.03
energy_intensity_decrease_rate: 0.02
fossil_fuel_ratio_decrease_rate: 0.01

# 各领域碳排放系数
energy_emission_factor: 0.8
industry_emission_factor: 0.6
transport_emission_factor: 0.7
building_emission_factor: 0.5
agriculture_emission_factor: 0.3
service_emission_factor: 0.4

# 初始条件
initial_population: 1000000
initial_gdp_per_capita: 50000
initial_energy_intensity: 0.5
initial_fossil_fuel_ratio: 0.8

# 城市名称
city_name: "示例城市"

# 图片全局文字设置
font_settings:
  font_size: 14
  axes_titlesize: 18
  axes_labelsize: 16
  legend_fontsize: 14

# 预测年份范围
years:
  start: 2025
  end: 2051
```

### 4.2 `config/scenario_settings.yaml`
该文件用于设置不同情景下的参数，每个情景可以有默认参数，也可以为特定年份设置参数。示例内容如下：
```yaml
# 情景设置
base_scenario:
  default:
    population_growth_rate: 0.01
    gdp_per_capita_growth_rate: 0.03
    energy_intensity_decrease_rate: 0.02
    fossil_fuel_ratio_decrease_rate: 0.01
  2030:
    population_growth_rate: 0.015
    gdp_per_capita_growth_rate: 0.035
  2037:
    energy_intensity_decrease_rate: 0.03

low_carbon_scenario:
  default:
    population_growth_rate: 0.005
    gdp_per_capita_growth_rate: 0.02
    energy_intensity_decrease_rate: 0.03
    fossil_fuel_ratio_decrease_rate: 0.02
  2035:
    energy_intensity_decrease_rate: 0.04

zero_carbon_scenario:
  default:
    population_growth_rate: 0
    gdp_per_capita_growth_rate: 0.01
    energy_intensity_decrease_rate: 0.05
    fossil_fuel_ratio_decrease_rate: 0.05
  2040:
    fossil_fuel_ratio_decrease_rate: 0.06
```

## 五、公式算法解释

### 5.1 二氧化碳排放计算
在 `src/model.py` 中，每个领域的二氧化碳排放量计算公式如下：
- **能源领域**：
  \[E_{energy} = P \times GDP_{pc} \times EI \times FFR \times EF_{energy}\]
  其中，\(E_{energy}\) 是能源领域的二氧化碳排放量，\(P\) 是人口数量，\(GDP_{pc}\) 是人均 GDP，\(EI\) 是能源强度，\(FFR\) 是化石燃料比例，\(EF_{energy}\) 是能源领域的碳排放系数。
- **工业领域**：
  \[E_{industry} = P \times GDP_{pc} \times EI \times FFR \times EF_{industry}\]
  其中，\(E_{industry}\) 是工业领域的二氧化碳排放量，\(EF_{industry}\) 是工业领域的碳排放系数。
- **交通领域**：
  \[E_{transport} = P \times GDP_{pc} \times EI \times FFR \times EF_{transport}\]
  其中，\(E_{transport}\) 是交通领域的二氧化碳排放量，\(EF_{transport}\) 是交通领域的碳排放系数。
- **建筑领域**：
  \[E_{building} = P \times GDP_{pc} \times EI \times FFR \times EF_{building}\]
  其中，\(E_{building}\) 是建筑领域的二氧化碳排放量，\(EF_{building}\) 是建筑领域的碳排放系数。
- **农业领域**：
  \[E_{agriculture} = P \times GDP_{pc} \times EI \times FFR \times EF_{agriculture}\]
  其中，\(E_{agriculture}\) 是农业领域的二氧化碳排放量，\(EF_{agriculture}\) 是农业领域的碳排放系数。
- **服务领域**：
  \[E_{service} = P \times GDP_{pc} \times EI \times FFR \times EF_{service}\]
  其中，\(E_{service}\) 是服务领域的二氧化碳排放量，\(EF_{service}\) 是服务领域的碳排放系数。
- **总排放量**：
  \[E_{total} = E_{energy} + E_{industry} + E_{transport} + E_{building} + E_{agriculture} + E_{service}\]

### 5.2 参数更新
在每个预测年份，参数会根据情景设置进行更新：
- **人口数量更新**：
  \[P_{t+1} = P_{t} \times (1 + r_{pop})\]
  其中，\(P_{t}\) 是第 \(t\) 年的人口数量，\(P_{t+1}\) 是第 \(t + 1\) 年的人口数量，\(r_{pop}\) 是人口增长率。
- **人均 GDP 更新**：
  \[GDP_{pc_{t+1}} = GDP_{pc_{t}} \times (1 + r_{gdp})\]
  其中，\(GDP_{pc_{t}}\) 是第 \(t\) 年的人均 GDP，\(GDP_{pc_{t+1}}\) 是第 \(t + 1\) 年的人均 GDP，\(r_{gdp}\) 是人均 GDP 增长率。
- **能源强度更新**：
  \[EI_{t+1} = EI_{t} \times (1 - r_{ei})\]
  其中，\(EI_{t}\) 是第 \(t\) 年的能源强度，\(EI_{t+1}\) 是第 \(t + 1\) 年的能源强度，\(r_{ei}\) 是能源强度下降率。
- **化石燃料比例更新**：
  \[FFR_{t+1} = FFR_{t} \times (1 - r_{ffr})\]
  其中，\(FFR_{t}\) 是第 \(t\) 年的化石燃料比例，\(FFR_{t+1}\) 是第 \(t + 1\) 年的化石燃料比例，\(r_{ffr}\) 是化石燃料比例下降率。

## 六、输出结果说明
### 6.1 CSV 文件
运行项目后，会在 `data/output` 目录下生成一个以城市名称命名的 CSV 文件，如 `示例城市_co2_emissions.csv`。该文件包含了不同情景下各年份各领域的二氧化碳排放量数据。

### 6.2 PNG 图片
同时，还会生成一系列 PNG 图片，包括：
- 各领域单独的折线图：展示不同情景下每个领域的二氧化碳排放随时间的变化趋势。
- 不同情景下各领域排放的堆积图：展示在特定情景下各领域二氧化碳排放的占比情况。
- 城市二氧化碳排放的预测图：展示不同情景下城市整体二氧化碳排放随时间的变化趋势。

## 七、注意事项
- 确保配置文件中的参数设置合理，否则可能会导致预测结果不符合实际情况。
- 若需要修改预测年份范围或其他参数，可直接在 `config/model_params.yaml` 和 `config/scenario_settings.yaml` 文件中进行修改。
- 运行项目前，请确保虚拟环境已激活（如果使用了虚拟环境），并且所需的依赖库已正确安装。
