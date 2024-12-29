# Contributors:
# * Contributor: <alexandersafstrom@proton.me>
# Generated by Django 5.1.3 on 2024-12-20 18:15

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                ("image_id", models.TextField(primary_key=True, serialize=False)),
                ("created_at", models.IntegerField()),
                ("image", models.BinaryField()),
                ("age", models.IntegerField(null=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                (
                    "localization",
                    models.CharField(
                        choices=[
                            ("ear", "Ear"),
                            ("face", "Face"),
                            ("neck", "Neck"),
                            ("scalp", "Scalp"),
                            ("abdomen", "Abdomen"),
                            ("back", "Back"),
                            ("chest", "Chest"),
                            ("trunk", "Trunk - Other"),
                            ("acral", "Acral (Fingers/Toes)"),
                            ("hand", "Hand"),
                            ("upper_extremity", "Upper Extremity (Arm)"),
                            ("foot", "Foot"),
                            ("lower_extremity", "Lower Extremity (Leg)"),
                            ("genital", "Genital Area"),
                        ],
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "lesion_type",
                    models.CharField(
                        choices=[
                            ("nv", "Melanocytic nevi"),
                            ("bkl", "Benign keratosis-like lesions"),
                            ("df", "Dermatofibroma"),
                            ("vasc", "Vascular lesions"),
                            ("mel", "Melanoma"),
                            ("bcc", "Basal cell carcinoma"),
                            (
                                "akiec",
                                "Actinic keratoses and intraepithelial carcinoma",
                            ),
                        ],
                        max_length=5,
                    ),
                ),
            ],
            options={
                "db_table": "images",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                ("version", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.IntegerField()),
                ("weights", models.BinaryField()),
                ("hyperparameters", models.TextField(default="default")),
            ],
            options={
                "db_table": "models",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=150, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("age", models.IntegerField()),
                (
                    "sex",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="skinscan_user_set",
                        related_query_name="skinscan_user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="skinscan_user_set",
                        related_query_name="skinscan_user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "users",
                "managed": True,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Requests",
            fields=[
                ("request_id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.IntegerField()),
                ("probability", models.FloatField(blank=True, null=True)),
                ("image", models.BinaryField()),
                (
                    "localization",
                    models.CharField(
                        choices=[
                            ("ear", "Ear"),
                            ("face", "Face"),
                            ("neck", "Neck"),
                            ("scalp", "Scalp"),
                            ("abdomen", "Abdomen"),
                            ("back", "Back"),
                            ("chest", "Chest"),
                            ("trunk", "Trunk - Other"),
                            ("acral", "Acral (Fingers/Toes)"),
                            ("hand", "Hand"),
                            ("upper extremity", "Upper Extremity (Arm)"),
                            ("foot", "Foot"),
                            ("lower extremity", "Lower Extremity (Leg)"),
                            ("genital", "Genital Area"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "lesion_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("nv", "Melanocytic nevi (Benign)"),
                            ("bkl", "Benign keratosis-like lesion (Benign)"),
                            ("df", "Dermatofibroma (Benign)"),
                            ("vasc", "Vascular lesion (Benign)"),
                            ("mel", "Melanoma (Malignant)"),
                            ("bcc", "Basal cell carcinoma (Malignant)"),
                            (
                                "akiec",
                                "Actinic keratoses and intraepithelial carcinoma (Malignant)",
                            ),
                        ],
                        max_length=5,
                        null=True,
                    ),
                ),
                ("feature_impact", models.TextField(blank=True, null=True)),
                ("heatmap", models.BinaryField(blank=True, null=True)),
                ("model", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "requests",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ActiveModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.IntegerField()),
                (
                    "model",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="application.model",
                    ),
                ),
            ],
            options={
                "db_table": "model_active",
                "managed": True,
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(("id", 1)),
                        name="single_active_model_constraint",
                    )
                ],
            },
        ),
    ]
