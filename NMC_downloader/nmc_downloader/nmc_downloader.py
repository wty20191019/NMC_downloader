# -*- coding: gbk -*-
import sys
import nmc_radar_downloader
import nmc_weatherchartWithRadar_downloader

def main():

    
    

     
    
    if choice == "1":
        print("正在下载雷达数据...")
        nmc_radar_downloader.nmc_radar_downloader()
    elif choice == "2":
        print("正在下载天气图表与雷达数据...")
        nmc_weatherchartWithRadar_downloader.nmc_weatherchartWithRadar_downloader()
    else:
        print("无效选择")
    

if __name__ == "__main__":
     if len(sys.argv) > 1:
        choice = sys.argv[1]
        print(f"The input parameter is: {choice}")
        main()
     else:
        choice = input("请选择下载类型 (1: 雷达数据_当前UTC时间到25小时前, 2: 天气图表与雷达_下载最近7天的UTC时间图片): ")
        main()