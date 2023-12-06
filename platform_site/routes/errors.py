# Third-party Imports
from flask import Blueprint, render_template
from flask_login import current_user

# Local Imports
errors = Blueprint('routes/errors', __name__)

# @errors.app_errorhandler(404)
# def error_404(error):
#     return render_template('errors/404.html', user=current_user), 404

# @errors.app_errorhandler(403)
# def error_403(error):
#     return render_template('errors/403.html', user=current_user), 403

# @errors.app_errorhandler(500)
# def error_500(error):
#     return render_template('errors/404.html', user=current_user), 500