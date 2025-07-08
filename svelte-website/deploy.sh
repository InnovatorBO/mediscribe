#!/bin/bash

# Deploy script for GitHub Pages

echo "🚀 Starting deployment process..."

# Build the project
echo "📦 Building project..."
npm run build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    
    # Create a temporary directory for deployment
    echo "📁 Preparing deployment files..."
    
    # Copy build files to a deployment directory
    cp -r dist/* ./
    
    echo "🎉 Deployment files ready!"
    echo ""
    echo "📋 Next steps:"
    echo "1. git add ."
    echo "2. git commit -m 'Deploy to GitHub Pages'"
    echo "3. git push origin main"
    echo ""
    echo "🌐 Your site will be available at: https://yourusername.github.io/your-repo-name/"
    
else
    echo "❌ Build failed! Please check for errors."
    exit 1
fi 