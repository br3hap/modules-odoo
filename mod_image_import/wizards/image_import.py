# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Image_import(models.TransientModel):
    _name = 'image.import'
    _description = _('Importar Imágenes')

    model_id = fields.Many2one('ir.model', string='Modelo')
    field_reference_id = fields.Many2one(comodel_name='ir.model.fields', string='Campo de referencia')
    field_imagen_id = fields.Many2one(comodel_name='ir.model.fields', string='Campo Imagen en el modelo seleccionado')
    image_ids = fields.Many2many(comodel_name='ir.attachment', string='Imágenes')
    error_log = fields.Text(string="Errores durante la importación", readonly=True)



    def import_image(self):
        self.error_log = False

        errores = []

        for r in self.image_ids:
            image_name = r.name.split('.')[0].strip()

            try:
                item = self.env[self.model_id.model].search([(self.field_reference_id.name, '=', image_name)], limit=1)
                if item:
                    item.update({self.field_imagen_id.name: r.datas})
                else:
                    errores.append(f"No se encontró un registro con {self.field_reference_id.name} = '{image_name}'")
            except Exception as e:
                errores.append(f"Error al procesar imagen '{r.name}': {str(e)}")

        if errores:
            self.error_log = "\n".join(errores)
        else:
            self.error_log = "Importación completada sin errores."
