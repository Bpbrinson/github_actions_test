from flask import Blueprint, redirect, url_for, render_template, flash
from app.form import Contact
from app.s3_utils import upload_to_s3

bp = Blueprint('main', __name__)

@bp.route("/contact_form", methods = ["GET", "POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        upload_to_s3(name, email, message)
        
        flash(f"Thank you {name}, for you input!!")
        return redirect(url_for('main.contact'))
    return render_template("contact_form.html", form = form)
                                      