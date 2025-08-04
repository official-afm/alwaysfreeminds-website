# app.py - Main Flask Application
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, verify_jwt_in_request, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///buymindinsights.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-change-this')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize extensions
db = SQLAlchemy(app)
cors = CORS(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # user, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    featured = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'excerpt': self.excerpt,
            'content': self.content,
            'category': self.category,
            'author': self.author,
            'featured': self.featured,
            'published': self.published,
            'image': self.image_url,
            'publishedAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='new')  # new, read, replied
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100))
    subscribed = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# API Routes

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})

# Blog Routes
@app.route('/api/blog/posts')
def get_blog_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    search = request.args.get('search')
    
    query = BlogPost.query.filter_by(published=True)
    
    if category and category != 'All':
        query = query.filter_by(category=category)
    
    if search:
        query = query.filter(
            db.or_(
                BlogPost.title.contains(search),
                BlogPost.excerpt.contains(search),
                BlogPost.content.contains(search)
            )
        )
    
    posts = query.order_by(BlogPost.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'posts': [post.to_dict() for post in posts.items],
        'total': posts.total,
        'pages': posts.pages,
        'current_page': page
    })

@app.route('/api/blog/posts/<slug>')
def get_blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug, published=True).first()
    if not post:
        return jsonify({'error': 'Failed to submit contact form'}), 500

# Newsletter Routes
@app.route('/api/newsletter/subscribe', methods=['POST'])
def subscribe_newsletter():
    data = request.json
    email = data.get('email')
    name = data.get('name', '')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # Check if already subscribed
    existing = Newsletter.query.filter_by(email=email).first()
    if existing:
        if existing.subscribed:
            return jsonify({'message': 'Already subscribed'}), 200
        else:
            existing.subscribed = True
            db.session.commit()
            return jsonify({'message': 'Resubscribed successfully'}), 200
    
    newsletter = Newsletter(email=email, name=name)
    
    try:
        db.session.add(newsletter)
        db.session.commit()
        
        # Here you would integrate with email service (ConvertKit, Mailchimp, etc.)
        # add_to_email_list(email, name)
        
        return jsonify({'message': 'Subscribed successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to subscribe'}), 500

@app.route('/api/newsletter/unsubscribe', methods=['POST'])
def unsubscribe_newsletter():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    newsletter = Newsletter.query.filter_by(email=email).first()
    if newsletter:
        newsletter.subscribed = False
        db.session.commit()
    
    return jsonify({'message': 'Unsubscribed successfully'}), 200

# Admin Routes (Protected)
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    user = User.query.filter_by(email=email, role='admin').first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role
            }
        }), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/admin/posts', methods=['GET'])
def admin_get_posts():
    try:
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
        return jsonify([post.to_dict() for post in posts])
    
    except Exception as e:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/api/admin/posts', methods=['POST'])
def admin_create_post():
    try:
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        data = request.json
        
        # Generate slug from title
        import re
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', data['title'].lower())
        slug = re.sub(r'\s+', '-', slug).strip('-')
        
        # Ensure unique slug
        base_slug = slug
        counter = 1
        while BlogPost.query.filter_by(slug=slug).first():
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        post = BlogPost(
            title=data['title'],
            slug=slug,
            excerpt=data['excerpt'],
            content=data['content'],
            category=data['category'],
            author=data.get('author', user.name),
            featured=data.get('featured', False),
            published=data.get('published', False),
            image_url=data.get('image_url')
        )
        
        db.session.add(post)
        db.session.commit()
        
        return jsonify(post.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create post'}), 500

@app.route('/api/admin/posts/<int:post_id>', methods=['PUT'])
def admin_update_post(post_id):
    try:
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        post = BlogPost.query.get_or_404(post_id)
        data = request.json
        
        post.title = data.get('title', post.title)
        post.excerpt = data.get('excerpt', post.excerpt)
        post.content = data.get('content', post.content)
        post.category = data.get('category', post.category)
        post.featured = data.get('featured', post.featured)
        post.published = data.get('published', post.published)
        post.image_url = data.get('image_url', post.image_url)
        post.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify(post.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update post'}), 500

@app.route('/api/admin/contacts')
def admin_get_contacts():
    try:
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        contacts = Contact.query.order_by(Contact.created_at.desc()).all()
        
        return jsonify([{
            'id': c.id,
            'name': c.name,
            'email': c.email,
            'subject': c.subject,
            'message': c.message,
            'status': c.status,
            'created_at': c.created_at.isoformat()
        } for c in contacts])
    
    except Exception as e:
        return jsonify({'error': 'Unauthorized'}), 401

# Database initialization
@app.before_first_request
def create_tables():
    db.create_all()
    
    # Create admin user if it doesn't exist
    admin = User.query.filter_by(email='admin@buymindinsights.com').first()
    if not admin:
        admin = User(
            email='admin@buymindinsights.com',
            name='Admin',
            role='admin'
        )
        admin.set_password('changeme123')  # Change this!
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)({'error': 'Post not found'}), 404
    
    # Get related posts (same category, exclude current post)
    related_posts = BlogPost.query.filter(
        BlogPost.category == post.category,
        BlogPost.id != post.id,
        BlogPost.published == True
    ).limit(3).all()
    
    return jsonify({
        'post': post.to_dict(),
        'related': [p.to_dict() for p in related_posts]
    })

@app.route('/api/blog/featured')
def get_featured_posts():
    posts = BlogPost.query.filter_by(featured=True, published=True).limit(3).all()
    return jsonify([post.to_dict() for post in posts])

# Contact Routes
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.json
    
    # Basic validation
    required_fields = ['name', 'email', 'subject', 'message']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400
    
    contact = Contact(
        name=data['name'],
        email=data['email'],
        subject=data['subject'],
        message=data['message']
    )
    
    try:
        db.session.add(contact)
        db.session.commit()
        
        # Here you would typically send an email notification
        # send_contact_notification(contact)
        
        return jsonify({'message': 'Contact form submitted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify