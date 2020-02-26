from rest_framework import serializers
from quotes.models import Quote




class QuotesSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author.username', read_only=True)
    categories = serializers.StringRelatedField(many=True)
    pub_date = serializers.DateTimeField(format='%D', read_only=True)
    slugged_username=serializers.ReadOnlyField(source='author.slugged_username')
    class Meta:
        model = Quote
        fields = ['quote','author','categories','pub_date', 'slugged_username']
    
class QuoteDetailSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Quote
        fields = ['quote','categories']




