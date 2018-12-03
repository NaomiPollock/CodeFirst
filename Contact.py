from flask import Flask, render_template, request
app = Flask("MyApp")
@app.route("/Contact", methods=["POST"])
def sign_up():
	form_data = request.form()
	print (form_data["email"])
	return "All OK"
