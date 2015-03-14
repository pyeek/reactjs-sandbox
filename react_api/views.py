from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}

@view_config(route_name='like', renderer='templates/like.jinja2')
def like(request):
    return {}

@view_config(route_name='comments', renderer='templates/comments.jinja2')
def comments(request):
    return {}

@view_config(route_name='comments_api', renderer='json')
def comments_api(request):
    return {}

@view_config(route_name='product_api', renderer='json')
def products_api(request):
    return {
        'data': [
            {'category': 'Sporting Goods', 'price': '$49.99', 'stocked': True, 'name': 'Football'},
            {'category': 'Sporting Goods', 'price': '$9.99', 'stocked': True, 'name': 'Baseball'},
            {'category': 'Sporting Goods', 'price': '$29.99', 'stocked': False, 'name': 'Basketball'},
            {'category': 'Electronics', 'price': '$99.99', 'stocked': True, 'name': 'iPod Touch'},
            {'category': 'Electronics', 'price': '$399.99', 'stocked': False, 'name': 'iPhone 5'},
            {'category': 'Electronics', 'price': '$199.99', 'stocked': True, 'name': 'Nexus 7'}
            ]
        }
