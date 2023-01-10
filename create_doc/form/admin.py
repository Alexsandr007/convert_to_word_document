from django.contrib import admin

from .models import *

admin.site.register(Profession)
admin.site.register(ProfessionRisk)
admin.site.register(Danger)
admin.site.register(DangerousEvent)
admin.site.register(Effect)
admin.site.register(EventCondition)
admin.site.register(Measure)
admin.site.register(WeightConsequence)
admin.site.register(DegreeProbability)
admin.site.register(LevelRisk)
admin.site.register(RiskAcceptability)
admin.site.register(Comment)
