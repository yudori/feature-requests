# -*- coding: utf-8 -*-
"""Test forms."""
from datetime import date

from werkzeug.datastructures import MultiDict

from feature_requests.features.forms import FeatureRequestForm
from feature_requests.features.models import FeatureRequest


class TestFeatureRequestForm:
    """FeatureRequest form."""

    def test_validate_success(self, db):
        """Validate with success."""
        form = FeatureRequestForm(MultiDict({'title': 'Request 1', 'client': FeatureRequest.CLIENT_A,
                                             'client_priority': 1, 'target_date': '2018-12-09',
                                             'product_area': FeatureRequest.PRODUCT_AREA_BIL}))
        assert form.validate() is True

    def test_validate_failure(self, db):
        """Fail validation."""
        form = FeatureRequestForm(MultiDict({'title': 'Request 1', 'client': FeatureRequest.CLIENT_A,
                                             'client_priority': 1, 'target_date': '2018-13-09',
                                             'product_area': FeatureRequest.PRODUCT_AREA_BIL}))
        assert form.validate() is False
        assert 'Not a valid date value' in form.target_date.errors

        form = FeatureRequestForm(MultiDict({'title': 'Request 1', 'client': FeatureRequest.CLIENT_A,
                                             'client_priority': 1, 'target_date': '2018-12-09',
                                             'product_area': 'BILL'}))
        assert form.validate() is False
        assert 'Not a valid choice' in form.product_area.errors