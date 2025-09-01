
# 国家气象中心卫星云图（[天气图](https://www.nmc.cn/publish/observations/china/dm/weatherchart-h000.htm "天气图") [叠加卫星云图](https://www.nmc.cn/publish/observations/china/dm/radar-h000.htm)）下载工具

## 1. 项目简介

本工具是一个用于自动下载国家气象中心（NMC）卫星云图的Python脚本程序。它能够根据指定的时间范围，批量下载**红外卫星云图产品**，并保存到本地目录。这些气象图像可用于天气分析、科研教育或数据可视化等场景。

工具主要功能包括：
- 自动生成指定时间范围内的所有图片URL
- 批量下载卫星云图图片到本地
- 支持自定义时间范围和保存路径

## 2. 环境要求与安装

### 2.1 系统要求
- **Python版本**：Python 3.6或更高版本
- **操作系统**：Windows、macOS或Linux

### 2.2 安装步骤
1.  **安装Python解释器**
    如果系统未安装Python，请从[Python官方网站](https://www.python.org/)下载并安装。安装时建议勾选"Add Python to PATH"选项。

2.  **验证安装**
    安装完成后，在命令行中输入以下命令验证安装：
    ```bash
    python --version
    # 或
    python3 --version
    ```

3.  **获取脚本**
    将提供的Python脚本保存为本地文件，例如`nmc_weatherchartWithRadar_downloader.py`。

4.  **安装依赖**
    本工具仅使用Python标准库，无需安装第三方包。

## 3. 使用方法

### 3.1 基本使用
1.  **直接运行**：使用默认参数（下载最近7天的UTC时间图片）运行脚本：
    ```bash
    python nmc_weatherchartWithRadar_downloader.py
    ```
    图片将自动保存在项目目录下的`images_jpg`文件夹中。

2.  **自定义时间范围**：修改脚本底部的`__main__`部分：
    ```python
    if __name__ == "__main__":
        # 手动设置时间范围（格式：YYYYMMDDHH）
        start_time = "2025082000"  # 开始时间
        end_time = "2025082012"    # 结束时间
        
        # 下载图片
        download_time_range_images(start_time, end_time, save_dir="my_images")
    ```

### 3.2 参数说明
- **start_time**：开始时间，格式为`年月日时`（YYYYMMDDHH），例如`2025082000`表示2025年8月20日00时（UTC时间）
- **end_time**：结束时间，格式同上
- **save_dir**：图片保存目录名，默认为"downloaded_images"

## 4. 函数详细说明

### 4.1 generate_image_urls(start_time, end_time)
生成指定时间范围内的所有图片URL。

**参数**：
- `start_time` (str): 开始时间，格式为YYYYMMDDHH
- `end_time` (str): 结束时间，格式为YYYYMMDDHH

**返回**：
- `list`: 包含所有图片URL的列表

### 4.2 download_with_urlretrieve(url, save_path)
使用urllib.request.urlretrieve下载单个文件。

**参数**：
- `url` (str): 文件URL
- `save_path` (str): 文件保存路径

**返回**：
- `bool`: 下载成功返回True，否则返回False

### 4.3 download_time_range_images(start_time, end_time, save_dir)
下载指定时间范围内的所有图片。

**参数**：
- `start_time` (str): 开始时间，格式为YYYYMMDDHH
- `end_time` (str): 结束时间，格式为YYYYMMDDHH
- `save_dir` (str): 图片保存目录，默认为"downloaded_images"

### 4.4 get_utc_time_formatted()
获取当前UTC时间和7天前的UTC时间，格式化为YYYYMMDDHH格式。

**返回**：
- `tuple`: (当前时间字符串, 7天前时间字符串)

## 5. 使用示例

### 示例1：下载最近7天的卫星云图
```python
# 使用默认设置，下载最近7天的图片
if __name__ == "__main__":
    end_time, start_time = get_utc_time_formatted()
    download_time_range_images(start_time, end_time, save_dir="recent_images")
```

### 示例2：下载特定时间范围的图片
```python
# 下载2025年8月20日00时至2025年8月20日12时的图片
if __name__ == "__main__":
    start_time = "2025082000"  # 2025年8月20日00时
    end_time = "2025082012"    # 2025年8月20日12时
    download_time_range_images(start_time, end_time, save_dir="august_images")
```

## 6. 注意事项

1.  **时间格式**：所有时间参数必须使用**UTC时间**，格式为`YYYYMMDDHH`（年月日时）
2.  **网络连接**：确保计算机具有稳定的互联网连接，以下载图片文件
3.  **存储空间**：大量下载可能占用较大磁盘空间，请确保有足够存储容量
4.  **文件覆盖**：相同文件名的图片会被新下载的覆盖
5.  **时间范围**：请注意结束时间应晚于开始时间，否则不会下载任何图片

