# -*- coding: utf-8 -*-
"""View tests using WebTest.

See: http://webtest.readthedocs.org/
"""
from flask import url_for

from feature_requests.features.models import FeatureRequest

from tests.factories import FeatureRequestFactory


class TestFeatureRequestView:
    """Add new feature request."""

    def test_get_page(self, db, testapp):
        """Test render home page."""
        res = testapp.get('/')
        assert res.status_code == 200
        assert 'Feature Requests' in res

    def test_post_success(self, db, testapp):
        """Test add new feature request."""
        old_count = len(FeatureRequest.query.all())
        # Goes to homepage
        res = testapp.get('/')
        form = res.form
        form['title'] = 'Request 1'
        form['client'] = FeatureRequest.CLIENT_B
        form['client_priority'] = 2
        form['target_date'] = '2012-12-12'
        form['product_area'] = FeatureRequest.PRODUCT_AREA_BIL
        # Submits
        res = form.submit()
        assert res.status_code == 200
        assert len(FeatureRequest.query.all()) == old_count + 1
        assert 'You have successfully logged your request' in res

    def test_post_fail(self, db, testapp):
        """Test fail to add new feature request."""
        old_count = len(FeatureRequest.query.all())
        # Goes to homepage
        res = testapp.get('/')
        form = res.form
        form['title'] = 'Request 1'
        form['client'] = FeatureRequest.CLIENT_B
        form['client_priority'] = 2
        form['target_date'] = '133-133-2012'
        form['product_area'] = FeatureRequest.PRODUCT_AREA_BIL
        # Submits
        res = form.submit()
        assert res.status_code == 200
        assert len(FeatureRequest.query.all()) == old_count
        assert 'Not a valid date value' in res
