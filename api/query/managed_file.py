from typing import Any, Iterable, List, Optional

import graphene
from promise import Promise
from files.models import ManagedFile
from federation.directives import key, provides


@key(fields=['id'])
class ManagedFileType(graphene.ObjectType):

    class Meta:
        interfaces = (graphene.Node, )


    env = graphene.String()
    file_name = graphene.String()

    s3_bucket = graphene.String()
    s3_key = graphene.String()
    s3_base_name = graphene.String()
    s3_revision = graphene.Int()

    mime_type = graphene.String()
    category = graphene.String()
    context = graphene.String()

    #related_entities = graphene.ConnectionField('api.query.related_entity.RelatedEntityConnection')


    @staticmethod
    def resolve_env(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.env


    @staticmethod
    def resolve_file_name(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.file_name


    @staticmethod
    def resolve_s3_bucket(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.s3_bucket


    @staticmethod
    def resolve_s3_key(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.s3_key


    @staticmethod
    def resolve_s3_base_name(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.base_name


    @staticmethod
    def resolve_s3_revision(root: Any, info: graphene.ResolveInfo) -> graphene.Int:
        return root.s3_revision


    @staticmethod
    def resolve_mime_type(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.mime_type


    @staticmethod
    def resolve_category(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.category


    @staticmethod
    def resolve_context(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.context


    @staticmethod
    def resolve_related_entities(root: Any, info: graphene.ResolveInfo) -> graphene.String:
        return root.related_entities


    @classmethod
    def is_type_of(cls, root: Any, info: graphene.ResolveInfo) -> bool:
        return isinstance(root, ManagedFile)


    @classmethod
    def get_node(cls, info: graphene.ResolveInfo, decoded_id: str) -> Promise[Optional[Any]]:
        key = int(decoded_id)
        return info.context.loaders.managed_file.load(key)


@provides({'node': 'id'})
class ManagedFileConnection(graphene.Connection):

    class Meta:
        node = ManagedFileType


class Query(graphene.ObjectType):

    managed_file = graphene.Node.Field(ManagedFileType)
    managed_files = graphene.ConnectionField(ManagedFileConnection)

    @staticmethod
    def resolve_managed_file(root: None, info: graphene.ResolveInfo, **kwargs) -> Iterable[Any]:
        return ManagedFile.objects.all()

