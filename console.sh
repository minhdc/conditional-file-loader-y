
#! /bin/sh

clear

export PYTHONPATH=./src:../program-y/src:../template-y/libs/MetOffer-1.3.2:.

python3 ./src/conditionalfileloader/new_chat_bot.py --config ./config.yaml --cformat yaml --logging ./logging.yaml --bot_root .

