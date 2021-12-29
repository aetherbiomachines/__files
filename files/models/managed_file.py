from django.db import models


class Environment(models.TextChoices):

    LOCAL = 'local'
    TEST = 'test'
    DEV = 'dev'
    STG = 'stg'
    PRD = 'prd'


class S3Bucket(models.TextChoices):

    NONE = 'no bucket selected'
    LIMS_DATA_PRD = 'lims-data-prd'
    LIMS_DATA_DEV = 'lims-data-dev'


class MIMEType(models.TextChoices):

    BIN = 'application/octet-stream'
    CSV = 'text/csv'
    GIF = 'image/gif'
    JPEG = 'image/jpeg'
    PDF = 'application/pdf'
    PNG = 'image/png'
    TXT = 'text/plain'


class Category(models.TextChoices):

    TESTING_ONLY = 'category_unit_testing_only'
    LCMS = 'lcms'
    NGS = 'ngs'
    MALDI = 'maldi'


class Context(models.TextChoices):

    TESTING_ONLY = 'context_unit_testing_only'
    RAW = 'raw'
    PROCESSED = 'processed'


class ManagedFile(models.Model):

    env = models.CharField(max_length=10, choices=Environment.choices, default=Environment.TEST)

    file_name = models.CharField(max_length=100)

    s3_bucket = models.CharField(max_length=50, choices=S3Bucket.choices)
    s3_key = models.CharField(unique=True, max_length=250)
    s3_base_name = models.CharField(max_length=250)
    s3_revision = models.IntegerField(default=0)

    mime_type = models.CharField(max_length=50, choices=MIMEType.choices, default=MIMEType.BIN)
    category = models.CharField(max_length=50, choices=Category.choices)
    context = models.CharField(max_length=50, choices=Context.choices)

    related_entities = models.ManyToManyField('files.RelatedEntity')
