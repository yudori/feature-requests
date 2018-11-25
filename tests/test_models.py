# -*- coding: utf-8 -*-
"""Model unit tests."""
from datetime import date
import pytest

from feature_requests.features.models import FeatureRequest

from tests.factories import FeatureRequestFactory


@pytest.mark.usefixtures('db')
class TestFeatureRequest:
    """FeatureRequest tests."""

    def test_str_representation(self):
        """Test user factory."""
        request = FeatureRequestFactory(id=1, client=FeatureRequest.CLIENT_A,
                                        client_priority=1, title='New title')
        assert str(request) == '<Feature(1 - New title)>'

    def test_save(self, db):
        """Test single save."""
        old_count = len(FeatureRequest.query.all())
        request = FeatureRequest(title='Request 1', client=FeatureRequest.CLIENT_A,
                                 client_priority=1, target_date=date(2018, 3, 3),
                                 product_area=FeatureRequest.PRODUCT_AREA_CLA)
        request.save()
        assert len(FeatureRequest.query.all()) == old_count + 1

    def test_save_with_same_client_priority(self, db):
        """Test save with existing  client priority."""
        old_count = len(FeatureRequest.query.all())
        request = FeatureRequest(title='Request 1', client=FeatureRequest.CLIENT_A,
                                 client_priority=2, target_date=date(2018, 3, 3),
                                 product_area=FeatureRequest.PRODUCT_AREA_CLA)
        request1 = request.save()
        request = FeatureRequest(title='Request 2', client=FeatureRequest.CLIENT_A,
                                 client_priority=2, target_date=date(2018, 4, 3),
                                 product_area=FeatureRequest.PRODUCT_AREA_BIL)
        request2 = request.save()
        assert len(FeatureRequest.query.all()) == old_count + 2
        assert (request1.title, request1.client_priority) == ('Request 1', 3)
        assert (request2.title, request2.client_priority) == ('Request 2', 2)