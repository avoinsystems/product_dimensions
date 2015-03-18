# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name': 'Product Dimensions',
    'version': '1.0',
    'category': 'Product',
    'sequence': 14,
    'description': """
Product Dimensions
==================
Add dimensions (length, width and height) products. Find the volume automatically when you change one of these dimensions.
    """,
    'author': 'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'depends': [
        'product',
    ],
    'data': [
        'product_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: