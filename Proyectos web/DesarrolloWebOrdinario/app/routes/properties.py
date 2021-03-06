from flask import Blueprint, jsonify, request, session, render_template, redirect, url_for

from app.controllers import get_properties, add_properties, update_properties

properties_routes = Blueprint("properties_routes", __name__)

@properties_routes.route("/buscar", methods=["GET"])
def houses_page():
    return render_template("houses.html", filters=request.args)

@properties_routes.route("/ver/<id>", methods=["GET"])
def house_page(id:int):
    return render_template("house.html", data=get_properties.get_properties(id=id).get('0', {}))

@properties_routes.route("/editar", methods=["GET"])
def house_edit_page():

    if not "user" in session:
        return redirect(url_for("index"))

    data = {}
    if request.args.get('id', -1) != -1:
        data = get_properties.get_properties(id=request.args['id']).get('0', {})

    return render_template("home_cu.html", data=data)


@properties_routes.route("/", methods=["GET"])
def houses():
    properties = get_properties.get_properties(args= request.args)

    return jsonify(**properties)

@properties_routes.route("/<id>", methods=["GET"])
def house_by_id(id:int):
    properties = get_properties.get_properties(id= id)

    return jsonify(**properties)

@properties_routes.route("/", methods=["POST"])
def houses_post():    
    
    res = {"Error": "Usuario no autorizado"}

    if  "user" in session:
        res = add_properties.add_properties(request.form)

    return jsonify(**res)


@properties_routes.route("/", methods=["PUT"])
def houses_put():    

    res = {"Error": "Usuario no autorizado"}

    if "user" in session:
        res = update_properties.update_properties(request.form)

    return jsonify(**res)

@properties_routes.route("/", methods=["PATCH"])
def houses_patch():    
    
    res = {"Error": "Usuario no autorizado"}

    if "user" in session:
        res = update_properties.patch_properties(request.form)

    return jsonify(**res)