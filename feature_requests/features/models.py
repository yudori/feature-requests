# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from sqlalchemy_utils.types.choice import ChoiceType

from feature_requests.database import Column, Model, SurrogatePK, db, relationship


class FeatureRequest(SurrogatePK, Model):
    """A stored feature request."""

    CLIENTS = [
        (u'CLIENT_A', u'Client A'),
        (u'CLIENT_B', u'Client B'),
        (u'CLIENT_C', u'Client C'),
    ]

    PRODUCT_AREAS = [
        (u'POL', u'Policies'),
        (u'BIL', u'Billing'),
        (u'CLA', u'Claims'),
        (u'REP', u'Reports'),
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
