from django.db import models


class Comment(models.Model):
    description = models.TextField(null=True,blank=True)


CHOICES = (
    ('1', 'Да'),
    ('2', 'Нет'),
)


class RiskAcceptability(models.Model):
    value = models.CharField(max_length=10, choices = CHOICES)
    comments = models.OneToOneField(Comment,
                                    on_delete=models.CASCADE, primary_key=True)
VALUES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class LevelRisk(models.Model):
    value = models.IntegerField()
    risk_acceptability = models.OneToOneField(RiskAcceptability,
                                    on_delete=models.CASCADE, primary_key=True)

class DegreeProbability(models.Model):
    value = models.IntegerField(choices=VALUES)
    level_risk = models.OneToOneField(LevelRisk,
                                    on_delete=models.CASCADE, primary_key=True)

class WeightConsequence(models.Model):
    value = models.IntegerField(choices = VALUES)
    degree_probability = models.OneToOneField(DegreeProbability,
                                    on_delete=models.CASCADE, primary_key=True)

class Measure(models.Model):
    title = models.TextField()
    weight_consequences = models.OneToOneField(WeightConsequence,
                                    on_delete=models.CASCADE, primary_key=True)



TERMS = (
    ('A', 'Аварийные(A)'),
    ('HT', 'Нетипичные(HT)'),
    ('T', 'Типичные(T)'),
)



class EventCondition(models.Model):
    value = models.CharField(max_length=30, choices=TERMS)
    measures = models.OneToOneField(Measure,
                                   on_delete=models.CASCADE, primary_key=True)


class Effect(models.Model):
    description = models.TextField()
    event_conditions = models.OneToOneField(EventCondition,
                                   on_delete=models.CASCADE, primary_key=True)


class DangerousEvent(models.Model):
    description = models.TextField()
    effects = models.OneToOneField(Effect,
                                   on_delete=models.CASCADE, primary_key=True)


class Danger(models.Model):
    description = models.TextField()
    dangerous_event = models.OneToOneField(DangerousEvent,
                                           on_delete=models.CASCADE, primary_key=True)


class ProfessionRisk(models.Model):
    description = models.TextField()
    danger = models.ManyToManyField(Danger)

class Profession(models.Model):
    description = models.TextField()
    profession_risk = models.ManyToManyField(ProfessionRisk)
