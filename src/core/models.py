from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


CATEGORY_CHOICES = (("S", "Shirt"), ("SW", "Sport wear"), ("OW", "Outwear"))

LABEL_CHOICES = (("P", "primary"), ("S", "secondary"), ("D", "danger"))


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product-detail", kwargs={"slug": self.slug})


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    queryset = Item.objects.filter(slug=slug).order_by("-id")
    exists = queryset.exists()
    if exists:
        new_slug = f"{slug}-{queryset.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Item)
