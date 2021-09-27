from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'
    _description = "Employee Full-Details"


    fname = fields.Char(string="FirstName")
    lname = fields.Char(string="Lastname")
    employmentNo = fields.Integer(string="Employment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    html = fields.Html()
    bdate = fields.Date(string='Date of birth')
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    image = fields.Binary(string='Image')
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    percentage = fields.Integer(string="Percentage")
    maths = fields.Integer(string="Maths")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    income = fields.Integer(string="Income")
    age = fields.Integer(string="age",store=True)
    total = fields.Integer(string="total")
    working = fields.Boolean(string="Working",default=True)
    country_id = fields.Many2one('res.country', string='Country')
    college_id = fields.Many2one("student.college", string="College")
    name_seq = fields.Char(string="Student Sequence", required=True, copy=False, readonly=True, index=True, default=lambda self:('New'))



class college(models.Model):
    _name = "employee.college"
    _rec_name = "college_name"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    id1 = fields.One2many("employee", "college_id", string="College Id")



class country(models.Model):
    _name = "employee.country"
    _rec_name = "country_name"

    country_name = fields.Char(string="Country Name")
    current_city = fields.Char(string="Current city")
    id1 = fields.One2many("employee", "country_id", string="Country Id")