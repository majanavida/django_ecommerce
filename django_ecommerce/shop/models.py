from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
       
        
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
        
        
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='shop/products/%d/%m/%Y', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id ,self.slug])
        
    
    def __str__(self):
        return self.name