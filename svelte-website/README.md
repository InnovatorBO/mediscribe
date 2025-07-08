# Svelte Website with Dropdown Navigation

A modern, responsive website built with Svelte featuring a dropdown navigation menu and dynamic content loading.

## Features

- 🎯 **3 Pages**: Home, About, and Contact pages
- 📱 **Responsive Design**: Works perfectly on all devices
- ⚡ **Dynamic Content**: JavaScript-powered content loading
- 🎨 **Modern UI**: Beautiful gradients and animations
- 🔽 **Dropdown Navigation**: Clean and intuitive menu
- 📝 **Contact Form**: Functional contact form with validation
- 🚀 **Fast Performance**: Built with Svelte for optimal speed

## Project Structure

```
svelte-website/
├── src/
│   ├── components/
│   │   └── Navigation.svelte    # Dropdown navigation component
│   ├── pages/
│   │   ├── Home.svelte         # Home page
│   │   ├── About.svelte        # About page
│   │   └── Contact.svelte      # Contact page
│   ├── styles/
│   │   └── global.css          # Global styles
│   ├── utils/
│   │   └── content.js          # Content management utilities
│   ├── App.svelte              # Main app component
│   └── main.js                 # Entry point
├── index.html                  # HTML template
├── package.json                # Dependencies and scripts
├── vite.config.js             # Vite configuration
└── README.md                  # This file
```

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd svelte-website
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:3000`

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Customization

### Adding New Pages

1. Create a new component in `src/pages/`
2. Add the page to the navigation menu in `src/components/Navigation.svelte`
3. Update the routing logic in `src/App.svelte`
4. Add content data to `src/utils/content.js`

### Styling

- Global styles are in `src/styles/global.css`
- Component-specific styles are in each Svelte component
- The design uses CSS Grid and Flexbox for responsive layouts

### Content Management

All dynamic content is managed in `src/utils/content.js`. You can easily modify:
- Page headings and descriptions
- Team member information
- Contact details
- Feature lists

## Deployment

### GitHub Pages

1. Build the project:
```bash
npm run build
```

2. Push to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

3. Enable GitHub Pages in your repository settings

### Other Platforms

The project can be deployed to any static hosting service:
- Netlify
- Vercel
- AWS S3
- Firebase Hosting

## Technologies Used

- **Svelte** - Frontend framework
- **Vite** - Build tool and dev server
- **CSS3** - Styling with modern features
- **JavaScript** - Dynamic content and interactions

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

If you have any questions or need help, please open an issue on GitHub. 