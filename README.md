# Selenium の練習 in python

## 環境構築

```sh
docker-compose build
```

## jupyter labを起動

```sh
docker-compose up -d jupyter
```

## SeleniumでWebアクセス実行コマンド

```sh
python main.py -u {user id} -p {password}
```

## TODO

* main.py 実行後に `[chrome] <defunct>` のゾンビプロセスが残ってしまう。
  * `docker-compose down && docker-compose up -d jupyter` でプロセスはまっさらになるが、main.py内の処理でなんとかしたい
