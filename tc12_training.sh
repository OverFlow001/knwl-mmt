cp split_tc12.py /mnt/Storage/Dataset/iaprtc12/
cd /mnt/Storage/Dataset/iaprtc12
python3 split_tc12.py
cd -
rm -rf data
mkdir -p data/mono/de/ && cp /mnt/Storage/Dataset/iaprtc12/{all,idx}.de data/mono/de/
mkdir -p data/mono/en/ && cp /mnt/Storage/Dataset/iaprtc12/{all,idx}.en data/mono/en/
mkdir -p data/para/dev/ && cp /mnt/Storage/Dataset/iaprtc12/{test,val}.{de,en} data/para/dev/

bash install-tools.sh
bash tc12-full-reload/process-data-nmt.sh --src de --tgt en --reload_vocab vocab_ende --reload_codes codes_ende
cp /mnt/Storage/Dataset/iaprtc12/idx.{de,en} data/processed/de-en/

tc12-full-reload/img.full-reload.deen.sh