# -*- coding: utf-8 -*-
from datetime import datetime, time


import logging

from odoo import models, fields, api, _
from odoo.fields import Datetime
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.model
    def retrieve_dashboard(self):
        result = {
            'all_my_sales': 0,
            'last_7_days': 0,
            'qty_draft_orders': 0,
            'qty_sale_orders': 0,
            'order_today':0

        }

        today = datetime.today().date()
        start_of_day = Datetime.to_string(datetime.combine(today, time.min))
        end_of_day = Datetime.to_string(datetime.combine(today, time.max))

        so = self.env['sale.order']
        result['order_today'] = so.search_count(
            [('create_date', '>=', start_of_day), ('create_date', '<=', end_of_day)])
        result['total_customer'] = len(so.search([]).mapped('partner_id').ids)

        return result
