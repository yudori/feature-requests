# -*- coding: utf-8 -*-
"""Features views."""
from datetime import datetime

from flask import Blueprint, render_template, request, flash

from feature_requests.features.forms import FeatureRequestForm
from feature_requests.features.models import FeatureRequest
from feature_requests.utils import flash_errors


blueprint = Blueprint('features', __name__, static_folder='../static')


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Features home."""
    form = FeatureRequestForm(request.form)
    if request.method == 'POST':
        if form.validate():
            feature_request = FeatureRequest(
                title=request.form.get('title'),
                description=request.form.get('description'),
                client=request.form.get('client'),
                client_priority=request.form.get('client_priority'),
                target_date=datetime.strptime(
                    request.form.get('target_date'), '%Y-%m-%d'
                ).date(),
                product_area=request.form.get('product_area'),
            )
            feature_request.save()
            flash('You have successfully logged your request', 'success')
        else:
            flash_errors(form)
    features = FeatureRequest.query.all()
    return render_template('features/home.html', form=form, features=features)
