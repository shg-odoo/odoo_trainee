from odoo import  fields, models

class Userslist(models.Model):
    _name = 'user.list'
    _description = "Engineers and Clients detail"

    user_id = fields.Integer()
    role = fields.Char(string="role")
    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    # mobile_no = fields.Char(string="mobile_no")
    # password = fields.Char(string="password")
    # address = fields.Char(string="Address", translate=True)
    # session = fields.Char(string="session")
    # specialist = fields.Char(string="specialist", translate=True)
    # experience  = fields.Char(string="experience", translate=True)
    # birthday = fields.Date(string="Birthday", required=True)
    # age = fields.Integer(compute="calculate_age", store=True)
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    # physics = fields.Integer()
    # chemistry = fields.Integer()
    # total = fields.Integer(string="Total")
    # average = fields.Float()
    # total_compute = fields.Integer(compute="_compute_total", store=True)
    # sem_fee = fields.Integer(string="Fee per semester")
    # enrollment_no = fields.Integer(string="Enrollment number")
    # branch = fields.Char(string="Branch")