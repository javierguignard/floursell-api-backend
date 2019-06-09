from rest_framework import serializers
from production.models import Product, ProducedReport, ProducedItems

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProducedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducedItems
        fields = ('product','quantity')

class ProducedReportSerializer(serializers.ModelSerializer):
    items = ProducedItemSerializer(many=True, read_only=False)

    def create(self, validated_data):
        items_data = validated_data.pop('Product')
        report = ProducedReport.objects.create(**validated_data)
        creation_date = validated_data.get('creation_date')
        for track_data in items_data:
            ProducedItems.objects.create(ProducedReport=report, **track_data)
        return report

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        for track_data in items_data:
            if track_data.get('Product'):
                ProducedItems.objects.filter(ProducedReport=instance.id, product= track_data.get('product')).update(quantity = track_data.get('quantity'))
        instance.save()
        return instance

    class Meta:
        model = ProducedReport
        fields = '__all__'