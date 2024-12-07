from flask import Flask, request, render_template
from googlesearch import search

app = Flask(__name__)

def google_search(query, num_results=10, domain=""):
    """
    Search Google for a given query and return a list of result links, filtered by domain type if specified.

    :param query: The search query.
    :param num_results: Number of search results to return (default is 10).
    :param domain: The type of domain to filter (e.g., ".com", ".org").
    :return: A list of URLs from the search results.
    """
    try:
        if domain:
            query += f" site:{domain}"
        results = []
        for link in search(query, num_results=num_results):
            results.append(link)
        return results
    except Exception as e:
        return [f"Error: {e}"]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        domain = request.form.get('domain')
        if query:
            num_results = int(request.form.get('num_results', 10))
            results = google_search(query, num_results, domain)
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
