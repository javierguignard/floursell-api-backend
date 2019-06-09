from rest_framework import serializers
from sells.models import Customer, Order, Sell, Payment, ItemOrder, ItemSell


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PaymentCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = ('product','quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = ItemOrderSerializer(many=True, read_only=False)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        creation_date = validated_data.get('creation_date')
        for track_data in items_data:
            ItemOrder.objects.create(order=order, **track_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        for track_data in items_data:
            if track_data.get('product'):
                ItemOrder.objects.filter(order=instance.id, product= track_data.get('product')).update(quantity = track_data.get('quantity'))
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = '__all__'


class ItemSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSell
        fields = ('id','product','quantity', 'amount')


class SellSerializer(serializers.ModelSerializer):
    items = ItemSellSerializer(many=True, read_only=False)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sell = Sell.objects.create(**validated_data)
        for track_data in items_data:
            ItemSell.objects.create(sell=sell, **track_data)
        return sell

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        for track_data in items_data:
            if track_data.get('product'):
                ItemSell.objects.filter(sell=instance.id, product= track_data.get('product')).update(quantity = track_data.get('quantity'))
        instance.save()
        return instance

    class Meta:
        model = Sell
        fields = '__all__'
