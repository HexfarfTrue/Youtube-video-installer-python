#!/bin/bash
#EN_US.UTF-8 : You can add a "cd 'directory to .py file'" to top of this script if you want to use Youtube_video_installer from any directory
#RU-RU.UTF-8 : Вы можете добавть "cd 'директория к .py файлу'" на начало скрипта, если желаете использовать его из любой директории

source $HOME/venv/bin/activate 

#EN_US.UTF-8 : Change ~/venv/bin/activate to ~/venv/bin/activate.fish and etc, if you using different shell
#RU_RU.UTF-8 : Измените  ~/venv/bin/activate на ~/venv/bin/activate

python Youtube_video_installer.py

deactivate
