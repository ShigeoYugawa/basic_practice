# 基礎学習テンプレート

---

## 概要
Djangoの機能学習用スターターキット。
CusutomUserは実装済。後からユーザーにカスタムフィールドやメール認証などを追加しやすい状態になっている。

---

## 技術スタック
- Python 3.12.3
- Django 5.2.6

---

## インストール方法（git cloneから再現する方法）

---

## イチから構築する方法

### 開発ディレクトリの準備
```bash
$ touch basic_practice
$ cd basic_practice
```

### 仮想環境の準備
```bash
$ python3 -m venv .venv # 環境によってpython -m venv .venv
$ source .venv/bin/activate
(venv)$
```

### pip をアップデート
```bash
(venv)$ pip install --upgrade pip
```

### Django および必要なツールをインストール
```bash
(venv)$ pip install django pytest django-stubs mypy pytest-django
```

### Django プロジェクト作成
```bash
(venv)$ django-admin startproject basic_practice .
```

### Django の動作確認
```bash
(venv)$ python manage.py runserver
```
ブラウザで http://127.0.0.1:8000/ にアクセスして Django のウェルカムページが表示されればOK。

### CustomUser を作成する
[class CustomUser](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/models.py#L40)

### CustomUserManager を作成する
[class CustomUserManager](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/models.py#L16)

### マイグレーションを実行する
必ずカスタムユーザーを使ってアプリ開発できるように真っ先にマイグレーションを実行しておく
ここではsqliteを使う
```bash
(venv)$ python manage.py makemigrations accounts
```

### 
---

## ライセンス

このリポジトリは **学習目的のみ** で作成されています。  
コードは学習や個人プロジェクトに使用できますが、**商用利用や再配布は禁止**です。

