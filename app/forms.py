from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    amount = DecimalField("Số tiền", validators=[DataRequired()])
    category = SelectField("Danh mục", choices=[
        ('Ăn uống', 'Ăn uống'),
        ('Đi lại', 'Đi lại'),
        ('Mua sắm', 'Mua sắm'),
        ('Giải trí', 'Giải trí'),
        ('Khác', 'Khác')
    ])
    description = StringField("Mô tả")
    date = DateField("Ngày", format='%Y-%m-%d')
    submit = SubmitField("Thêm chi tiêu")