from flask import Flask, jsonify, request

app = Flask(__name__)

'''
Metodos:
GET -> obtener informacion (en la mayoria de los casos de una BD)
POST -> Crear informacion (en la mayoria de casos en una BD)
PUT -> actualizar informacion (actualiza la informacion de algun objeto guardado en la BD)
DELETE -> borrar informacion (borra algun objeto de la BD)
'''

@app.route("/")
def root():
    return "root"

#metodo GET
@app.route("/users/<user_id>")
def get_user(user_id):
    user = {'id': user_id, 'name': 'test', 'telefono': '999-666-333'}
    # /users/2654?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

#metodo POST
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    data["status"] = "User Create"
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
