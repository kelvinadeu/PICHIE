from ..models import User,pitchie,Comment
from .forms import AddpitchieieieieieForm,AddComment,EditBio
from . import main
from flask import render_template,redirect,url_for,flash,request,abort
from flask_login import login_required
import datetime
from .. import photos,db

@main.route("/")
def index():
    pitchies = pitchies.query.all()
    title = "Home"
    return render_template("index.html", pitchie = pitchie,title = title)

@main.route("/pitchieieieieiee/<category>")
def categories(category):
    pitchies = None
    if category == "all":
        pitchies = pitchie.query.order_by(pitchie.time.desc())
    else:
        pitchies = pitchieieie.query.filter_by(category = category).order_by(pitchie.time.desc()).all()

    return render_template("pitchies.html", pitchies = pitchies, title = category.upper())

@main.route("/<uname>/add/pitchie", methods = ["GET","POST"])
@login_required
def add_pitchie(uname):
    form = AddpitchieForm()
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)
    title = "Add pitchie"
    if form.validate_on_submit():
        title = form.title.data
        pitchie = form.pitchie.data
        category = form.category.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
        new_pitchie = pitchie(title = title, content = pitchie, category = category,user = user, date = date,time = time)
        new_pitchie.save_pitchie()
        pitchies = pitchie.query.all()
        return redirect(url_for("main.categories",category = category))
    return render_template("add_pitchie.html",form = form, title = title)

@main.route("/<user>/pitchie/<pitchie_id>/add/comment", methods = ["GET","POST"])
@login_required
def comment(user,pitchie_id):
    user = User.query.filter_by(id = user).first()
    pitchie = pitchie.query.filter_by(id = pitchie_id).first()
    form = AddComment()
    title = "Add comment"
    if form.validate_on_submit():
        content = form.content.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
        new_comment = Comment(content = content, user = user, pitchieieieieie = pitchieieieieie,time = time, date = date )
        new_comment.save_comment()
        return redirect(url_for("main.view_comments", pitchie_id=pitchie.id))
    return render_template("comment.html", title = pitchie.title,form = form,pitchie = pitchie)

@main.route("/<pitchie_id>/comments")
@login_required
def view_comments(pitchie_id):
    pitchie = pitchie.query.filter_by(id = pitchie_id).first()
    title = "Comments"
    comments = pitchie.get_pitchie_comments()

    return render_template("view_comments.html", comments = comments,pitchie = pitchie,title = title)

@main.route("/profile/<user_id>")
@login_required
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    pitchies = pitchie.query.filter_by(user_id = user.id).order_by(pitchie.time.desc())
    title = user.name.upper()
    return render_template("profile.html", pitchies = pitchies, user = user,title = title)

@main.route("/<user_id>/profile")
def user(user_id):
    user = User.query.filter_by(id = user_id).first()
    pitchies = pitchie.query.filter_by(user_id = user.id).order_by(pitchie.time.desc())

    title = user.name.upper()
    return render_template("user.html", pitchiees = pitchies, user = user,title = title)

@main.route("/pic/<user_id>/update", methods = ["POST"])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    title = "Edit Profile"
    if "profile-pic" in request.files:
        pic = photos.save(request.files["profile-pic"])
        file_path = f"photos/{pic}"
        user.profile_pic = file_path
        db.session.commit()
    return redirect(url_for("main.profile", user_id = user.id))

@main.route("/<user_id>/profile/edit",methods = ["GET","POST"])
@login_required
def update_profile(user_id):
    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    form = EditBio()

    if form.validate_on_submit():
        bio = form.bio.data
        user.bio = bio
        db.session.commit()
        return redirect(url_for('main.profile',user_id = user.id))
    return render_template("update_profile.html",form = form,title = title)
