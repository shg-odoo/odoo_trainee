from odoo import models, fields, api, exceptions
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string="Name" )

    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No", size=10, track_visibility='always') 


    age = fields.Integer(string="Age", compute='cal_age', store=True,)


    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    image = fields.Binary(string = "image")
    birthdate = fields.Date(string = "Date of Birth")
    dateTo = fields.Date(string='Date', default=datetime.today())
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], string='Gender')
    city = fields.Char(string = "City")
    bloodGroup = fields.Selection([
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ], string='Blood Group', default='B+')

    address = fields.Text(string="Address")
    pincode = fields.Char(string="Pincode")
    country = fields.Char(string="Country")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height (cm)")
    disabled = fields.Boolean(string="Physically Disabled?", default=False)
    active = fields.Boolean('Active', default=True)

    college_ids = fields.Many2one('college', string='College')

    hobbies_ids = fields.Many2many('hobbies', string='Hobbies')
    
    maths = fields.Integer(string="Maths")
    chemistry = fields.Integer(string="Chemistry")
    physics = fields.Integer(string="Physics")
    total = fields.Integer(string="Total")
    average = fields.Integer(string="Average")

    defaultName = fields.Char(string="Default Name")

    sequenceName = fields.Char(
        string="Student Sequence",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default="New",
    )

    state = fields.Selection([
            ('applied', 'Applied'),
            ('inProgress', 'In Progress'),
            ('underReview', 'Under Review'),
            ('result', 'Result'),
        ], string='Status', default='applied', readonly=True)


    def action_inProgress(self):
        for rec in self:
            rec.state = "inProgress"

    def action_underReview(self):
        for rec in self:
            rec.state = "underReview"

    def action_result(self):
        for rec in self:
            rec.state = "result"
    
    def action_restart(self):
        for rec in self:
            rec.state = "applied"

    @api.model
    def create(self, vals):
        if vals.get("sequenceName", "New") == "New":
            vals["sequenceName"] = (
                self.env["ir.sequence"].next_by_code("student.sequence") or "New"
            )
        result = super(student, self).create(vals)
        return result


    @api.depends("birthdate")
    def cal_age(self):
        for i in self:
            if i.birthdate:
                i.age = relativedelta(date.today(), i.birthdate).years


    @api.onchange("maths", "chemistry", "physics")
    def _result(self):
        for i in self:
            icollege_ids = fields.Many2one('college', string='College').total = i.maths + i.chemistry + i.physics
            i.average = (i.total)/3
    

    def student_college(self):
        print("Button Clicked")

    # def add_college(self):
    #     ids = self._context.get('active_ids')
    #     self.env['student'].browse(ids).write({'college_ids':self.college_ids})

    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s %s' % (rec.sequenceName, rec.name)))
    #     return res

    def test_recordset(self):
        for rec in self:
            print("Record Set Operation")
            students = self.env['student'].search([])
            print("Mapped Students...", students.mapped('name'))
            print("Sorted Students...", students.sorted(lambda o: o.write_date, reverse=True))
            print("Filtered Students...", students.filtered(lambda o: o.disabled))

            #Search
            students_male = self.env['student'].search([('gender', '=', 'male')])
            print("Male Students....", students_male)

            students_female = self.env['student'].search([('gender', '=', 'female')])
            print("Female Students....", students_female)

            #Search with OR
            students_male_or = self.env['student'].search(['|',('gender', '=', 'male'),('age', '=', 22)])
            print("Male Students Or Age = 22....", students_male_or)

            #Search with AND
            students_male_or = self.env['student'].search([('gender', '=', 'male'),('age', '=', 22)])
            print("Male Students and Age = 22....", students_male_or)


            #Search Count
            students_count = self.env['student'].search_count([])
            print("Student Count...", students_count)


            #Browse
            students_browse = self.env['student'].browse(1)
            print("Student Browse...", students_browse)

            #Exists
            if students_browse.exists():
                print("Record Found")
            else:
                print("No Record Found")

            # #Copy
            # students_copy = self.env['student'].browse(1)
            # students_copy.copy() 

            #Unlink
            # students_unlink = self.env['student'].browse(11)
            # students_unlink.unlink() 

            # #fields_get
            # students_get=self.env["student"]
            # print(students_get.field_get())

            #read
            students_read=self.env["student"]
            print(self.read(students_read))


    
class college(models.Model):
    _name = 'college'
    _description = "College Details"
    _rec_name = "collegeName"
    _inherit = "student"

    collegeName = fields.Char(string="College Name")
    collegeCity = fields.Char(string="College City")

    student_ids = fields.One2many('student','college_ids',string='Student')



class hobbies(models.Model):
    _name = 'hobbies'
    _description = "Student Hobbies"
    _rec_name = "hobbies"

    hobbies = fields.Char(string="Hobbies")


class admission(models.Model):
    _inherit = "student"

    eligible = fields.Boolean(
        string="Eligible For Admission", compute="_Eligible", store=True)

    @api.depends("age")
    def _Eligible(self):
        for i in self:
            if i.age >= 22:
                i.eligible = True
            else:
                i.eligible = False


# class AddCollege(models.TransientModel):
#     _name = "add.college"
#     _description = "Registration of College to Mutiple Student Records"
#     _rec_name = "addCity"
    

#     college_ids = fields.Char(string="College")
#     addCity = fields.Char(string="City")
#     def add_college(self):
#         vals={
#             'collegeName': self.college_ids,
#             'collegeCity' : self.addCity
#         }
#         self.env['college'].create(vals)