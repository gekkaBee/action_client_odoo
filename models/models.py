from odoo import api, models, fields


class ActionClientExample(models.Model):
    _name = 'action.client.example'

    char_field = fields.Char()
    integer_fields = fields.Integer()
    date_field = fields.Date()
    datetime_field = fields.Datetime()

    @staticmethod
    def return_client_action():
        return {
            'res.model': 'action.client.example',
            'type': 'ir.actions.client',
            'tag': 'action_client_example',
            'target': 'new'
        }

