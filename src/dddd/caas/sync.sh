#!/bin/bash

nohup python3.9 sync_account_directory.py &
nohup python3.9 sync_adc_to_local.py &
nohup python3.9 sync_adc_to_backup.py &
nohup python3.9 delete_file_new.py &
nohup python3.9 delete_file.py &

