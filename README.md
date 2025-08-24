# 🎯 Rian Hub - Multi-Functional Django Web Application

Welcome to **Rian Hub**, a comprehensive Django web application that serves as a personal hub containing various interactive tools and games. This project demonstrates modern web development practices with Django, featuring multiple integrated applications with data visualization and interactive user experiences.

## 🌟 Features

### 🏠 Main Hub
- **Landing Page**: Beautiful welcome interface with Lottie animations
- **Navigation Hub**: Easy access to all applications
- **Responsive Design**: Mobile-friendly Bootstrap interface

### 💰 Compound Interest Calculator
- Calculate compound interest with principal, rate, and time
- **Millionaire Timeline**: Find out when you'll become a millionaire!
- Calculation history with persistent storage
- Interactive pie charts for data visualization
- Input validation and error handling

### 🛒 E-Commerce Shop
- Product catalog with pricing
- Shopping cart functionality
- Purchase history tracking
- Sales analytics with visual charts
- Real-time cart updates

### ⚽ Football Team Selection
- Automated selection system based on age and gender criteria
- Selection history with detailed tracking
- Statistical analysis of applications
- Visual representation of selection data

### 🎮 Rock-Paper-Scissors Game
- Classic gameplay against computer opponent
- Game history tracking
- Win/loss/tie statistics
- Interactive pie charts showing performance
- Real-time game state updates

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Frontend**: Bootstrap 5, Chart.js, Lottie Animations
- **Deployment**: Vercel-ready configuration
- **Language**: Python 3.8+

## 📁 Project Structure

```
Rian_Hub/
├── interest_project/          # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── main/                    # Landing page app
├── calculator/              # Compound interest calculator
├── shop/                    # E-commerce functionality
├── football_selection/      # Team selection system
├── rps_game/               # Rock-Paper-Scissors game
├── templates/              # Shared templates
├── staticfiles/            # Static assets
└── manage.py              # Django management script
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Compound_calc
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to `http://127.0.0.1:8000`

## 🎯 Application Features

### Calculator App
- **Formula**: A = P(1 + r/100)^t
- **Millionaire Calculation**: Uses logarithmic formulas
- **Data Persistence**: All calculations saved to database
- **Visualization**: Interactive charts showing calculation trends

### Shop App
- **Product Management**: Add/view products
- **Cart System**: Add items and complete purchases
- **Analytics**: Sales tracking with visual reports
- **History**: Complete purchase history

### Football Selection App
- **Criteria**: Ages 14-20, Male gender
- **Automated Decisions**: Instant selection/rejection
- **Tracking**: Complete application history
- **Analytics**: Selection statistics and trends

### RPS Game App
- **Game Logic**: Classic Rock-Paper-Scissors rules
- **Statistics**: Win/loss ratios and trends
- **History**: Complete game history
- **Visualization**: Performance charts

## 📊 Data Models

The application uses several Django models to store data:

- **CalculationHistory**: Stores compound interest calculations
- **Product/CartItem/PurchaseHistory**: E-commerce data
- **SelectionHistory**: Football selection records
- **RPSHistory**: Game results and statistics

## 🎨 User Interface

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Bootstrap 5**: Modern, clean interface
- **Interactive Charts**: Real-time data visualization
- **Animations**: Lottie animations for enhanced UX
- **Form Validation**: Client and server-side validation

## 🔧 Configuration

### Environment Variables
The application supports environment-based configuration for:
- Database settings
- Debug mode
- Secret key management
- Static files configuration

### Deployment
- **Vercel Ready**: Configured for Vercel deployment
- **Static Files**: Properly configured for production
- **WSGI**: Production-ready WSGI configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Django framework for the robust backend
- Bootstrap for the responsive frontend
- Chart.js for beautiful data visualizations
- Lottie for smooth animations

## 📞 Contact

For questions, suggestions, or contributions, please open an issue on GitHub.

---

**Happy Coding! 🚀**
