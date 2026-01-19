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
                 "/coscaas/chg8szh_t",
                 "/coscaas/ciq2szh_t",
                 "/coscaas/cnj9szh_t",
                 "/coscaas/cny5sgh_t",
                 "/coscaas/coc4szh_t",
                 "/coscaas/cos_bucket_inventory",
                 "/coscaas/ctn3szh_t",
                 "/coscaas/cwh8szh_t",
                 "/coscaas/cwn9szh_t",
                 "/coscaas/cxi6wx_t",
                 "/coscaas/cyu7wx_t",
                 "/coscaas/DevopsShared2",
                 "/coscaas/DevopsShared3",
                 "/coscaas/DevopsShared4",
                 "/coscaas/DevopsShared5",
                 "/coscaas/dfu1szh_t",
                 "/coscaas/dhn5sgh_t",
                 "/coscaas/doa2sgh_t",
                 "/coscaas/DPEIEN_t",
                 "/coscaas/dze2szh_t",
                 "/coscaas/dzg2szh_t",
                 "/coscaas/eav1szh_shared_t",
                 "/coscaas/eli3szh_t",
                 "/coscaas/enm1szh_t",
                 "/coscaas/euc1szh_t",
                 "/coscaas/ewo1wx_t",
                 "/coscaas/ezd1szh_t",
                 "/coscaas/fau2sgh_t",
                 "/coscaas/fau3sgh_t",
                 "/coscaas/feg5szh_t",
                 "/coscaas/fengyuan_t",
                 "/coscaas/fhe8sgh_t",
                 "/coscaas/fji3szh_t",
                 "/coscaas/fna8szh_t",
                 "/coscaas/fnl2szh_t",
                 "/coscaas/fug7szh_t",
                 "/coscaas/fxl01",
                 "/coscaas/gam4wx_t",
                 "/coscaas/gch3sgh_t",
                 "/coscaas/geo1cng_t",
                 "/coscaas/ghc4szh_t",
                 "/coscaas/goy5szh_t",
                 "/coscaas/gup1wx_t",
                 "/coscaas/gyu1cgd4_t",
                 "/coscaas/ham2wx_t",
                 "/coscaas/hanteng_t",
                 "/coscaas/haowen_t",
                 "/coscaas/hem4szh_t",
                 "/coscaas/heziyu_t",
                 "/coscaas/hhg1szh_t",
                 "/coscaas/hiq3szh_t",
                 "/coscaas/hiz4szh_t",
                 "/coscaas/hma9kor_t",
                 "/coscaas/hni7szh_t",
                 "/coscaas/hos4wx_t",
                 "/coscaas/huangman_t",
                 "/coscaas/hushaoy_t",
                 "/coscaas/hut9szh_t",
                 "/coscaas/ico1szh_t",
                 "/coscaas/icz4szh_t",
                 "/coscaas/iix5sgh_t",
                 "/coscaas/iiz1wx_t",
                 "/coscaas/irn1szh_t",
                 "/coscaas/ish3szh_t",
                 "/coscaas/isy3szh_t",
                 "/coscaas/iul8sgh_t",
                 "/coscaas/jak1szh_t",
                 "/coscaas/jdh1sgh_t",
                 "/coscaas/jianghan_t",
                 "/coscaas/jiangyi",
                 "/coscaas/jianing_t",
                 "/coscaas/jiaweili_t",
                 "/coscaas/jsu3szh_t",
                 "/coscaas/jye2szh_t",
                 "/coscaas/kix1sgh_t",
                 "/coscaas/kmb2hi",
                 "/coscaas/knc1szh_t",
                 "/coscaas/knn1szh_t",
                 "/coscaas/koc2wx_t",
                 "/coscaas/kra1sf",
                 "/coscaas/lanjun_t",
                 "/coscaas/lianglq_t",
                 "/coscaas/liuzimig_t",
                 "/coscaas/liysh_t",
                 "/coscaas/longhai_t",
                 "/coscaas/mlu2szh_t",
                 "/coscaas/naz1wx_t",
                 "/coscaas/nnj1wx_t",
                 "/coscaas/nqh1szh_t",
                 "/coscaas/nsz3szh_t",
                 "/coscaas/num1st",
                 "/coscaas/ooy2szh_t",
                 "/coscaas/qem1sgh_t",
                 "/coscaas/qgw1szh_t",
                 "/coscaas/qhctest",
                 "/coscaas/qiaohaicong_t",
                 "/coscaas/qiaohaicong_tt",
                 "/coscaas/qiaohhh_t",
                 "/coscaas/qiupeng_t",
                 "/coscaas/qnt1sgh_t",
                 "/coscaas/quu2sgh_t",
                 "/coscaas/rangfen_t",
                 "/coscaas/rbc1le",
                 "/coscaas/rem4sgh_t",
                 "/coscaas/rongrong_t",
                 "/coscaas/Sales_t",
                 "/coscaas/samqliu",
                 "/coscaas/sco4syv_t",
                 "/coscaas/SEN5SGH",
                 "/coscaas/shangtao_t",
                 "/coscaas/shenyi_t",
                 "/coscaas/sjh8wx_t",
                 "/coscaas/somcszh_t",
                 "/coscaas/ssn4sgh_t",
                 "/coscaas/suw5wx_t",
                 "/coscaas/taa1st_t",
                 "/coscaas/tew2wx_t",
                 "/coscaas/tyi3szh2_t",
                 "/coscaas/tyn3szh_t",
                 "/coscaas/uaw2szh_t",
                 "/coscaas/ueh1sgh",
                 "/coscaas/ujw4szh_t",
                 "/coscaas/ult1sgh_t",
                 "/coscaas/upp1szh_t",
                 "/coscaas/uql1wx_t",
                 "/coscaas/user_bosch_default_notest",
                 "/coscaas/usu3wx_t",
                 "/coscaas/usy2szh_t",
                 "/coscaas/uxd3szh_t",
                 "/coscaas/wba3wx_t",
                 "/coscaas/wbg3szh_t",
                 "/coscaas/wenjing_t",
                 "/coscaas/wez1cgd4_t",
                 "/coscaas/wgx9sgh_t",
                 "/coscaas/wix6wx_t",
                 "/coscaas/wsh9wx_t",
                 "/coscaas/wuchenglin_t",
                 "/coscaas/wuyu_t",
                 "/coscaas/wye4sgh_t",
                 "/coscaas/wyg6wx_t",
                 "/coscaas/wyi7wx_t",
                 "/coscaas/xal3wx_t",
                 "/coscaas/xaq2szh_t",
                 "/coscaas/xcu6wx_t",
                 "/coscaas/xiaotong_t",
                 "/coscaas/xie9szh_t",
                 "/coscaas/xil5wx_t",
                 "/coscaas/xla5szh_t",
                 "/coscaas/xun9szh",
                 "/coscaas/xuy2lr_t",
                 "/coscaas/yaf6wx_t",
                 "/coscaas/yaning_t",
                 "/coscaas/yao4wx_t",
                 "/coscaas/yha7sgh_t",
                 "/coscaas/yii7szh_t",
                 "/coscaas/yij6sgh_t",
                 "/coscaas/yiq6szh_t",
                 "/coscaas/yjn6sgh_t",
                 "/coscaas/ysa4wx_t",
                 "/coscaas/yua8wx_t",
                 "/coscaas/yuchen_t",
                 "/coscaas/yujie_t",
                 "/coscaas/yuu4wx_t",
                 "/coscaas/yuu7wx_t",
                 "/coscaas/yuxuan_t",
                 "/coscaas/ywa2szh_t",
                 "/coscaas/yxe8szh_t",
                 "/coscaas/yza8szh_t",
                 "/coscaas/zab3szh_t",
                 "/coscaas/zag2wx_t",
                 "/coscaas/ZAG2WX_t",
                 "/coscaas/zanghp_t",
                 "/coscaas/zci3wx_t",
                 "/coscaas/zdo6fe",
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