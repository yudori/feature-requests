# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from datetime import date
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from feature_requests.database import db
from feature_requests.features.models import FeatureRequest


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class FeatureRequestFactory(BaseFactory):
    """FeatureRequest factory."""

    title = Sequence(lambda n: 'request{0}'.format(n))
    target_date = date(2018, 12, 5)
    product_area = FeatureRequest.PRODUCT_AREA_BIL

    class Meta:
        """Factory configuration."""

        model = FeatureRequest
