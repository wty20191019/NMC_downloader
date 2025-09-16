@echo off
rem 使用start命令启动第一个批处理文件，并指定窗口标题为"Radar Downloader"
start "Radar Downloader" nmc_radar_downloader.bat

rem 使用start命令启动第二个批处理文件，并指定窗口标题为"WeatherChart Downloader"
start "WeatherChart Downloader" nmc_weatherchartWithRadar_downloader.bat
