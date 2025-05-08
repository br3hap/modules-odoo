# -*- coding: utf-8 -*-

import base64
import io
import openai
import PyPDF2

import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class PartnerDocument(models.Model):
    _name = 'partner.document'
    _description = 'Documentos del contacto'

    name = fields.Char('Nombre del Documento')
    partner_id = fields.Many2one('res.partner', string='Contacto', required=True, ondelete='cascade')
    document_file = fields.Binary(string='Archivo')
    document_content = fields.Text('Contenido Extraído')


    def action_extract_document_content(self):
        for r in self:
            if r.document_file:
                file_content = base64.b64decode(r.document_file)
                extracted_text = r.extract_text_from_pdf(file_content)

                if extracted_text:
                    processed_text = r.call_openai(extracted_text)
                    r.document_content = processed_text
                else:
                    r.document_content = 'No se pudo extraer texto del documento'


    def extract_text_from_pdf(self, file_content):
        try:
            reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text
        except Exception:
            return ''


    def call_openai(self, prompt_text):
        config = self.env['partner.ai.settings'].search([], limit=1)
        if not config or not config.openai_api_key:
            raise ValueError('No se encontró configuracion de IA')
        
        openai.api_key = config.openai_api_key

        response = openai.ChatCompletion.create(
            model=config.openai_model or "gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente que extrae y resume contenido de documentos."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=config.temperature or 0.2,
            max_tokens=1500,

        )

        return response['choices'][0]['message']['content']
        






