
import urllib.request
import os
from datetime import datetime, timedelta, timezone
import time
from concurrent.futures import ThreadPoolExecutor, as_completed  
import threading  


# 全局变量和锁，用于线程安全的计数
global_counter = {'success': 0, 'skipped': 0, 'failed': 0}
counter_lock = threading.Lock()

# 全局变量
total_files = 0
processed_files = 0
progress_lock = threading.Lock()
start_time_total = 0



def generate_image_urls(start_time, end_time):
	"""
	生成指定时间范围内的所有图片URL
	
	Args:
		start_time (str): 开始时间
		end_time (str): 结束时间
	
	Returns:
		list: 包含所有图片URL的列表
	"""
	urls = []
	
	# 解析时间参数
	start_datetime = datetime.strptime(start_time, "%Y%m%d%H%M")
	end_datetime = datetime.strptime(end_time, "%Y%m%d%H%M")
	
	current_datetime = start_datetime
	while current_datetime <= end_datetime:
		# 格式化日期部分（URL路径）
		date_path = current_datetime.strftime("%Y/%m/%d")
		# 格式化文件名部分
		filename_time = current_datetime.strftime("%Y%m%d%H%M")
		
		# 构建URL   
		#天气图叠加红外卫星云图 https://image.nmc.cn/product/2025/08/31/WESA/SEVP_NMC_WESA_SFER_ESPCT_ACWP_L00_P9_20250831000000000.jpg
		#全国逐时气温           https://image.nmc.cn/product/2025/09/01/STFC/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_20250901130000000.jpg
		#雷达拼图               https://image.nmc.cn/product/2025/09/01/RDCP/SEVP_AOC_RDCP_SLDAS3_ECREF_ACHN_L88_PI_20250901145400000.PNG

		# https://image.nmc.cn/product/2025/09/01/RDCP/SEVP_AOC_RDCP_SLDAS3_ECREF_ANCN_L88_PI_20250901153000000.PNG

		url = f"https://image.nmc.cn/product/{date_path}/RDCP/SEVP_AOC_RDCP_SLDAS3_ECREF_ACHN_L88_PI_{filename_time}00000.PNG"

		urls.append(url)
		
		# 步进等级 (增加一小时/分钟) weeks=  days=   hours= ​	minutes=  seconds=  microseconds= 
		current_datetime += timedelta(minutes=1)


	
	return urls







def download_with_urlretrieve(url, save_path):
    """
    使用urllib.request.urlretrieve下载文件，并显示进度条
    
    Args:
        url (str): 文件URL
        save_path (str): 保存路径
    
    Returns:
        bool: 下载是否成功
    """
    # 检查文件是否已经存在
    if os.path.exists(save_path):
        with counter_lock:  # 使用锁保护全局变量
            global_counter['skipped'] += 1
        print(f"文件已存在，跳过下载: {os.path.basename(save_path)}")
        return True
        
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 定义进度回调函数
        def progress_callback(block_num, block_size, total_size):
            if total_size <= 0:
                return
                
            downloaded = block_num * block_size
            percent = min(downloaded / total_size * 100, 100)
            
            # 创建进度条显示
            bar_length = 40
            filled_length = int(bar_length * percent / 100)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            
            # 显示进度信息
            status = f"{percent:.1f}% [{bar}] {downloaded/(1024 * 1024):.1f}MB/{total_size/(1024 * 1024):.1f}MB"
            print(f"\r{os.path.basename(save_path)}: {status}", end='')
            
            # 如果下载完成，换行
            if percent >= 100:
                print()
        
        # 下载文件并显示进度
        urllib.request.urlretrieve(url, save_path, reporthook=progress_callback)
        
        with counter_lock:  # 使用锁保护全局变量
            global_counter['success'] += 1
        return True
    except Exception as e:
        with counter_lock:  # 使用锁保护全局变量
            global_counter['failed'] += 1
        print(f"\n下载失败 {os.path.basename(save_path)}: {e}")
        return False






