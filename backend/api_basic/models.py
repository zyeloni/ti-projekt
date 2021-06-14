from django.db import models

class Players(models.Model):
    uuid = models.CharField(max_length=36,unique=True)
    displayName = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UUID: {uid} Name: {name}".format(uid=self.uuid, name=self.displayName)

class EntityStats(models.Model):
    entityType = models.CharField(max_length=20)
    player = models.ForeignKey(Players, related_name='entityStats_on_Players', on_delete=models.CASCADE)


    def __str__(self):
        return "EntityType {type} on Player: {uid}".format(uid=self.player, type=self.entityType)

class BlockStats(models.Model):
    blockType = models.CharField(max_length=30)
    player = models.ForeignKey(Players, related_name='blockStats_on_Players', on_delete=models.CASCADE)

    def __str__(self):
        return "BlockType {type} on Player: {uid}".format(uid=self.player, type=self.blockType)
