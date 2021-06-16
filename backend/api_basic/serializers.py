from rest_framework import serializers
from .models import Players, EntityStats, BlockStats, KillStats


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['id', 'uuid', 'displayName', 'createdAt']

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
class BlockStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockStats
        fields = ['player', 'blockType']

    def to_internal_value(self, data):
        try:
            try:
                obj_id = data['player']
                return {
                    'player': Players.objects.get(uuid=obj_id),
                    'blockType': data['blockType']
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

class KillStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KillStats
        fields = ['killer', 'victim', 'createdAt']
        depth = 1

    def to_internal_value(self, data):
        try:
            try:
                killer_id = data['killer']
                victim_id = data['victim']
                return {
                    'killer': Players.objects.get(uuid=killer_id),
                    'victim': Players.objects.get(uuid=victim_id)
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