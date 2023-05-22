from django.db import models

# Create your models here.

# 여기에서 __all__이 의미하는 것은 * 기호를 사용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미이다.

__all__ = (
    'Tag',
    'Product',
    'ProductOption',
)




class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name = "태그명")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name = "상품명")
    tag_set = models.ManyToManyField(Tag, blank=True, verbose_name = "Tag:Product M:M 관계")

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='option_set', 
        related_query_name='option', 
        on_delete=models.CASCADE,
        verbose_name = "Product 테이블 외래키",
        )

    name = models.CharField(max_length=100, verbose_name = "옵션명")
    price = models.IntegerField(verbose_name = "상품 가격")

    def __str__(self):
        return self.name