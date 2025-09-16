# 国家气象中心(NMC)数据下载工具技术文档

## 技术说明

### 系统架构
本工具包含以下核心文件：
- **批处理启动器** (`*.bat`)
  - `start_both.bat`: 同时启动雷达和天气图下载器
  - `start_radar_downloader.bat`: 启动雷达拼图下载器
  - `start_weatherchart_downloader.bat`: 启动天气图下载器
- **Python主程序** (`nmc_downloader.py`)
  - 提供命令行交互界面
  - 调用相应下载模块
- **下载模块** (`nmc_*.py`)
  - `nmc_radar_downloader.py`: 雷达拼图下载功能
  - `nmc_weatherchartWithRadar_downloader.py`: 天气图下载功能.

### 功能模块说明

#### 1. 雷达拼图下载器 (`nmc_radar_downloader.py`)
- **数据源**: 国家气象中心雷达拼图
- **时间范围**: 下载当前UTC时间前25小时至当前时间的数据
- **时间精度**: 每分钟一张图
- **保存格式**: PNG
- **URL格式**: 
  `https://image.nmc.cn/product/{YYYY}/{MM}/{DD}/RDCP/SEVP_AOC_RDCP_SLDAS3_ECREF_ACHN_L88_PI_{YYYYMMDDHHMM}00000.PNG`

#### 2. 天气图下载器 (`nmc_weatherchartWithRadar_downloader.py`)
- **数据源**: 天气图叠加红外卫星云图
- **时间范围**: 下载当前UTC时间前7天至当前时间的数据
- **时间精度**: 每小时一张图
- **保存格式**: JPG
- **URL格式**: 
  `https://image.nmc.cn/product/{YYYY}/{MM}/{DD}/WESA/SEVP_NMC_WESA_SFER_ESPCT_ACWP_L00_P9_{YYYYMMDDHH}0000000.jpg`

#### 3. 下载核心功能
- **多线程下载**: 使用`urllib.request`实现
- **断点续传**: 自动跳过已存在文件
- **进度显示**:
  - 实时下载进度条
  - 文件大小显示
  - 总下载统计
- **时间处理**:
  - 自动计算UTC时间范围
  - 支持分钟级和小时级时间步进

### 技术特点
1. **跨平台支持**: 兼容Windows批处理和Python环境
2. **用户友好**: 提供图形进度条和中文提示
3. **高效下载**: 支持批量下载和自动续传
4. **模块化设计**: 各功能独立，便于维护扩展

## 使用说明

### 环境要求
- **操作系统**: Windows
- **Python版本**: 3.x
- **依赖库**: 
  - `urllib`
  - `datetime`
  - `time`
  - `os`

### 安装步骤
1. 确保系统已安装Python 3.x
2. 将所有文件保存到同一目录
3. 安装所需依赖（通常Python标准库已包含）

### 使用方法

#### 方式1: 批处理启动（推荐）
- **同时启动两个下载器**:
  ```bash
  start_both.bat
  ```
- **单独启动雷达拼图下载器**:
  ```bash
  start_radar_downloader.bat
  ```
- **单独启动天气图下载器**:
  ```bash
  start_weatherchart_downloader.bat
  ```

#### 方式2: Python命令行启动
```bash
python nmc_downloader.py
```
根据提示输入选项：
```
请选择下载类型 (1: 雷达拼图_前25小时数据, 2: 天气图_7天数据): 
```

#### 方式3: 带参数启动
```bash
python nmc_downloader.py 1  # 下载雷达拼图
python nmc_downloader.py 2  # 下载天气图
```

### 下载目录
- 雷达数据: `./nmc_radar_downloader/`
- 天气图数据: `./nmc_weatherchartWithRadar_downloader/`

### 使用示例
```
请选择下载类型 (1: 雷达拼图_前25小时数据, 2: 天气图_7天数据): 1

开始生成URL列表，时间范围: 202509041518 到 202509031518
共生成 1500 个图片URL

开始下载 1500 个文件

[1/1500] 开始下载: SEVP_AOC_RDCP_SLDAS3_ECREF_ACHN_L88_PI_20250903151800000.PNG
25.0% [██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 1.2MB/4.8MB

[2/1500] 文件已存在，跳过下载: SEVP_AOC_RDCP_SLDAS3_ECREF_ACHN_L88_PI_20250903151900000.PNG

...

下载完成! 成功下载: 1480, 跳过已存在: 20, 总计: 1500
总耗时: 382.45秒
```

### 注意事项
1. 下载速度取决于网络状况和服务器响应
2. 默认下载最近数据，不可指定历史时间段
3. 下载过程中不要关闭命令行窗口
4. 重复运行会自动跳过已下载文件
5. UTC时间与北京时间相差8小时（北京=UTC+8）

### 常见问题
**Q: 下载进度卡住不动怎么办？**  
A: 可能是网络问题，终止后重新运行，程序会自动续传

**Q: 如何修改保存路径？**  
A: 编辑对应的Python文件中的`save_dir`参数

**Q: 为什么有些文件下载失败？**  
A: 可能服务器上该时段数据缺失，程序会自动跳过

**Q: 下载的文件如何查看？**  
A: 所有文件按原始文件名保存，可使用图片浏览器查看