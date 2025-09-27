"""
accounts.models モジュール

このモジュールはCustomUserモデル全般の管理を担当する

クラス:
- CustomUserManager: カスタムユーザーの管理
- CustomUser: カスタムユーザー　独自フィールドを定義するために利用する
"""


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """CustomUserモデルの管理 
    create_user と create_superuser メソッドを提供し、ユーザー作成時の処理を統一します。
    """

    def create_user(self, email, password=None, **extra_fields):
        """通常のユーザー作成"""
        if not email:
            raise ValueError("メールアドレスは必須です")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """管理者（スーパーユーザー）作成"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル

    現在はパスワード認証を未設置

    Attributes:
        email (str): ログインで使用するメールアドレス
        nickname (str): 表示用ニックネーム
        is_active (bool): アカウント有効判定　パスワード認証未設置段階では常にTrue
        is_staff (bool): 管理画面での操作権限
        USERNAME_FIELD (str): 認証に使用するフィールド（email）
        REQUIRED_FIELDS (list): create_superuser で必須の追加フィールド
    """

    email = models.EmailField(verbose_name="メールアドレス", unique=True)
    nickname = models.CharField(verbose_name="ニックネーム", max_length=50, blank=True, null=True)
    password = models.CharField(verbose_name="パスワード", max_length=128)
    is_active = models.BooleanField(verbose_name="アカウントの有効性", default=True)
    is_staff = models.BooleanField(verbose_name="アカウントの管理画面アクセス権限", default=False)

    objects = CustomUserManager() # emailでユーザー作成するために必要。

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー一覧"

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.email
    
    def get_display_name(self):
        return self.nickname or self.email