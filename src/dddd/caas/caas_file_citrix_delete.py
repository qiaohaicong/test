#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import subprocess
from datetime import datetime,timedelta
import logging
from logging.handlers import TimedRotatingFileHandler

LOG_FILE = '/data/caas_file_delete.log'

def setup_logging():
    """设置按天轮转的日志"""
    # 创建日志目录（如果不存在）
    log_dir = os.path.dirname(LOG_FILE)
    os.makedirs(log_dir, exist_ok=True)
    # 配置 TimedRotatingFileHandler
    handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight', interval=1, backupCount=30
    )
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    # 配置日志
    logging.basicConfig(level=logging.INFO, handlers=[handler])


def main():
    date_list = ["/coscaas/aai1wx_t",
                 "/coscaas/acj5szh_t",
                 "/coscaas/agy3szh_t",
                 "/coscaas/aiz2sgh_t",
                 "/coscaas/ajg5szh_t",
                 "/coscaas/ajk1szh_t",
                 "/coscaas/aoo1szh_t",
                 "/coscaas/aoo5szh_t",
                 "/coscaas/aqw2szh_t",
                 "/coscaas/arl2kor_t",
                 "/coscaas/auj4szh_t",
                 "/coscaas/aus2sgh_t",
                 "/coscaas/azh1szh",
                 "/coscaas/azw2sgh_t",
                 "/coscaas/bam3lr_t",
                 "/coscaas/buxiangyu_t",
                 "/coscaas/cae3wx_t",
                 "/coscaas/chaoyang_t",
                 "/coscaas/chaoyue_t",
                 "/coscaas/chengyz_t",
                 "/coscaas/zea8szh_t",
                 "/coscaas/zes7szh_t",
                 "/coscaas/zhikang_t",
                 "/coscaas/zhuhua_t"]
    try:
        # 逐一同步
        for d in date_list:
            try:
                logging.info("公有云到专区" + d)
                data = findFiles(d)
                logging.info("测试新增一行")
                logging.info(str(data))
                target = d.replace("coscaas","coscaas/back_up_delete")
                mvcmd = "mv " + d + " " + target
                subprocess.run(mvcmd, shell=True, check=True)

                logging.info(target + "==============" + mvcmd)
            except Exception as e:
                logging.error(f"Error: Failed to run commands. Error message: {e}")
    except Exception as e:
        logging.error(f"Error: Failed to run commands. Error message: {e}")

def findFiles(source):
    cmd = "find " + source + " -type f |wc -l"
    logging.info("find files:%s" % cmd)
    with os.popen(cmd) as rs:
        lines = rs.read()
    data = str(lines).split('\n')
    return data


if __name__ == "__main__":
    setup_logging()
    while True:
        main()
        time.sleep(60)
