from . import serializers
from models import Contact

class ContactSerializer(serializers.ModelSerializers):
    class Mata:
        model = Contact
        filter = "__all__"
