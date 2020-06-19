
from demo_app.models import Match, Sport, Market, Selection
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')

class MarketSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = Market
        fields = ('id', 'name','sport')

class SelectionSerializer(serializers.ModelSerializer):
    market = MarketSerializer(many=True)
    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds', 'market')

class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime', 'status')



class MatchDetailSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    market = MarketSerializer()
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime', 'sport', 'market', 'status')




