from odoo import fields,models,api
from odoo.exceptions import ValidationError

class collegestudent(models.Model):
    _name='college.student'
    _description="student details"


    name=fields.Char(string="Name")
    sid=fields.One2many("college.teacher","t_id",string="student id")
    age=fields.Integer(string="Age")
    physics=fields.Integer(string="Physics")
    chemistry=fields.Integer(string="Chemistry")
    math=fields.Integer(string="Maths")
    phone=fields.Char(string="Phone_number")
    clg_name=fields.Char(string="College name")
    clg_id=fields.Many2one("colleges")
    course=fields.Char(string="Course")
    gender=fields.Selection([('male','Male'),('female','Female')],default="male"
    ,string="Gender")
    total_comp=fields.Integer(string="Total Compute")
    total=fields.Integer(string="Total",compute="sum")
    average=fields.Float(string="Average",compute="sum")
    image=fields.Binary(string="Image")
    age_group=fields.Selection([('major','Major'),('minor','Minor')]
    ,string="Group",compute="set_group")
    join_date=fields.Date(string="Join date")
    hobb_id=fields.Many2many("student.hobbies",string="Hobbies")
    
    @api.depends("physics","chemistry","math")
    def sum(self):
      for r in self:
        r.total=r.physics+r.chemistry+r.math
        r.average=r.total/3

    @api.onchange("physics","chemistry","math")
    def test(self):
      for rec in self:
        rec.total_comp=rec.physics+rec.chemistry+rec.math

    @api.constrains('age')
    def check_age(self):
          for rec in self :
            if rec.age <18 :
              raise ValidationError("Your age is too young:" )
  
        
    @api.depends("age")
    def set_group(self):
      for rec in self:  
        if rec.age > 20:
            rec.age_group='major'
        else:
            rec.age_group='minor'    


class Hobby(models.Model):
  _name="student.hobbies"
  _rec_name = "hobby"

  hobby=fields.Char()  

class allcollege(models.Model):
  _name="colleges"
  _description="All colleges"

  student_id=fields.One2many("college.student","clg_id")
  clg_name=fields.Char(string="college name")
  