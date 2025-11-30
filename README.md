# Cyber Toolkit - Kali Linux Style UI

A modern cybersecurity toolkit built with React + Vite, featuring a Kali Linux-inspired dark theme interface.

## Features

- 🎨 **Kali Linux-inspired Dark Theme** - Dark mode with neon blue accents (#2AB0FF)
- 📱 **Responsive Design** - Works on all devices
- 🎭 **Smooth Animations** - Fade transitions, hover effects, and button ripples
- 🔧 **Multiple Tools**:
  - Port Scanner
  - Ping Tool
  - Hash Generator (MD5, SHA1, SHA256)
- 🎯 **Collapsible Sidebar** - Clean navigation with slide animations

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to `http://localhost:5173`

### Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

## Project Structure

```
├── src/
│   ├── components/
│   │   ├── Sidebar.jsx
│   │   └── Sidebar.css
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── Dashboard.css
│   │   ├── PortScanner.jsx
│   │   ├── PortScanner.css
│   │   ├── PingTool.jsx
│   │   ├── PingTool.css
│   │   ├── HashGenerator.jsx
│   │   ├── HashGenerator.css
│   │   ├── About.jsx
│   │   └── About.css
│   ├── App.jsx
│   ├── App.css
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

## Technologies Used

- **React 18** - UI library
- **Vite** - Build tool and dev server
- **React Router v6** - Routing
- **React Icons** - Icon library
- **Crypto-JS** - Hash generation

## Theme Colors

- Background: `#0F0F0F`
- Accent: `#2AB0FF` (neon blue)
- Text Primary: `#ffffff`
- Text Secondary: `#b0b0b0`
- Border: `#1a1a1a`

## Disclaimer

This toolkit is for educational and authorized security testing purposes only. Always ensure you have proper authorization before performing any security assessments.

## License

MIT

