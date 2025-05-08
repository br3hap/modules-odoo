# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class PartnerAiSettings(models.Model):
    _name = 'partner.ai.settings'
    _description = 'PartnerAiSettings'

    name = fields.Char('Name', default='Configuracion General IA')
    openai_api_key = fields.Char('Api Key de OpenAI')
    openai_model = fields.Char('Modelo de OpenAI', default='gpt-4o')
    temperature = fields.Float('Temperatura', default=0.2)

    _sql_constraints = [
        ('unique_ai_config', 'UNIQUE(name)', 'Sólo puede existir una configuración de IA.')
    ]
