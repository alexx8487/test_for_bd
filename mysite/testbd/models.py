from django.db import models


class Transaction(models.Model):
    class Type(object):
        DEPOSIT = 1
        WITHDRAW = 2

        choices = (
            (DEPOSIT, u'out'),
            (WITHDRAW, u'in'),
        )

    date = models.DateTimeField(auto_now_add=True)
    type = models.SmallIntegerField(choices=Type.choices)

    class Meta(object):
        get_latest_by = 'date'
        ordering = ['-date']


class Purchase(Transaction):
    original_price = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __unicode__(self):
	    return '%s %s %s' % (self.date, self.type, self.original_price)