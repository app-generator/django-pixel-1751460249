# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    date amm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    numero amm = models.CharField(max_length=255, null=True, blank=True)
    cip_sn = models.CharField(max_length=255, null=True, blank=True)
    conditionnement = models.CharField(max_length=255, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Medicament(models.Model):

    #__Medicament_FIELDS__
    nom commercial = models.CharField(max_length=255, null=True, blank=True)
    forme pharmaceutique = models.CharField(max_length=255, null=True, blank=True)
    voie d'administration = models.CharField(max_length=255, null=True, blank=True)
    titulaire = models.CharField(max_length=255, null=True, blank=True)

    #__Medicament_FIELDS__END

    class Meta:
        verbose_name        = _("Medicament")
        verbose_name_plural = _("Medicament")


class Composition(models.Model):

    #__Composition_FIELDS__
    principe actif = models.CharField(max_length=255, null=True, blank=True)
    dosage = models.CharField(max_length=255, null=True, blank=True)
    unite = models.CharField(max_length=255, null=True, blank=True)

    #__Composition_FIELDS__END

    class Meta:
        verbose_name        = _("Composition")
        verbose_name_plural = _("Composition")


class Presentation(models.Model):

    #__Presentation_FIELDS__
    numero amm = models.CharField(max_length=255, null=True, blank=True)
    date amm = models.CharField(max_length=255, null=True, blank=True)
    cip = models.CharField(max_length=255, null=True, blank=True)
    conditionnement = models.CharField(max_length=255, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)

    #__Presentation_FIELDS__END

    class Meta:
        verbose_name        = _("Presentation")
        verbose_name_plural = _("Presentation")


class Forme(models.Model):

    #__Forme_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Forme_FIELDS__END

    class Meta:
        verbose_name        = _("Forme")
        verbose_name_plural = _("Forme")


class Laboratoire(models.Model):

    #__Laboratoire_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Laboratoire_FIELDS__END

    class Meta:
        verbose_name        = _("Laboratoire")
        verbose_name_plural = _("Laboratoire")


class Voie D'Administration(models.Model):

    #__Voie D'Administration_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Voie D'Administration_FIELDS__END

    class Meta:
        verbose_name        = _("Voie D'Administration")
        verbose_name_plural = _("Voie D'Administration")


class Classe Thérapeutique(models.Model):

    #__Classe Thérapeutique_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Classe Thérapeutique_FIELDS__END

    class Meta:
        verbose_name        = _("Classe Thérapeutique")
        verbose_name_plural = _("Classe Thérapeutique")


class Substance(models.Model):

    #__Substance_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Substance_FIELDS__END

    class Meta:
        verbose_name        = _("Substance")
        verbose_name_plural = _("Substance")



#__MODELS__END
