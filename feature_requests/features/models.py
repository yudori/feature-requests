# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from sqlalchemy_utils.types.choice import ChoiceType

from feature_requests.database import Column, Model, SurrogatePK, db, relationship


class FeatureRequest(SurrogatePK, Model):
    """A stored feature request."""

    CLIENT_A = u'CLIENT_A'
    CLIENT_B = u'CLIENT_B'
    CLIENT_C = u'CLIENT_C'

    CLIENTS = [
        (CLIENT_A, u'Client A'),
        (CLIENT_B, u'Client B'),
        (CLIENT_C, u'Client C'),
    ]

    PRODUCT_AREA_POL = u'POL'
    PRODUCT_AREA_BIL = u'BIL'
    PRODUCT_AREA_CLA = u'CLA'
    PRODUCT_AREA_REP = u'REP'

    PRODUCT_AREAS = [
        (PRODUCT_AREA_POL, u'Policies'),
        (PRODUCT_AREA_BIL, u'Billing'),
        (PRODUCT_AREA_CLA, u'Claims'),
        (PRODUCT_AREA_REP, u'Reports'),
    ]

    __tablename__ = 'feature_requests'

    title = Column(db.String(127), nullable=False, info={'label': 'Title'})
    description = Column(db.Text, nullable=True, info={'label': 'Description'})
    client = Column(ChoiceType(CLIENTS, impl=db.String(8)), nullable=False, info={'label': 'Client'})
    client_priority = Column(db.Integer, nullable=False, info={'label': 'Client Priority'})
    target_date = Column(db.Date, nullable=False, info={'label': 'Target Date'})
    product_area = Column(ChoiceType(PRODUCT_AREAS, impl=db.String(4)), nullable=False, info={'label': 'Product Area'})
    
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Feature({0} - {1})>'.format(self.id, self.title)

    def save(self, commit=True):
        """Save the record."""
        # optimize priority logic for few database calls
        client_requests = db.session.query(FeatureRequest).filter(
            FeatureRequest.client == self.client,
            FeatureRequest.client_priority >= self.client_priority).order_by(
            FeatureRequest.client_priority)
        if client_requests.first() and int(client_requests.first().client_priority) == int(self.client_priority):
            current_priority = int(self.client_priority)
            update_requests = []
            for request in client_requests:
                if int(request.client_priority) == current_priority:
                    current_priority += 1
                    request.client_priority = current_priority
                    update_requests.append(request)
                else:
                    break
            if update_requests:
                db.session.bulk_save_objects(update_requests)
        db.session.add(self)
        if commit:
            db.session.commit()                
        return self
