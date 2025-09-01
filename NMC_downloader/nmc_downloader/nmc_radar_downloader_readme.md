# Python气象雷达图像下载脚本使用说明书

## 脚本简介

这是一个用于自动下载中国气象局（NMC）雷达拼图图像的Python脚本。它能够根据指定的时间范围，批量生成并下载对应的雷达图像文件（PNG格式），这些图像提供了全国范围的雷达数据拼接结果，对气象分析和预报有重要参考价值。

## 功能特点

- ⏰ **自动时间范围处理**：支持指定任意时间范围自动生成所有图像URL
- 🌐 **自动UTC时间计算**：默认获取当前UTC时间和25小时前的UTC时间作为范围
- 💾 **批量下载**：自动创建目录并批量下载所有图像文件
- 🔧 **容错机制**：包含异常处理，单个下载失败不影响整体任务
- 📊 **进度反馈**：实时显示下载进度和成功率统计

## 环境要求

- **Python版本**：Python 3.6或更高版本
- **操作系统**：Windows、macOS或Linux
- **依赖库**：仅需Python标准库（urllib、os、datetime），无需额外安装

## 安装步骤

1. 确保已安装Python解释器（从[Python官网](https://www.python.org/downloads/)下载安装）
2. 安装时勾选"Add Python to PATH"选项（Windows系统）
3. 将脚本保存为`.py`文件，如`nmc_radar_downloader.py`

## 使用方法

### 基本使用

运行脚本即可开始下载，默认时间范围为当前UTC时间到25小时前：

```bash
python nmc_radar_downloader.py
```

### 自定义时间范围

修改脚本底部的参数来自定义时间范围：

```python
if __name__ == "__main__":
    # 手动设置时间范围（格式：YYYYMMDDHHMM）
    start_time = "202509010000"  # 开始时间
    end_time = "202509011200"    # 结束时间
    
    # 下载图片
    download_time_range_images(start_time, end_time, save_dir="custom_images")
```

### 自定义保存目录

```python
# 将图片保存到指定目录
download_time_range_images(start_time, end_time, save_dir="my_radar_images")
```

## 参数说明

### 时间格式要求
- 必须使用**YYYYMMDDHHMM**格式
- 示例：2025年9月1日12点30分 → `202509011230`

### 函数参数

| 参数名 | 类型 | 必选 | 默认值 | 说明 |
|--------|------|------|--------|------|
| start_time | str | 是 | 25小时前 | 开始时间(YYYYMMDDHHMM) |
| end_time | str | 是 | 当前UTC时间 | 结束时间(YYYYMMDDHHMM) |
| save_dir | str | 否 | "downloaded_images" | 图片保存目录 |

## 输出结果

脚本运行后会将图像保存在指定目录中，使用以下命名格式：
```
SEVP_AOC_RDCP_SLDAS3_ECREF_ANCN_L88_PI_20250901153000000.PNG
```

其中文件名中的数字部分代表图像的时间信息（年月日时分）。

