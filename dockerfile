FROM nvidia/cuda:11.4.3-base-ubuntu20.04

#docker-composeから受け取った引数(proxyのアドレス)を環境変数にセット
ARG http_tmp
ARG https_tmp
ENV http_proxy=$http_tmp
ENV https_proxy=$https_tmp

#aptのTime Zone設定でハングアップしない様に予め指定及び設定する
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#コンテナ内で使用するパッケージをインストール
RUN apt update --fix-missing && apt install python3 python3-pip git screen tmux wine mono-runtime -y

#wineで32bitアプリを動かす為の設定
RUN dpkg --add-architecture i386 && apt-get update && apt-get install wine32 -y

#tsharkを強引にインストールする
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark


#requirements.txtの内容をインストールする
COPY ET-BERT/requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt