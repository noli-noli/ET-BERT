#シェル内で本ファイルを実行


#Googleドライブで共有したURL内に存在するIDを定義
ID="1c5v7q8syD_9r3IDJM3_g7Un8RnoM1Mdm"
#保存するファイル名
FILE="pretrained_model.bin"

wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$ID" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$ID" -O $FILE && rm -rf /tmp/cookies.txt