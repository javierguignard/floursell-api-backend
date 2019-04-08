from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from utils.models import GenericModel
from production.models import ProductItem


class Customer(GenericModel):
    """
    The Costumer is a person that consume my products
    """
    name = models.CharField(_('Nombre'), max_length=128)
    address = models.CharField(_('Dirección'), max_length=256, null=True, blank=True)
    phone = models.CharField(_('Teléfono'), max_length=65, null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=128, null=True, blank=True)
    observations = models.TextField(_('Observaciones'), null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ('created_by', 'name')


class Order(GenericModel):
    """
    The order, is a list of products that my costumer needs
    """
    customer = models.ForeignKey(Customer, verbose_name=_('Cliente'), on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.customer, self.creation_date.strftime('%d/%m/%Y %H:%M hs'))

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')


class Sell(GenericModel):
    """
    The sell, is the list of products that I can deliver
    """
    STATUS = ((0, _('Cargada')), (1, _('Entregada')), (2, _('Rechazada')),)
    customer = models.ForeignKey(Customer, verbose_name=_('Cliente'), on_delete=models.CASCADE)
    status = models.SmallIntegerField(_('Estado'), choices=STATUS)

    def __str__(self):
        return '{} - {}'.format(self.customer, self.creation_date.strftime('%d/%m/%Y %H:%M hs'))

    class Meta:
        verbose_name = _('Venta')
        verbose_name_plural = _('Ventas')


class ItemOrder(ProductItem):
    order = models.ForeignKey(Order, verbose_name=_('Orden'), related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class ItemSell(ProductItem):
    amount = models.FloatField(_('Precio de venta'))
    sell = models.ForeignKey(Sell, verbose_name=_('Venta'),related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class Payment(GenericModel):
    """
    Payments that seller receive of customer.
    """
    customer = models.ForeignKey(Customer, verbose_name=_('Cliente'), on_delete=models.CASCADE)
    amount = models.FloatField(_('Ingresa'))

    def __str__(self):
        return '{} - {}'.format(self.customer, self.creation_date.strftime('%d/%m/%Y %H:%M'))

    class Meta:
        verbose_name = _('Pago del cliente')
        verbose_name_plural = _('Pagos del cliente')