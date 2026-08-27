from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Website</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
            }
            header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            nav {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            nav h1 {
                font-size: 1.8rem;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin-left: 2rem;
                transition: opacity 0.3s;
            }
            nav a:hover {
                opacity: 0.8;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem 1rem;
            }
            .hero {
                text-align: center;
                padding: 3rem 0;
            }
            .hero h2 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                color: #667eea;
            }
            .hero p {
                font-size: 1.1rem;
                color: #666;
                margin-bottom: 2rem;
            }
            .btn {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 5px;
                text-decoration: none;
                transition: background 0.3s;
            }
            .btn:hover {
                background: #764ba2;
            }
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            .feature-card {
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-card h3 {
                color: #667eea;
                margin-bottom: 1rem;
            }
            footer {
                background: #333;
                color: white;
                text-align: center;
                padding: 2rem 0;
                margin-top: 3rem;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <h1>MyWeb</h1>
                <div>
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                </div>
            </nav>
        </header>

        <div class="container">
            <div class="hero">
                <h2>Welcome to My Website</h2>
                <p>Build amazing web experiences with Python and Flask</p>
                <a href="/contact" class="btn">Get Started</a>
            </div>

            <div class="features">
                <div class="feature-card">
                    <h3>🚀 Fast</h3>
                    <p>Lightning-fast performance and quick loading times for the best user experience.</p>
                </div>
                <div class="feature-card">
                    <h3>🔒 Secure</h3>
                    <p>Built with security in mind to protect your data and privacy.</p>
                </div>
                <div class="feature-card">
                    <h3>📱 Responsive</h3>
                    <p>Works perfectly on all devices - desktop, tablet, and mobile.</p>
                </div>
            </div>
        </div>

        <footer>
            <p>&copy; 2024 MyWeb. All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Us</title>
        <style>
            body { font-family: Arial; max-width: 1200px; margin: 0 auto; padding: 2rem; }
            h1 { color: #667eea; }
        </style>
    </head>
    <body>
        <h1>About Us</h1>
        <p>We are a team dedicated to creating amazing web experiences.</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f'''
        <html>
        <head><style>body {{ font-family: Arial; padding: 2rem; }}</style></head>
        <body>
            <h1>Thank You, {name}!</h1>
            <p>We received your message and will get back to you soon at {email}.</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
        '''
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact Us</title>
        <style>
            body { font-family: Arial; max-width: 600px; margin: 0 auto; padding: 2rem; }
            form { display: flex; flex-direction: column; }
            input, textarea { padding: 0.5rem; margin: 0.5rem 0; }
            button { background: #667eea; color: white; padding: 0.75rem; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background: #764ba2; }
        </style>
    </head>
    <body>
        <h1>Contact Us</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
            <button type="submit">Send Message</button>
        </form>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
