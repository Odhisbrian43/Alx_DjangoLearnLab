from .models import Book, Author
from rest_framework import serializers
from datetime import date

#Book serializer including all relevant fields.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        
        #Date validatore making sure future date is not entered raising an error for a future date.
        def date_validator(self,data):
            today = date.today()
            if(data['publicatyion_year']) > today:
                raise serializers.ValidationError("The date entered is in the future, please confirm.")
            return data()

#Author serializer with a nested bookserializer and for all related books per author.
class AuthorSerializer(serializers.ModelSerializer):
    Books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']