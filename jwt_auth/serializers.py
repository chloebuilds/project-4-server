from django.conf import settings
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Comparable to a virtual field in Mongoose. Password will only ever be acknowledge in
    # WRITE requests, so it will never include it in READ requests. We do this for the
    # password_confirmation field, too.
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    
    # We do this to add our own custom validation. Must be called validate for the serializer
    # to know what to use it for. The second argument, data, is the incoming request object
    def validate(self, data):
        # You can use `.pop` on a dictionary in Python, which will remove the property and
        # store it in the variable you assign it to. Do this for password & password_confirmation so
        # we can compare them to make sure they're the same and, if so, validate the password.
        password = data.pop("password")
        password_confirmation = data.pop("password_confirmation")
        
        # First compare the password and password_confirmation. If not, raise a ValidationError
        # and send back an error message.
        if password != password_confirmation:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match"})
        
        #! This is where we can use the password validator from Django. We use a try/except.
        #? `if not settings.DEBUG` means we don't validate in development but we do in production
        if not settings.DEBUG:
            try:
                # Run in through the built-in Django validator
                validation.validate_password(password=password)
            
            # Rename the ValidationError for clarity as we'll use the ValidationError from Django
            # But we'll also raise a serializers.ValidationError, which would get confusing!
            except ValidationError as err:
                raise serializers.ValidationError({"password": err.messages})
        
        # Attach the hashed password to the data dictionary.
        data["password"] = make_password(password)
        
        # So, we removed the original password and password_confirmation.
        # Compared and validated the password.
        # Then once that was all OK, hashed the password and added it back to the dictionary
        # So we can store it in the database
        return data
    
    class Meta:
        model = User
        fields = "__all__"