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
        for track_data in items_data:
            ItemOrder.objects.create(order=order, **track_data)
        return order

    class Meta:
        model = Order
        fields = '__all__'


class ItemSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSell
        fields = '__all__'


class SellSerializer(serializers.ModelSerializer):
    items = ItemSellSerializer(many=True, read_only=False)

    class Meta:
        model = Sell
        fields = '__all__'
