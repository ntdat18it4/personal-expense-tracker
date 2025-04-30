from flask import Blueprint, render_template, redirect, url_for
from .models import Expense
from .forms import ExpenseForm
from . import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('index.html', expenses=expenses)

@bp.route('/add', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(
            amount=form.amount.data,
            category=form.category.data,
            description=form.description.data,
            date=form.date.data or datetime.utcnow().date()
        )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_expense.html', form=form)