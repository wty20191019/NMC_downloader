# NMC_downloader
国家气象中心(NMC)图片下载器_NMC_downloader

# 国家气象中心(NMC)图片下载器使用说明

## 一、程序功能
1. **雷达拼图下载**：下载最近25小时内的全国雷达拼图
2. **天气图+卫星云图下载**：下载最近7天的天气图叠加红外卫星云图

## 二、文件说明
```
nmc_downloader/ 
├── nmc_downloader.py       # 主程序
├── download_radar.bat      # 雷达拼图下载脚本
├── download_weather.bat    # 天气图下载脚本
├── nmc_radar_downloader.py       # 雷达下载模块
└── nmc_weatherchartWithRadar_downloader.py  # 天气图下载模块
```

## 三、使用方式

##### 方法1：批处理文件（推荐）
程序使用Python标准库开发，无需额外安装依赖包。首次使用建议以管理员身份运行批处理文件。
- **下载雷达拼图**：双击 `download_radar.bat`
- **下载天气图**：双击 `download_weather.bat`

##### 方法2：命令行执行
```bash
# 下载雷达拼图
python nmc_downloader.py 1

# 下载天气图
python nmc_downloader.py 2
```

##### 方法3：交互式选择
直接运行主程序后根据提示选择：
```bash
python nmc_downloader.py
```
将显示：
```
请选择选项 (1: 雷达拼图_前25小时, 2: 天气图+卫星云图_7天):
```

## 四、下载内容说明

| 功能 | 时间范围 | 时间间隔 | 图片格式 | 保存目录 |
|------|----------|----------|----------|----------|
| 雷达拼图 | 最近25小时 | 每分钟 | PNG | `nmc_radar_downloader/` |
| 天气图+卫星云图 | 最近7天 | 每小时 | JPG | `nmc_weatherchartWithRadar_downloader/` |

## 五、技术参数
1. **时间基准**：使用UTC时间（世界协调时）
2. **图片来源**：国家气象中心官方服务器
3. **命名规则**：
   - 雷达：`SEVP_AOC_RDCP_SLDAS3_ECREF_ANCN_L88_PI_时间戳.PNG`
   - 天气图：`SEVP_NMC_WESA_SFER_ESPCT_ACWP_L00_P9_时间戳.jpg`

## 六、注意事项
1. 需保持网络连接正常
2. 雷达拼图下载量较大（约1500张/25小时）
3. 程序会自动创建保存目录
4. 下载失败时会显示错误信息但继续下载其他文件

## 七、自定义修改
如需修改时间范围，可编辑对应模块中的：
```python
# 雷达模块（nmc_radar_downloader.py）
current_datetime += timedelta(minutes=1)  # 时间间隔
timedelta(hours=25)                      # 时间范围

# 天气图模块
current_datetime += timedelta(hours=1)   # 时间间隔
timedelta(days=7)                       # 时间范围
```

> 提示：程序使用Python标准库开发，无需额外安装依赖包。首次使用建议以管理员身份运行批处理文件。
版权声明

## 版权声明

本工具仅限个人学习研究使用，请遵守国家气象中心数据使用规定。图片版权归属中国气象局所有。
