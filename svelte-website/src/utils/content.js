// Simple content management utility
export const pageContent = {
  home: {
    heading: 'Home Page'
  },
  
  about: {
    heading: 'About Page'
  },
  
  contact: {
    heading: 'Contact Page'
  }
}

// Function to get content for a specific page
export function getPageContent(pageName) {
  return pageContent[pageName] || pageContent.home
}

// Function to simulate API call
export function fetchPageContent(pageName) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(getPageContent(pageName))
    }, 300)
  })
} 