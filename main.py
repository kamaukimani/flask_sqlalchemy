from app import create_app

app=create_app()

@app.route('/')
def home():
    return "My api is working"

if __name__=="__main__":
    app.run(port=5555,debug=True)