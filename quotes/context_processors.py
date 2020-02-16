from . models import QuoteCategory


def add_quotesCategory_to_context(request):
    quoteContext=QuoteCategory.objects.all().prefetch_related('quote_set')
    return {
        'quoteContext':quoteContext
    }



