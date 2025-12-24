from rest_framework import serializers
from ...models import Product, ProductCategory, ProductBrand

class ProductSerializers(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField()
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    
    class Meta:
        model = Product
        fields = [
            "id",  # ← اضافه کردن
            "title",
            "slug",
            "brand",  # ← اضافه کردن (مهم!)
            "stock_quantity",  # ← اضافه کردن
            "short_description",  # ← اضافه کردن
            "description",  # ← اضافه کردن
            "price",
            "snippet",
            "category",
            "is_active",
            "is_delete",
            "relative_url",
            "absolute_url",
        ]
        read_only_fields = []  # همه فیلدها قابل نوشتن باشند

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("is_active", None)
        rep["category"] = CategorySerializer(instance.category.all(), many=True).data
        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["title", "id"]