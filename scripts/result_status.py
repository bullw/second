import os
import json
import sys

def count_statuses(report_dir):
    # 统计结果
    status_count = {
    }

    # 遍历目录下的所有文件
    if not os.path.exists(report_dir) or not os.path.isdir(report_dir):
        return
    for file in os.listdir(report_dir):
        file_path = os.path.join(report_dir, file)
        if not os.path.isfile(file_path) or not file.endswith('result.json'):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                status = json_data.get('status', 'unknown')
                if status not in status_count:
                    status_count[status] = 1
                else:
                    status_count[status] += 1
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # 打印统计结果
    print("Test Result Summary:")
    for status, count in status_count.items():
        print(f"{status.capitalize()} Count: {count}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python result_stats.py <report_directory>")
        sys.exit(1)
    report_directory = sys.argv[1]
    count_statuses(report_directory)