def download_time_range_images(start_time, end_time, save_dir="downloaded_images", max_workers=5):
    """
    下载指定时间范围内的所有图片，使用多线程并行下载
    
    Args:
        start_time (str): 开始时间，格式为YYYYMMDDHHMM
        end_time (str): 结束时间，格式为YYYYMMDDHHMM
        save_dir (str): 图片保存目录
        max_workers (int): 最大线程数，控制并发度
    """
    # 重置全局计数器
    global global_counter, total_files, processed_files, start_time_total
    global_counter = {'success': 0, 'skipped': 0, 'failed': 0}
    processed_files = 0
    
    print(f"开始生成URL列表，时间范围: {start_time} 到 {end_time}")
    urls = generate_image_urls(start_time, end_time)
    total_files = len(urls)
    
    print(f"共生成 {total_files} 个图片URL")
    
    # 创建保存目录
    os.makedirs(save_dir, exist_ok=True)
    
    # 显示总体进度
    print(f"\n开始使用 {max_workers} 个线程下载 {total_files} 个文件")
    start_time_total = time.time()
    
    # 使用ThreadPoolExecutor进行并行下载
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 创建任务字典，将Future对象与URL关联
        future_to_url = {}
        for url in urls:
            filename = url.split('/')[-1]
            save_path = os.path.join(save_dir, filename)
            # 提交下载任务到线程池
            future = executor.submit(download_with_urlretrieve, url, save_path)
            future_to_url[future] = url
        
        # 处理完成的任务，获取结果或异常
        for future in as_completed(future_to_url):
            try:
                future.result()  # 获取结果，如果任务抛出异常，这里会重新抛出
            except Exception as exc:
                # 异常已在download_with_urlretrieve中处理，这里可选择记录日志
                pass
            
            # 更新已处理文件计数并显示总进度
            with progress_lock:
                processed_files += 1
                show_overall_progress()
    
    # 计算总耗时
    end_time_total = time.time()
    total_time = end_time_total - start_time_total
    
    print(f"\n下载完成! 成功: {global_counter['success']}, 跳过: {global_counter['skipped']}, 失败: {global_counter['failed']}, 总计: {total_files}")
    print(f"总耗时: {total_time:.2f}秒")






def show_overall_progress():
    """显示总体下载进度和状态"""
    elapsed_time = time.time() - start_time_total
    progress_percent = (processed_files / total_files * 100) if total_files > 0 else 0
    
    # 计算下载速度
    download_speed = processed_files / elapsed_time if elapsed_time > 0 else 0
    
    # 计算预估剩余时间
    remaining_files = total_files - processed_files
    eta = remaining_files / download_speed if download_speed > 0 else 0
    
    # 创建总进度条
    bar_length = 30
    filled_length = int(bar_length * progress_percent / 100)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    # 显示总体进度信息
    status = f"总进度: {progress_percent:.1f}% [{bar}] {processed_files}/{total_files}"
    status += f" | 成功: {global_counter['success']} 跳过: {global_counter['skipped']} 失败: {global_counter['failed']}"
    status += f" | 速度: {download_speed:.1f}文件/秒 | ETA: {eta:.1f}秒"
    
    print(f"\r{status}", end='')
    
    # 如果下载完成，换行
    if processed_files >= total_files:
        print()






def get_utc_time_formatted():
    """
    获取当前UTC时间和 N 天前的UTC时间，格式为YYYYMMDDHH
    Returns:
        tuple: (当前时间字符串, N天前时间字符串)

    """

    # 获取当前UTC时间
    current_utc_time = datetime.now(timezone.utc)
    
    # 计算 N 天前的UTC时间
    # 步进等级 (减少一小时/分钟) weeks=  days=   hours= ​	minutes=  seconds=  microseconds= 
    seven_days_ago_utc = current_utc_time - timedelta(hours=25)
    
    # 格式化为YYYYMMDDHHMM
    current_formatted = current_utc_time.strftime("%Y%m%d%H%M")
    seven_days_ago_formatted = seven_days_ago_utc.strftime("%Y%m%d%H%M")
    
    return current_formatted, seven_days_ago_formatted





def nmc_radar_downloader():

	end_time,start_time = get_utc_time_formatted()

	download_time_range_images(start_time, end_time, save_dir="nmc_radar_downloader")
	#__________________________start_time__end_time____________保存目录名

	return 0


# if __name__ == "__main__":

# 	# 设置时间范围
# 	end_time,start_time = get_utc_time_formatted()
  
	
# 	# 下载图片
# 	download_time_range_images(start_time, end_time, save_dir="images_jpg")
# 	#__________________________start_time__end_time____________保存目录名


