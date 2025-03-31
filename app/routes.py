from app import myapp_obj, db
from flask import render_template, redirect, url_for, request
from app.models import Recipe
from app.forms import RecipeForm

@myapp_obj.route("/recipes")
@myapp_obj.route("/")
def list_recipes():
    recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=recipes)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('list_recipes'))
    return render_template("add_recipe.html", form=form)

@myapp_obj.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe_detail.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:recipe_id>/delete")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('list_recipes'))