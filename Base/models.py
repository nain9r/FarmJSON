from django.db import models


class Scene1Choice1(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene1Choice2(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene1Choice3(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene2Choice1(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene2Choice2(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene2Choice3(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene3Choice1(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene3Choice2(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene3Choice3(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene4Choice1(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene4Choice2(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene4Choice3(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene5Choice1(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene5Choice2(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class Scene5Choice3(models.Model):
    text = models.CharField(max_length=1000)
    consequence = models.CharField(max_length=1000)


class IntroStep(models.Model):
    introStep = models.CharField(max_length=200)


class Intro1(models.Model):
    intro13 = models.CharField(max_length=200)


class Intro2(models.Model):
    intro2= models.CharField(max_length=200)