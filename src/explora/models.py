from django.db import models


class Block(models.Model):
    block_num = models.IntegerField(unique=True)
    block_time = models.DateTimeField(null=True)
    block_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.block_num


# class Transaction(models.Model):
#     pass


# class Action(models.Model):
#     pass
