# Django 基礎学習テンプレート

<br>

## 概要
Djangoの機能学習用スターターキット。
CusutomUserは実装済。後からユーザーにカスタムフィールドやメール認証などを追加しやすい状態になっている。

---

## 技術スタック
- Python 3.12.3
- Django 5.2.6

---

## 前提条件

このリポジトリは **学習用スターターキット** として作成されています。  
対象読者は以下の前提を満たしていることを想定しています。

- Linux または WSL での開発環境が準備できている  
- Python と pip の基本操作を理解している  
- GitHub からリポジトリを clone できる  
- ターミナルでコマンドを実行できる  

👉 上記に不安がある方は、まず Linux / Python / Git の基礎を学習してから取り組むことを推奨します。

<br>

---

## git cloneからプロジェクトを再現する方法

### 開発ディレクトリの準備
```bash
$ touch basic_practice
$ cd basic_practice
```

### リポジトリをクローン
```bash
$ git clone https://github.com/ShigeoYugawa/basic_practice.git
```

### 仮想環境の準備
```bash
$ python3 -m venv .venv # 環境によっては python -m venv .venv
$ source .venv/bin/activate
(.venv)$
```

### 依存パッケージをインストール
```bash
(.venv)$ # 各種ツールの最新版をインストールできるようにpipをアップデートする
(.venv)$ pip install --upgrade pip 
(.venv)$ # プロジェクトで使用しているバージョンのツールをインストールする
(.venv)$ pip install -r requirements.txt 
```

### マイグレーションを実行
```bash
(.venv)$ # DBにモデルに対応したテーブルを作成する
(.venv)$ python manage.py migrate 
```

### 管理者ユーザーを追加する
```bash
(.venv)$ python manage.py createsuperuser
メールアドレス: #ここで管理者のメールアドレスを入力
Password:
Password(again):
Superuser created successfully.
(.venv)$
```

### Django Shell でユーザー追加
```bash
(.venv)$ # Djangoシェルを使ってインタラクティブに操作する
(.venv)$ python manage.py shell 

Ctrl click to launch VS Code Native REPL
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> # カスタムユーザーモデルをインポート
>>> from accounts.models import CustomUser
>>>
>>> # ユーザーを１つ作成する
>>> user = CustomUser.objects.create_user(
...     email="user1@example.com",
...     password="testpass123",
...     is_active=True)
>>>
>>> # 現在インスタンス化しているユーザーを呼び出す
>>> print(user)
user1@example.com
>>>
>>> # カスタムユーザーをすべて呼び出す
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

### 管理画面にアクセスして登録ユーザーを確認する

#### 開発サーバーを起動

```bash
(.venv)$ python manage.py runserver
```

下記URLへアクセスして管理者メールアドレスとパスワードで管理画面へログインする
```bash
http://localhost:8000/admin
```

#### テストの実行

```bash
(.venv)$ pytest -v
====================================== test session starts ======================================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0 -- /path/to/basic_practice/.venv/bin/python3
cachedir: .pytest_cache
django: version: 5.2.6, settings: basic_practice.settings (from ini)
rootdir: /path/to/basic_practice
configfile: pytest.ini
plugins: django-4.11.1
collected 9 items                                                                               

tests/accounts/test_accounts_forms.py::test_dummy_user_form_valid PASSED                  [ 11%]
tests/accounts/test_accounts_forms.py::test_dummy_user_form_invalid PASSED                [ 22%]
tests/accounts/test_accounts_views.py::test_dummy_fbv PASSED                              [ 33%]
tests/accounts/test_accounts_views.py::test_dummy_cbv PASSED                              [ 44%]
tests/accounts/test_accounts_views.py::test_create_user_with_manager PASSED               [ 55%]
tests/accounts/test_accounts_views.py::test_create_superuser_with_manager PASSED          [ 66%]
tests/accounts/test_auth_flow.py::test_registration_login_logout_flow PASSED              [ 77%]
tests/accounts/test_accounts_forms.py::test_dummy_form_valid PASSED                       [ 88%]
tests/accounts/test_accounts_forms.py::test_dummy_form_invalid PASSED                     [100%]

======================================= 9 passed in 3.21s =======================================
(.venv)$
```

#### ブラウザでビューの動作を確認
```bash
(.venv)$ # 開発サーバーを起動
(.venv)$ python manage.py runserver
```

##### 関数ベースビューにアクセス
http://localhost:8000/accounts/dummy_fbv/

ブラウザに表示される内容
```bash
Hello Django from FBV!
```

##### クラスベースビューにアクセス
http://localhost:8000/accounts/dummy_cbv/

ブラウザに表示される内容
```bash
Hello Django from CBV!
```

##### ユーザー登録、ログアウト、ログインを確認する
`http://localhost:8000/`

ヘッダにあるSignupからユーザー登録画面へ移動する。
メールアドレス、パスワードでユーザー登録した後、ログアウトして、再度ログイン動作を実行してみる。
ユーザー登録後およびログイン後はWelcomeページに遷移する。ログアウトするとホーム画面に遷移する。


<br><br>

---

## イチから構築する方法

