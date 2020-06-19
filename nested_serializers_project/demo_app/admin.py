
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from demo_app.models import Sport, Match, Market, Selection

class SportListFilter(admin.SimpleListFilter):
    title = _('Sport')
    parameter_name = 'sport__name'

    def lookups(self, request, model_admin):
        lookup_set = set()
        market_queryset = Sport.objects.all()
        for market_obj in market_queryset:
            lookup_set.add((market_obj.name,market_obj.name))
        return lookup_set

    def queryset(self, request, queryset):
        if self.value() is not None:
            name = self.value()
            return queryset.filter(sport__name=name)

class MarketListFilter(admin.SimpleListFilter):
    title = _('Market')
    parameter_name = 'market__name'

    def lookups(self, request, model_admin):
        lookup_set = set()
        market_queryset = Market.objects.all()
        for market_obj in market_queryset:
            lookup_set.add((market_obj.name,market_obj.name))
        return lookup_set

    def queryset(self, request, queryset):
        return queryset

class SportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['id','name']


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'odds', 'market')
    list_filter = ('odds', MarketListFilter)
    search_fields = ['id','name', 'odds', 'market__name']


class SelectionInline(admin.StackedInline):
    model = Selection
    extra = 1


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sport')
    list_filter = ('name', SportListFilter)
    fieldsets = [
        (None,        {'fields': ['name']}),
        ('Sport',     {'fields': ['sport']}),
    ]
    inlines = [SelectionInline]
    search_fields = ['id','name', 'sport__name']


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sport', 'market','startTime', 'status')
    list_filter = ('name', SportListFilter, MarketListFilter, 'status')
    fields = ['name', 'startTime', 'sport', 'market', 'status']
    search_fields = ['id','name', 'sport__name', 'market__name']

admin.site.register(Market, MarketAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Sport,SportAdmin)
admin.site.register(Selection, SelectionAdmin)