@echo off

CLS

mkdir .\temp

SET PYTHONPATH=..\programy\src;..\programy\libs\MetOffer-1.3.2;.

python ./src/conditionalfileloader/ez_chatbot.py --config .\config.windows.yaml --cformat yaml --logging .\logging.windows.yaml