この手順は備忘録として作成しています。

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
(.venv)$ # 各種ツールの最新版をインストールできるようにpipをアップデートする
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
(.venv)$ touch accounts/models.py
```

- accounts/models.py

[class CustomUser](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/models.py#L40)

### CustomUserManager を作成する

- accounts/models.py

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
Password:
Password(again):
Superuser created successfully.
(.venv)$
```

### Django Shell でユーザー追加
```bash
(.venv)$ # Djangoシェルを使ってインタラクティブに操作する
(.venv)$ python manage.py shell 

Ctrl click to launch VS Code Native REPL
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> # カスタムユーザーモデルをインポート
>>> from accounts.models import CustomUser
>>>
>>> # ユーザーを１つ作成する
>>> user = CustomUser.objects.create_user(
...     email="user1@example.com",
...     password="testpass123",
...     is_active=True)
>>>
>>> # 現在インスタンス化しているユーザーを呼び出す
>>> print(user)
user1@example.com
>>>
>>> # カスタムユーザーをすべて呼び出す
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

#### 下記モジュールを追加する
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

- basic_practice/settings.py - 日本語対応させる

[settings](https://github.com/ShigeoYugawa/basic_practice/blob/main/basic_practice/settings.py#L106)


### 管理画面にアクセスして登録ユーザーを確認する
#### 開発サーバーを起動
```bash
(.venv)$ python manage.py runserver
```

#### 下記URLへアクセスして管理者メールアドレスとパスワードで管理画面へログインする
```bash
http://localhost:8000/admin
```

### ダミーのビュー、ルーティング、フォーム、テストを追加する

ここでは簡単な動作イメージを掴むためダミーのビューやフォームを作成した。

#### ビューの追加
```bash
(.venv)$ touch accounts/views.py
```
[accounts/views.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/views.py#L9)

#### ルーティングの追加
```bash
(.venv)$ touch accounts/urls.py
```
[accounts/urls.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/urls.py#L10)

[basic_practice/urls.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/basic_practice/urls.py#L20)

#### フォームの追加
```bash
(.venv)$ touch accounts/forms.py
```
[accounts/urls.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/accounts/forms.py#L9)

#### テストの追加
```bash
(.venv)$ mkdir -p tests/accounts
(.venv)$ touch tests/accounts/test_accounts_views.py
(.venv)$ touch tests/accounts/test_accounts_forms.py
(.venv)$ touch tests/accounts/test_auth_flow.py
```
[test_accounts_views.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/tests/accounts/test_accounts_views.py#L10)

[test_accounts_forms.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/tests/accounts/test_accounts_forms.py#L11)

[test_auth_flow.py](https://github.com/ShigeoYugawa/basic_practice/blob/main/tests/accounts/test_auth_flow.py#L8)

#### テストの実行

```bash
(.venv)$ pytest -v
====================================== test session starts ======================================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0 -- /path/to/basic_practice/.venv/bin/python3
cachedir: .pytest_cache
django: version: 5.2.6, settings: basic_practice.settings (from ini)
rootdir: /path/to/basic_practice
configfile: pytest.ini
plugins: django-4.11.1
collected 9 items                                                                               

tests/accounts/test_accounts_forms.py::test_dummy_user_form_valid PASSED                  [ 11%]
tests/accounts/test_accounts_forms.py::test_dummy_user_form_invalid PASSED                [ 22%]
tests/accounts/test_accounts_views.py::test_dummy_fbv PASSED                              [ 33%]
tests/accounts/test_accounts_views.py::test_dummy_cbv PASSED                              [ 44%]
tests/accounts/test_accounts_views.py::test_create_user_with_manager PASSED               [ 55%]
tests/accounts/test_accounts_views.py::test_create_superuser_with_manager PASSED          [ 66%]
tests/accounts/test_auth_flow.py::test_registration_login_logout_flow PASSED              [ 77%]
tests/accounts/test_accounts_forms.py::test_dummy_form_valid PASSED                       [ 88%]
tests/accounts/test_accounts_forms.py::test_dummy_form_invalid PASSED                     [100%]

======================================= 9 passed in 3.21s =======================================
(.venv)$ 


```

#### ブラウザでビューの動作を確認
```bash
(.venv)$ # 開発サーバーを起動
(.venv)$ python manage.py runserver
```

##### 関数ベースビューにアクセス
http://localhost:8000/accounts/dummy_fbv/

ブラウザに表示される内容
```bash
Hello Django from FBV!
```

##### クラスベースビューにアクセス
http://localhost:8000/accounts/dummy_cbv/

ブラウザに表示される内容
```bash
Hello Django from CBV!
```

##### ユーザー登録、ログアウト、ログインを確認する
`http://localhost:8000/`

ヘッダにあるSignupからユーザー登録画面へ移動する。
メールアドレス、パスワードでユーザー登録した後、ログアウトして、再度ログイン動作を実行してみる。
ユーザー登録後およびログイン後はWelcomeページに遷移する。ログアウトするとホーム画面に遷移する。


<br><br>

---

## ライセンス

このリポジトリは **学習目的のみ** で作成されています。  
コードは学習や個人プロジェクトに使用できますが、**商用利用や再配布は禁止**です。

