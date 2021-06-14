from rest_framework import serializers
from .models import Players, EntityStats


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['uuid', 'displayName']

class EntityStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityStats
        fields = ['player', 'entityType']

    def to_internal_value(self, data):
        try:
            try:
                obj_id = data['player']
                return {
                    'player': Players.objects.get(uuid=obj_id),
                    'entityType': data['entityType']
                }
            except KeyError:
                raise serializers.ValidationError(
                    'id is a required field.'
                )
            except ValueError:
                raise serializers.ValidationError(
                    'id must be an integer.'
                )
        except Players.DoesNotExist:
                raise serializers.ValidationError(
                    'Obj does not exist.'
                )