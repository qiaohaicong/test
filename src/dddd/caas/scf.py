# -*- coding: utf8 -*-
import json
from datetime import datetime
import requests  # 需要导入 requests 库

def main_handler(event, context):
    try:
        # 从事件中提取所需的参数
        record = event.get('Records', [{}])[0]

        # 提取参数
        url = record.get('cos', {}).get('cosObject', {}).get('url', '')
        size = record.get('cos', {}).get('cosObject', {}).get('size', 0)
        x_cos_request_id = record.get('cos', {}).get('cosObject', {}).get('meta', {}).get('x-cos-request-id', '')
        event_name = record.get('event', {}).get('eventName', '')
        event_source = record.get('event', {}).get('eventSource', '')
        event_time_unix = record.get('event', {}).get('eventTime', 0)

        # 转换时间
        event_time_formatted = ''
        if event_time_unix:
            try:
                dt = datetime.fromtimestamp(event_time_unix)
                event_time_formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                event_time_formatted = str(event_time_unix)

        # 从context提取
        request_id = context.get('request_id', '') if context else ''

        # 构建结果
        result = {
            "url": url,
            "x_cos_request_id": x_cos_request_id,
            "event_name": event_name,
            "event_source": event_source,
            "event_time_unix": event_time_unix,
            "event_time_formatted": event_time_formatted,
            "size": size,
            "scf_request_id": request_id
        }

        # ------------------ 新增：调用外部同步服务 ------------------
        try:
            # 目标服务地址
            sync_service_url = "http://42.192.26.193:8000/sync"
            # 提取主机信息用于Host头
            host_header = "42.192.26.193:8000"

            # 发送 POST 请求
            print(f"正在调用同步服务: {sync_service_url},参数: {result}")
            response = requests.post(
                sync_service_url,
                json=result,  # 直接将 result 作为 JSON 发送
                headers={'Content-Type': 'application/json','Host': host_header,},
                timeout=5  # 设置5秒超时
            )

            print(f"Response: {response.json()}")
        except requests.exceptions.Timeout:
            print("错误：调用同步服务超时（5秒）")
        except requests.exceptions.ConnectionError:
            print("错误：无法连接到同步服务，请检查网络和地址")
        except requests.exceptions.RequestException as req_err:
            print(f"错误：请求同步服务失败 - {str(req_err)}")
        except Exception as sync_err:
            print(f"错误：调用同步服务时发生意外错误 - {str(sync_err)}")
        # ---------------------------------------------------------

    except Exception as e:
        return {"error": str(e)}