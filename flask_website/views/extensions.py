from flask import Module, render_template, jsonify
from flask_website.utils import request_wants_json
from flask_website.listings.extensions import extensions

mod = Module(__name__, url_prefix='/extensions')


@mod.route('/')
def index():
    if request_wants_json():
        return jsonify(extensions=[ext.to_json() for ext in extensions])
    return render_template('extensions/index.html', extensions=extensions)


@mod.route('/creating/')
def creating():
    return redirect(url_for('docs.show', page='extensiondev'), 301)