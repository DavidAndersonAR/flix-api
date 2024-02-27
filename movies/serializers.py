from django.db.models import Avg
from rest_framework import serializers
from actors.models import Actor
from genres.models import Genre
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("a data não é valida")
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo ta parecendo um texto meu querido..')
        return value


# Metodo mais trabalhoso
# class MovieSerializers(serializers):
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset = Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset=Actor.objects.all(),
#         many = True,
#     )
#     resume = serializers.CharField()

#     rate = serializers.SerializerMethodField(read_only = True)

#     def get_rate(self, obj):
#         reviews = obj.reviews.filter(stars__lte = 3)

#         if reviews:
#             sum_reviews = 0

#             for review in reviews:
#                 sum_reviews += review.stars

#             reviews_count = reviews.count()

#             return round(sum_reviews / reviews_count, 1)

#         return None

#     def validate_release_date(self, value):
#         if value.year < 1990:
#             raise serializers.ValidationError("a data não é valida")
#         return value
    
#     def validate_resume(self, value):
#         if len(value) > 200:
#             raise serializers.ValidationError('Resumo ta parecendo um texto meu querido..')
#         return value