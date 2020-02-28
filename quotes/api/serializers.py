from rest_framework import serializers
from quotes.models import Quote,QuoteCategory




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
    quote=serializers.CharField(style={'base_template': 'textarea.html'})
    class Meta:
        model = Quote
        fields = ['quote','categories']

class QuoteCreateSerializer(serializers.ModelSerializer):
    categories=QuoteCategory.objects.all()
    category_choice=[(str(category.id), category.title) for category in categories]
    print(category_choice)
    # category_choice=[('1', 'happy'),('2', 'sad'), ('3', 'life')]
    categories=serializers.MultipleChoiceField(choices=category_choice)
    # author=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    author=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Quote
        fields=['quote','author', 'categories']


