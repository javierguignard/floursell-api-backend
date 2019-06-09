from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from utils.models import GenericModel


class RowMaterial(GenericModel):
    '''
    Products that I can consume
    '''
    title = models.CharField(_('Producto'), max_length=128)
    observations = models.TextField(_('Observaciones'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= _('Materias Primas')
        verbose_name = _('Materia Prima')

class RowMaterialPrice(GenericModel):
    sell = models.ForeignKey(RowMaterial, verbose_name=_('Venta'), on_delete=models.CASCADE)
    amount = models.FloatField(_('Precio de venta'))
    deprecated = models.FloatField(_('Activo'), default=False)

    class Meta:
        verbose_name_plural= _('Precios de la Materia Prima')
        verbose_name = _('Precio de la Materia Prima')

    deprecated.help_text=_(
        'Solo puede haber 1 precio por producto, si activa este, los otros se desactivan.')




class Product(GenericModel):
    '''
    Products that I can make
    '''
    title = models.CharField(_('Producto'), max_length=128)
    observations = models.TextField(_('Observaciones'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= _('Productos')
        verbose_name = _('Producto')


class ProductItem(models.Model):
    """
    Abrastract and generic class of Items of list of products
    """
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Cantidad"))

    class Meta:
        abstract = True


class ProductPrice(GenericModel):
    sell = models.ForeignKey(Product, verbose_name=_('Venta'), on_delete=models.CASCADE)
    amount = models.FloatField(_('Precio de venta'))
    deprecated = models.BooleanField(_('Activo'), default=False)

    def __str__(self):
        return '{} (${.2f})'.format(self.sell, self.amount)

    class Meta:
        verbose_name_plural= _('Precios de Productos')
        verbose_name = _('Precio de Producto')

    deprecated.help_text=_(
        'Solo puede haber 1 precio por producto, si activa este, los otros se desactivan.')


class Production(GenericModel):
    sell_amount = models.FloatField(_('Precio de venta'))
    produccion_amount = models.FloatField(_('Precio de venta'))


class RowMaterialItem(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Cantidad"))

class ProductionItems(ProductItem):
    production = models.ForeignKey(Production, on_delete=models.CASCADE)

class Deliver(GenericModel):
    pass

class DeliverItems(ProductItem):
    production = models.ForeignKey(Production, on_delete=models.CASCADE)

class ProducedReport(GenericModel):
    def __str__(self):
        return '{}'.format(self.creation_date.strftime('%d/%m/%Y %H:%M hs'))

    class Meta:
        verbose_name = _('plantilla')
        verbose_name_plural = _('plantillas')

class ProducedItems(ProductItem):
    report = models.ForeignKey(ProducedReport, verbose_name=_('plantilla'), related_name='items', on_delete=models.CASCADE)