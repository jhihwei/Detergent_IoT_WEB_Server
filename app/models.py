from django.db import models

# Create your models here.
class sales(models.Model):
    total_flow = models.BigIntegerField(verbose_name ="累積總量")
    flow = models.BigIntegerField()
    income = models.BigIntegerField()
    gross_income = models.BigIntegerField()
    receipt = models.IntegerField()
    terminal_id = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = '銷售資料'
        db_table = "sales"
        ordering = ['-timestamp']
