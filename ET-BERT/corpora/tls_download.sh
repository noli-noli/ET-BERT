#シェル内で本ファイルを実行


#Googleドライブで共有したURL内に存在するIDを定義
ID="1fw3FdKH7nmWYE7v-mq5jDS0poFO3_0_t"
#保存するファイル名
FILE="encrypted_traffic_burst.zip"

wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$ID" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$ID" -O $FILE && rm -rf /tmp/cookies.txt