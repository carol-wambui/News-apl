from app import app

if __name__ == '__main__':
    app.run()

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title)