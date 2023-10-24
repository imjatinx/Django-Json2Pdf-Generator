from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class PreviewTemplate(models.Model):
    name = models.CharField(_("Template Name"), max_length=50, null=True, blank=True)
    templatePath = models.CharField(_("Path"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


