from flask import Blueprint
from app.controllers.categories_controller import (
    create_category,
    list_categories,
    update_category,
    get_category_by_id,
    delete_category
) 

bp = Blueprint('categories_bp', __name__, url_prefix='/categories')

bp.post('')(create_category)
bp.get('')(list_categories)
bp.get('/<int:id>')(get_category_by_id)
bp.delete('/<int:id>')(delete_category)
bp.patch('/<int:id>')(update_category)