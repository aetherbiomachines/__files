'''
NOTE: unused
'''

import jsonfield
from django.db import models

from lims.lib.constants.files import S3Bucket, FileMIMEType, FileCategory, valid_file_context_choices, FileUploadOption
from lims.lib.constants.general import Environment


class ManagedFile(models.Model):
    env = models.CharField(max_length=10, choices=Environment.choices(), default=Environment.TEST)
    s3_bucket = models.CharField(max_length=50, choices=S3Bucket.choices())
    s3_key = models.CharField(unique=True, max_length=250)
    s3_base_name = models.CharField(max_length=250)
    s3_revision = models.IntegerField(default=0)
    file_name = models.CharField(max_length=100)
    related_entities = models.ManyToManyField('RelatedEntity', related_name='related_files')
    mime_type = models.CharField(max_length=50, choices=FileMIMEType.choices())
    category = models.CharField(max_length=50, choices=FileCategory.choices())
    context = models.CharField(max_length=50, choices=valid_file_context_choices)

    @classmethod
    def upload(cls, request):
        from lims.services.lims_files.lib.preprocess import preprocess_file
        from lims.services.lims_files.lib.serialize import serialize_file
        from lims.services.lims_files.lib.upload import upload_file
        from lims.services.lims_files.messages.publishers import FileServiceMessagePublisher
        file_category = request.POST[FileUploadOption.FILE_CATEGORY]
        file_context = request.POST[FileUploadOption.FILE_CONTEXT]
        file = request.FILES.get('file')

        exclude_args = [FileUploadOption.FILE_CATEGORY, FileUploadOption.FILE_CONTEXT]
        list_args = [FileUploadOption.RELATED_BARCODES]
        addl_args = {k: v for k, v in request.POST.items() if k not in exclude_args + list_args}
        addl_args.update({k: request.POST.getlist(k) for k in list_args})
        file_obj, file = preprocess_file(cls, file_category, file_context, file, **addl_args)
        upload_file(file_obj, file)

        FileServiceMessagePublisher().add_event(payload=serialize_file(file_obj, request.get_host()))
        return file_obj


class RelatedEntity(models.Model):
    barcode = models.CharField(max_length=50, null=True)
    metadata = jsonfield.JSONField()


