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



class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=QuoteCategory
        fields='__all__'

class CustomPKRelatedField(serializers.PrimaryKeyRelatedField):
    # A PrimaryKeyRelatedField derivative that uses named field for the display value.

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "title")
        super(CustomPKRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)

class QuoteDetailSerializer(serializers.ModelSerializer):
    categories = CustomPKRelatedField(queryset=QuoteCategory.objects.all(), many=True)
    quote=serializers.CharField(style={'base_template': 'textarea.html'})
    class Meta:
        model = Quote
        fields = ['quote','categories']




class QuoteCreateSerializer(serializers.ModelSerializer):
    # categories=QuoteCategory.objects.all()
    # category_choice=[(str(category.id), category.title) for category in categories]
    # categories=serializers.MultipleChoiceField(choices=category_choice)
    # categories = CustomPKRelatedField(queryset=QuoteCategory.objects.all(), many=True, required=True)
    # author=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    author=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Quote
        fields=['quote','author', 'categories']

