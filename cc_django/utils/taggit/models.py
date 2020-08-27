from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class TaggedUUIDItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    """使用 UUIDField 时需要使用此中间模型"""

    class Meta:
        verbose_name_plural = verbose_name = '标签管理'
        app_label = "taggit"
        index_together = [["content_type", "object_id"]]
        unique_together = [["content_type", "object_id", "tag"]]
