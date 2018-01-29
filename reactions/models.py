from django.db import models


def transform(inp):
    res = ''
    num = ''
    for i in range(0, len(inp)):
        if (inp[i].isdigit()) and (inp[i-1].isalpha() or num):
            num += inp[i]
            if i == len(inp)-1:
                res += '<sub>' + num + '</sub>'
        elif num:
            res += '<sub>' + num + '</sub>'
            res += inp[i]
            num = ''
        else:
            res += inp[i]
            num = ''
    return res


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=32)
    variable = models.CharField(max_length=32)
    coefficient = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'


class Reaction(models.Model):
    materials = models.CharField(max_length=256)
    products = models.CharField(max_length=256)
    conditions = models.CharField(max_length=128, blank=True, null=True)
    difficulty = models.ForeignKey(DifficultyLevel, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)

    materials_trans = models.CharField(max_length=256, blank=True, null=True, default=None)
    products_trans = models.CharField(max_length=256, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        self.materials_trans = transform(self.materials)
        self.products_trans = transform(self.products)

        super(Reaction, self).save(*args, **kwargs)

    def __str__(self):
        return "Реакция №%s" % self.id

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'
