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
$ python3 -m venv .venv # 環境によっては python -m venv .venv
$ source .venv/bin/activate
(.venv)$
```

### pip をアップデート
```bash
(.venv)$ pip install --upgrade pip
```

### Django および必要なツールをインストール
```bash
(.venv)$ pip install django pytest django-stubs mypy pytest-django
```

### Django プロジェクト作成
```bash
(.venv)$ django-admin startproject basic_practice .
```

### Django の動作確認
```bash
(.venv)$ python manage.py runserver
```
ブラウザで http://127.0.0.1:8000/ にアクセスして Django のウェルカムページが表示されればOK。

### CustomUser を作成する

```bash
(.venv)$ touch accounts/views.py
```

- accounts/views.py

[class CustomUser](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/models.py#L40)

### CustomUserManager を作成する

- accounts/views.py

[class CustomUserManager](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/models.py#L16)

### マイグレーションを実行する
必ずカスタムユーザーを使ってアプリ開発できるように真っ先にマイグレーションを実行しておく
※ここではsqliteを使う
```bash
(.venv)$ python manage.py makemigrations accounts
```

### 管理者ユーザーを追加する
```bash
(.venv)$ python manage.py createsuperuser
メールアドレス: #ここで管理者のメールアドレスを入力
パスワード(again):
Superuser created successfully.
(.venv)$
```

### Django Shell でユーザー追加
```bash
(.venv)$ python manage.py shell

Ctrl click to launch VS Code Native REPL
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> from accounts.models import CustomUser
>>> user = CustomUser.objects.create_user(
...     email="user1@example.com",
...     password="testpass123",
...     is_active=True)
>>>
>>> print(user)
user1@example.com
>>>
>>> users = CustomUser.objects.all()
>>> for user in users:
...     print(user.email, user.is_active, user.is_staff)
... 
admin@example.com True True
user1@example.com True False
>>>
>>> exit()
(.venv)$

```

### Django 管理画面で編集CustomUserを表示できるようにする

下記モジュールを追加する
- accounts/apps.py - 管理画面内のアプリ名を日本語に変換する
- accounts/admin.py - 管理画面にカスタムユーザーを表示させる
```bash
(.venv)$ touch accounts/apps.py
```
[class AccountsConfig](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/apps.py#L8)
```bash
(.venv)$ touch accounts/admin.py
```
[class CustomUserAdmin](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/admin.py#L7)

下記モジュールを修正する

- basic_practice/settings.py - カスタムユーザーをユーザーとして認識させる

[settings](https://github.com/ShigeoYugawa/basic_practice/blob/main/basic_practice/settings.py#L122)


### 管理画面にアクセスして登録ユーザーを確認する
開発サーバーを起動
```bash
(.venv)$ python manage.py runserver
```

下記URLへアクセスして管理者メールアドレスとパスワードで管理画面へログインする
```bash
http://localhost:8000/admin
```

---

## ライセンス

このリポジトリは **学習目的のみ** で作成されています。  
コードは学習や個人プロジェクトに使用できますが、**商用利用や再配布は禁止**です。

