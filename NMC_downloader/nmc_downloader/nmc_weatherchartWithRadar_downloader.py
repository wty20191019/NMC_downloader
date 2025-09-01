
import urllib.request
import os
from datetime import datetime, timedelta, timezone

def generate_image_urls(start_time, end_time):
	"""
	生成指定时间范围内的所有图片URL
	
	Args:
		start_time (str): 开始时间，格式为YYYYMMDDHH
		end_time (str): 结束时间，格式为YYYYMMDDHH
	
	Returns:
		list: 包含所有图片URL的列表
	"""
	urls = []
	
	# 解析时间参数
	start_datetime = datetime.strptime(start_time, "%Y%m%d%H")
	end_datetime = datetime.strptime(end_time, "%Y%m%d%H")
	
	current_datetime = start_datetime
	while current_datetime <= end_datetime:
		# 格式化日期部分（URL路径）
		date_path = current_datetime.strftime("%Y/%m/%d")
		# 格式化文件名部分
		filename_time = current_datetime.strftime("%Y%m%d%H")
		
		# 构建URL   
		#天气图叠加红外卫星云图 https://image.nmc.cn/product/2025/08/31/WESA/SEVP_NMC_WESA_SFER_ESPCT_ACWP_L00_P9_20250831000000000.jpg
		


		url = f"https://image.nmc.cn/product/{date_path}/WESA/SEVP_NMC_WESA_SFER_ESPCT_ACWP_L00_P9_{filename_time}0000000.jpg"

		urls.append(url)
		
		# 步进等级 (增加一小时) weeks=  days=   hours= ​	minutes=  seconds=  microseconds= 
		current_datetime += timedelta(hours=1)


	
	return urls

def download_with_urlretrieve(url, save_path):
	"""
	使用urllib.request.urlretrieve下载文件[1,4](@ref)
	
	Args:
		url (str): 文件URL
		save_path (str): 保存路径
	
	Returns:
		bool: 下载是否成功
	"""
	try:
		# 确保目录存在
		os.makedirs(os.path.dirname(save_path), exist_ok=True)
		
		# 下载文件
		urllib.request.urlretrieve(url, save_path)
		print(f"下载成功: {save_path}")
		return True
	except Exception as e:
		print(f"下载失败 {url}: {e}")
		return False

def download_time_range_images(start_time, end_time, save_dir="downloaded_images"):
	"""
	下载指定时间范围内的所有图片
	
	Args:
		start_time (str): 开始时间，格式为YYYYMMDDHH
		end_time (str): 结束时间，格式为YYYYMMDDHH
		save_dir (str): 图片保存目录
	"""
	print(f"开始生成URL列表，时间范围: {start_time} 到 {end_time}")
	urls = generate_image_urls(start_time, end_time)
	
	print(f"共生成 {len(urls)} 个图片URL")
	
	# 下载所有图片
	successful_downloads = 0
	for url in urls:
		# 从URL中提取文件名
		filename = url.split('/')[-1]
		save_path = os.path.join(save_dir, filename)
		
		if download_with_urlretrieve(url, save_path):
			successful_downloads += 1
	
	print(f"下载完成! 成功下载 {successful_downloads}/{len(urls)} 张图片")

def get_utc_time_formatted():
    """
    获取当前UTC时间和7天前的UTC时间，格式为YYYYMMDDHH
    Returns:
        tuple: (当前时间字符串, 7天前时间字符串)

    """

    # 获取当前UTC时间
    current_utc_time = datetime.now(timezone.utc)
    
    # 计算 N 天前的UTC时间
    seven_days_ago_utc = current_utc_time - timedelta(days=7)
    
    # 格式化为YYYYMMDDHH
    current_formatted = current_utc_time.strftime("%Y%m%d%H")
    seven_days_ago_formatted = seven_days_ago_utc.strftime("%Y%m%d%H")
    
    return current_formatted, seven_days_ago_formatted


def nmc_weatherchartWithRadar_downloader():
	# 设置时间范围
	end_time,start_time = get_utc_time_formatted()

	
	# 下载图片
	download_time_range_images(start_time, end_time, save_dir="nmc_weatherchartWithRadar_downloader")
	#__________________________start_time__end_time____________保存目录名


	return 0





# if __name__ == "__main__":

# 	# 设置时间范围
# 	end_time,start_time = get_utc_time_formatted()
  
	
# 	# 下载图片
# 	download_time_range_images(start_time, end_time, save_dir="images_jpg")
# 	#__________________________start_time__end_time____________保存目录名


