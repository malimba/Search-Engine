from flask import Flask,render_template, url_for, request, redirect
from helpers import retrieve_search_results
app = Flask(__name__)

@app.route('/')
def index():
    # return redirect('/search')
    return render_template('search.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        search_query = str(request.args.get('search'))
        results_dict = retrieve_search_results(searchQuery=search_query)
        return render_template('searchresults.html', search_query=search_query, results_dict=results_dict)
    if request.method == 'POST':
        return '<h1>TODO</h1>'

if __name__ == '__main__':
    app.run()
