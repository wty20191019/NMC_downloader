
# ������������������ͼ��[����ͼ](https://www.nmc.cn/publish/observations/china/dm/weatherchart-h000.htm "����ͼ") [����������ͼ](https://www.nmc.cn/publish/observations/china/dm/radar-h000.htm)�����ع���

## 1. ��Ŀ���

��������һ�������Զ����ع����������ģ�NMC��������ͼ��Python�ű��������ܹ�����ָ����ʱ�䷶Χ����������**����������ͼ��Ʒ**�������浽����Ŀ¼����Щ����ͼ��������������������н��������ݿ��ӻ��ȳ�����

������Ҫ���ܰ�����
- �Զ�����ָ��ʱ�䷶Χ�ڵ�����ͼƬURL
- ��������������ͼͼƬ������
- ֧���Զ���ʱ�䷶Χ�ͱ���·��

## 2. ����Ҫ���밲װ

### 2.1 ϵͳҪ��
- **Python�汾**��Python 3.6����߰汾
- **����ϵͳ**��Windows��macOS��Linux

### 2.2 ��װ����
1.  **��װPython������**
    ���ϵͳδ��װPython�����[Python�ٷ���վ](https://www.python.org/)���ز���װ����װʱ���鹴ѡ"Add Python to PATH"ѡ�

2.  **��֤��װ**
    ��װ��ɺ�������������������������֤��װ��
    ```bash
    python --version
    # ��
    python3 --version
    ```

3.  **��ȡ�ű�**
    ���ṩ��Python�ű�����Ϊ�����ļ�������`nmc_weatherchartWithRadar_downloader.py`��

4.  **��װ����**
    �����߽�ʹ��Python��׼�⣬���谲װ����������

## 3. ʹ�÷���

### 3.1 ����ʹ��
1.  **ֱ������**��ʹ��Ĭ�ϲ������������7���UTCʱ��ͼƬ�����нű���
    ```bash
    python nmc_weatherchartWithRadar_downloader.py
    ```
    ͼƬ���Զ���������ĿĿ¼�µ�`images_jpg`�ļ����С�

2.  **�Զ���ʱ�䷶Χ**���޸Ľű��ײ���`__main__`���֣�
    ```python
    if __name__ == "__main__":
        # �ֶ�����ʱ�䷶Χ����ʽ��YYYYMMDDHH��
        start_time = "2025082000"  # ��ʼʱ��
        end_time = "2025082012"    # ����ʱ��
        
        # ����ͼƬ
        download_time_range_images(start_time, end_time, save_dir="my_images")
    ```

### 3.2 ����˵��
- **start_time**����ʼʱ�䣬��ʽΪ`������ʱ`��YYYYMMDDHH��������`2025082000`��ʾ2025��8��20��00ʱ��UTCʱ�䣩
- **end_time**������ʱ�䣬��ʽͬ��
- **save_dir**��ͼƬ����Ŀ¼����Ĭ��Ϊ"downloaded_images"

## 4. ������ϸ˵��

### 4.1 generate_image_urls(start_time, end_time)
����ָ��ʱ�䷶Χ�ڵ�����ͼƬURL��

**����**��
- `start_time` (str): ��ʼʱ�䣬��ʽΪYYYYMMDDHH
- `end_time` (str): ����ʱ�䣬��ʽΪYYYYMMDDHH

**����**��
- `list`: ��������ͼƬURL���б�

### 4.2 download_with_urlretrieve(url, save_path)
ʹ��urllib.request.urlretrieve���ص����ļ���

**����**��
- `url` (str): �ļ�URL
- `save_path` (str): �ļ�����·��

**����**��
- `bool`: ���سɹ�����True�����򷵻�False

### 4.3 download_time_range_images(start_time, end_time, save_dir)
����ָ��ʱ�䷶Χ�ڵ�����ͼƬ��

**����**��
- `start_time` (str): ��ʼʱ�䣬��ʽΪYYYYMMDDHH
- `end_time` (str): ����ʱ�䣬��ʽΪYYYYMMDDHH
- `save_dir` (str): ͼƬ����Ŀ¼��Ĭ��Ϊ"downloaded_images"

### 4.4 get_utc_time_formatted()
��ȡ��ǰUTCʱ���7��ǰ��UTCʱ�䣬��ʽ��ΪYYYYMMDDHH��ʽ��

**����**��
- `tuple`: (��ǰʱ���ַ���, 7��ǰʱ���ַ���)

## 5. ʹ��ʾ��

### ʾ��1���������7���������ͼ
```python
# ʹ��Ĭ�����ã��������7���ͼƬ
if __name__ == "__main__":
    end_time, start_time = get_utc_time_formatted()
    download_time_range_images(start_time, end_time, save_dir="recent_images")
```

### ʾ��2�������ض�ʱ�䷶Χ��ͼƬ
```python
# ����2025��8��20��00ʱ��2025��8��20��12ʱ��ͼƬ
if __name__ == "__main__":
    start_time = "2025082000"  # 2025��8��20��00ʱ
    end_time = "2025082012"    # 2025��8��20��12ʱ
    download_time_range_images(start_time, end_time, save_dir="august_images")
```

## 6. ע������

1.  **ʱ���ʽ**������ʱ���������ʹ��**UTCʱ��**����ʽΪ`YYYYMMDDHH`��������ʱ��
2.  **��������**��ȷ������������ȶ��Ļ��������ӣ�������ͼƬ�ļ�
3.  **�洢�ռ�**���������ؿ���ռ�ýϴ���̿ռ䣬��ȷ�����㹻�洢����
4.  **�ļ�����**����ͬ�ļ�����ͼƬ�ᱻ�����صĸ���
5.  **ʱ�䷶Χ**����ע�����ʱ��Ӧ���ڿ�ʼʱ�䣬���򲻻������κ�ͼƬ

