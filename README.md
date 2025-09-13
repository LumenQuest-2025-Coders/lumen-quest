# Subscription Management System - Frontend

A React + Tailwind CSS frontend for a comprehensive subscription management system that integrates with a Python FastAPI backend.

## Features

- **Landing Page**: Hero section with features and call-to-action
- **Authentication**: Login/Register with role-based routing (Admin/Company/User)
- **JWT Management**: Secure token storage and API integration
- **Responsive Design**: Mobile-first Tailwind CSS styling
- **Role-based Routing**: Different dashboards based on user roles

## Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── AuthForm.js     # Generic authentication form
│   ├── Footer.js       # Site footer
│   ├── Navbar.js       # Navigation bar
│   └── PlanCard.js     # Subscription plan display
├── context/            # React context providers
│   └── AuthContext.js  # Authentication state management
├── hooks/              # Custom React hooks
│   └── useAuth.js      # Authentication hook
├── pages/              # Page components
│   ├── Landing.js      # Home/landing page
│   ├── Login.js        # User login
│   └── Register.js     # User registration
├── services/           # API integration
│   └── api.js          # Backend API calls
└── App.js              # Main application component
```

## Backend Integration

The frontend integrates with all backend modules:

- **Authentication**: JWT token management
- **User Management**: Registration, profile updates
- **Company Management**: Company creation and management
- **Plan Management**: Subscription plan operations
- **Subscription Management**: Full subscription lifecycle
- **Discount Management**: Coupon and discount handling
- **Analytics**: Revenue and usage analytics
- **Notifications**: Automated email notifications

## Role-based Routing

- **Admin**: `/admin/dashboard` - System administration
- **Company**: `/admin/plans` - Plan management
- **User**: `/plans` - Plan selection and subscription management

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit REACT_APP_API_URL to match your backend
   ```

3. Start development server:
   ```bash
   npm start
   ```

## API Configuration

Set `REACT_APP_API_URL` in your `.env` file to point to your FastAPI backend (default: `http://localhost:8000`).

## Technologies

- **React 18**: Modern React with hooks
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first styling
- **Axios**: HTTP client for API calls
- **Context API**: State management