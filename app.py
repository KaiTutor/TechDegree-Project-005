from flask import render_template, url_for, request, redirect
from models import db, Project, app
from datetime import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/project-form', methods=['GET', 'POST'])
def project_form():
    if request.method == 'POST':

        date_str = request.form.get('date')
        optimized_date = None
        if date_str:
            optimized_date = datetime.strptime(date_str, '%Y-%m')


        new_project = Project(date=optimized_date, title=request.form['title'],
                      description=request.form['description'], skills=request.form['skills'],
                      link = request.form['github'])

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/project/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    
    if request.method == 'POST':

        date_str = request.form.get('date')
        optimized_date = None
        if date_str:
            optimized_date = datetime.strptime(date_str, '%Y-%m')


        project.title = request.form['title']
        project.date = optimized_date
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.link = request.form['github']
    
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editproject.html', project=project)


@app.route('/delete/<id>')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


@app.context_processor
def inject_projects():
    # This grabs all projects from the DB
    all_projects = Project.query.all()
    # This makes 'projects' available to EVERY .html file automatically
    return dict(projects=all_projects)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
