# -*- coding: gbk -*-
import sys
import nmc_radar_downloader
import nmc_weatherchartWithRadar_downloader

def main():

    
    

     
    
    if choice == "1":
        print("���������״�����...")
        nmc_radar_downloader.nmc_radar_downloader()
    elif choice == "2":
        print("������������ͼ�����״�����...")
        nmc_weatherchartWithRadar_downloader.nmc_weatherchartWithRadar_downloader()
    else:
        print("��Чѡ��")
    

if __name__ == "__main__":
     if len(sys.argv) > 1:
        choice = sys.argv[1]
        print(f"The input parameter is: {choice}")
        main()
     else:
        choice = input("��ѡ���������� (1: �״�����_��ǰUTCʱ�䵽25Сʱǰ, 2: ����ͼ�����״�_�������7���UTCʱ��ͼƬ): ")
        main()