# -*- coding: utf-8 -*-
"""Features forms."""
from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm

from .models import FeatureRequest


class FeatureRequestForm(ModelForm, FlaskForm):
    """Feature Request form."""

    class Meta:
        model = FeatureRequest
